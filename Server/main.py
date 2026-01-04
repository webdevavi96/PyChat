from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.caching.config import rd
from app.routes.user_routes import app as user_router
from app.routes.user_action import app as actions


@asynccontextmanager
async def lifespan(app: FastAPI):
    await rd.ping()
    yield
    await rd.close()


origins = ["http://localhost5173", "http://127.0.0.1:5173"]


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(actions)


@app.get("/")
def home():
    return {"status": 404, "message": "Page not found!"}
