from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.caching.config import rd
from app.routes.user_routes import app as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await rd.ping()
    yield
    await rd.close()


app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
