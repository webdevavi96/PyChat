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


@app.post("/follow")
def toggle_follow(data: SubscribeChannel, db: Session = Depends(get_db)):

    _channel = db.query(Follower).filter(Follower.id == data.id).first()

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


@app.get("/folloowers")
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


@app.post("/create_post")
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


@app.get("/posts")
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


@app.get("/delete_post")
def delete_post(data: DeletePost, db: Session = Depends(get_db)):

    existing_post = (
        db.query(Post).filter(Post.id == data.id, Post.author == data.user_id).first()
    )

    if not existing_post:
        return {"status": 404, "message": "Post not found"}

    db.delete(existing_post)
    db.commit()

    return {"status": 200, "message": "Success"}


@app.post("/create_group")
def create_group(data: CreateGroup, db: Session = Depends(get_db)):

    group = Group(name=data.name, desc=data.desc, admin=data.admin_id)

    if not group:
        raise HTTPException(status_code=501, detail="Internal server error")

    db.add(group)
    db.commit()
    db.refresh(group)

    return {"status": 201, "message": "Success", "data": serialize_group(group)}


@app.post("/join_group")
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
