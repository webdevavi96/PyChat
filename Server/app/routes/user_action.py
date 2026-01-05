from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.FollowerSchema import (
    SubscribeChannel,
    GetSubscribers,
)
from app.schemas.PostSchema import NewPost, UpdatePost, DeletePost
from app.schemas.GroupSchema import (
    CreateGroup,
    JoinGroup,
    LeaveGroup,
    DeleteGroup,
    AddMember,
    RemoveMember,
)
from app.models.Groups import Group
from app.models.GroupMembers import GroupMembers
from app.serializer.follower_serializer import serialize_follower
from app.serializer.post_serializer import serialize_post
from app.serializer.group_serializer import serialize_group
from app.decorators.cache_decor import rate_limiter
from app.models.Follower import Follower
from app.models.UserModels import User
from app.models.Posts import Post
from app.core.Session import get_db
from app.caching.config import rd
import json


app = APIRouter()


@app.post(
    "/follow", dependencies=[Depends(rate_limiter(max_requests=2, time_window=10))]
)
def toggle_follow(data: SubscribeChannel, db: Session = Depends(get_db)):

    _channel = (
        db.query(Follower)
        .filter(
            Follower.subscriber == data.subscriber, Follower.channel == data.channel
        )
        .first()
    )

    if not _channel:
        new_follower = Follower(
            channel=data.channel, subscriber=data.subscriber, isSubscribed=True
        )

        db.add(new_follower)
        db.commit()
        db.refresh(new_follower)

        return {"sattus": 201, "message": "Success"}

    db.query(Follower).filter(Follower.id == _channel.id).update(
        {Follower.isSubscribed: not bool(_channel.isSubscribed)}
    )

    db.commit()
    db.refresh(_channel)
    return {"status": 200, "message": "Success"}


@app.get(
    "/folloowers", dependencies=[Depends(rate_limiter(max_requests=2, time_window=10))]
)
async def get_followers(
    data: GetSubscribers, page: int = 1, size: int = 1, db: Session = Depends(get_db)
):

    offset = (page - 1) * size

    user = db.query(User).filter(User.id == data.channel).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    cached_followers = await rd.get(name=f"followers:{data.channel}")
    if cached_followers:
        return {
            "status": 200,
            "message": "Success",
            "data": json.loads(cached_followers),
        }

    followers = (
        db.query(Follower)
        .filter(Follower.channel == data.channel)
        .offset(offset=offset)
        .limit(limit=size)
        .all()
    )

    if not followers:
        raise HTTPException(status_code=404, detail="No followers founs")

    await rd.set(name=f"followers:{data.channel}", value=json.dumps(followers))
    return {"status": 200, "message": "Success", "data": followers, "page": page}


@app.post(
    "/create_post", dependencies=[Depends(rate_limiter(max_requests=2, time_window=10))]
)
def create_post(data: NewPost, db: Session = Depends(get_db)):

    if not db.query(User).filter(User.id == data.author).first:
        raise HTTPException(status_code=404, detail="User not found")

    new_post = Post(title=data.title, detail=data.detail, author=data.author)

    if not new_post:
        raise HTTPException(status_code=501, detail="Internal server error")

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return {"status": 201, "message": "Success"}


@app.get("/posts", dependencies=[Depends(rate_limiter(max_requests=2, time_window=10))])
async def get_all_posts(
    user_id: int, page: int = 1, size: int = 10, db: Session = Depends(get_db)
):

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid user Id")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    cached_posts = await rd.get(f"posts:{page}")

    if cached_posts:
        return {"status": 200, "message": "Success", "data": json.loads(cached_posts)}

    offset = (page - 1) * size
    posts = db.query(Post).order_by(Post.id).offset(offset).limit(size).all()

    if not posts:
        raise HTTPException(status_code=404, detail="No Posts found")

    await rd.set(name=f"posts:{page}", value=json.dumps(posts), ex=600)

    return {"status": 200, "message": "Success", "data": posts, "page": page}


@app.get("/post")
async def get_post(user_id: int, post_id: int, db: Session = Depends(get_db)):

    if not user_id or not post_id:
        raise HTTPException(status_code=401, detail="Invaid user id or post id")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    post_c_key = f"post:{post_id}"

    cached_post = await rd.get(name=post_c_key)

    if cached_post:
        return {"status": 200, "message": "Success", "data": json.loads(cached_post)}

    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    await rd.set(name=post_c_key, value=json.dumps(post))

    return {"status": 200, "message": "Success", "data": serialize_post(post)}


@app.get(
    "/delete_post", dependencies=[Depends(rate_limiter(max_requests=2, time_window=5))]
)
def delete_post(data: DeletePost, db: Session = Depends(get_db)):

    existing_post = (
        db.query(Post).filter(Post.id == data.id, Post.author == data.user_id).first()
    )

    if not existing_post:
        return {"status": 404, "message": "Post not found"}

    db.delete(existing_post)
    db.commit()

    return {"status": 200, "message": "Success"}


