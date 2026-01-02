from redis.asyncio import Redis
from dotenv import load_dotenv
import os


load_dotenv()

R_HOST = os.getenv("REDIS_URL") or "localhost"
R_PORT = os.getenv("REDIS_PORT") or 6379


try:
    rd = Redis(
        host=R_HOST,
        port=R_PORT,
        decode_responses=True
    )

except Exception as e:
    print("Error in Chache config: ", str(e))
