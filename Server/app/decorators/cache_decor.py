from fastapi import Request, HTTPException, status
from app.caching.config import rd


def rate_limiter(max_requests: int, time_window: int):

    async def dependency(request: Request):

        client_ip = request.client.host
        endpoint = request.url.path
        redis_key = f"rate_limit:{client_ip}:{endpoint}"

        current = await rd.get(redis_key)

        if current is None:
            await rd.set(redis_key, 1, ex=time_window)

        elif int(current) < max_requests:
            await rd.incr(redis_key)

        else:
            retry_after = await rd.ttl(redis_key)
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail=f"To many requests at same time. Please Retry after {retry_after} seconds",
                headers={"Retry-After": str(retry_after)},
            )

    return dependency
