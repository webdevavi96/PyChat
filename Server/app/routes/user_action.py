from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.FollowerSchema import (
    SubscribeChannel,
    GetSubscribers,
)
from app.schemas.PostSchema import GetPost, NewPost, UpdatePost, DeletePost
from app.serializer.follower_serializer import serialize_follower
from app.serializer.post_serializer import serialize_post
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

    return {"status": 200, "message": "Success", "data": posts}


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