@app.post(
    "/create_group",
    dependencies=[Depends(rate_limiter(max_requests=2, time_window=10))],
)
def create_group(data: CreateGroup, db: Session = Depends(get_db)):

    group = Group(name=data.name, desc=data.desc, admin=data.admin_id)

    if not group:
        raise HTTPException(status_code=501, detail="Internal server error")

    db.add(group)
    db.commit()
    db.refresh(group)

    return {"status": 201, "message": "Success", "data": serialize_group(group)}


@app.post(
    "/join_group", dependencies=[Depends(rate_limiter(max_requests=2, time_window=10))]
)
def join_group(data: JoinGroup, db: Session = Depends(get_db)):

    group = db.query(Group).filter(Group.id == data.id).first()

    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    isInstance = group.members == data.member_id

    if isInstance:
        raise HTTPException(status_code=429, detail="Already joined this group")

    member = GroupMembers(group_id=data.id, user_id=data.member_id)

    if not member:
        raise HTTPException(status_code=501, detail="Internal server error")

    return {"status": 201, "message": "Success", "data": serialize_group(group)}


@app.post(
    "/add_memeber", dependencies=[Depends(rate_limiter(max_requests=2, time_window=10))]
)
def add_member(data: AddMember, db: Session = Depends(get_db)):

    existing = db.query(User).filter(User.member_of == data.id).first()

    if existing:
        raise HTTPException(status_code=409, detail="User already in this group")

    admin = db.query(User).filter(User.id == data.admin_id).first()

    if not admin:
        raise HTTPException(status_code=409, detail="You are not a admin of this group")

    user = db.query(User).filter(User.id == data.member_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_member = GroupMembers(group_id=data.id, user_id=data.member_id)

    db.add(new_member)
    db.commit()
    db.refresh(new_member)

    return {"status": 201, "message": "Success"}


@app.post(
    "/leave_group", dependencies=[Depends(rate_limiter(max_requests=2, time_window=10))]
)
def leave_group(data: LeaveGroup, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == data.member_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    group = db.query(Group).filter(Group.id == data.id).first()

    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    is_member = group.members == user.id
    if not is_member:
        raise HTTPException(status_code=409, detail="You are not part of this group")

    db.delete(is_member)
    db.commit()

    return {"status": 200, "message": "Success"}


@app.post(
    "/remove_member",
    dependencies=[Depends(rate_limiter(max_requests=3, time_window=10))],
)
def remove_member(data: RemoveMember, db: Session = Depends(get_db)):

    group = db.query(Group).filter(Group.id == data.id).first()

    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    is_admin = group.admin == data.admin_id

    if not is_admin:
        raise HTTPException(
            status_code=409, detail="You are not allowed to perform this action"
        )

    is_member = group.members == data.member_id
    if not is_member:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(is_member)
    db.commit()

    return {"status": 200, "message": "Success"}


@app.post(
    "/delete_group",
    dependencies=[Depends(rate_limiter(max_requests=2, time_window=10))],
)
def delete_group(data: DeleteGroup, db: Session = Depends(get_db)):

    group = db.query(Group).filter(Group.id == data.id).first()

    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    is_admin = group.admin == data.admin_id

    if not is_admin:
        raise HTTPException(
            status_code=404, detail="You are not allowed to perfrom this task"
        )

    db.delete(group)
    db.commit()

    return {"status": 200, "message": "Success"}


@app.get(
    "get_groups", dependencies=[Depends(rate_limiter(max_requests=2, time_window=10))]
)
async def get_groups(
    user_id: int, page: int = 1, size: int = 10, db: Session = Depends(get_db)
):

    offset = (page - 1) * size

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid user id")

    group_key = f"groups:{user_id}"
    _groups = await rd.get(name=group_key)

    if _groups:
        return {"status": 200, "message": "Success", "data": json.loads(_groups)}

    groups = (
        db.query(Group)
        .filter(Group.members == user_id)
        .offset(offset=offset)
        .limit(size)
        .all()
    )

    if not groups:
        raise HTTPException(status_code=404, detail="You are not the part of any group")

    await rd.set(name=group_key, value=json.dumps(groups), ex=600)

    return {"status": 200, "message": "Success", "data": groups}


@app.get(
    "/groups", dependencies=[Depends(rate_limiter(max_requests=3, time_window=15))]
)
async def get_group(user_id: int, group_id: int, db: Session = Depends(get_db)):

    if not user_id or not group_id:
        raise HTTPException(status_code=401, detail="User id or Group id is invalid")

    user_key = f"user:{user_id}"
    group_key = f"group:{group_id}"

    _user = await json.loads(await rd.get(name=user_key))
    _group = await json.loads(await rd.get(name=group_key))

    if _user and _group:
        is_member = _group.memmbers == _user.id

        if not is_member:
            raise HTTPException(
                status_code=404, detail="You are not a member of this group"
            )

        return {"status": 200, "message": "Success", "data": serialize_group(_group)}

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    group = (
        db.query(Group).filter(Group.id == group_id, Group.members == user.id).first()
    )

    if not group:
        raise HTTPException(
            status_code=404, detail="You are not a member of this group"
        )

    await rd.set(name=user_key, value=json.dumps(user))
    await rd.set(name=group_key, value=json.dumps(group))

    return {"status": 200, "message": "Success", "data": serialize_group(group)}
