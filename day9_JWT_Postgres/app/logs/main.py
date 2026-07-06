import time
from fastapi import FastAPI
from app.core.logging_config import logger
app = FastAPI()

@app.middleware("http")
async def log_requests(request, call_next):

    start = time.time()

    response = await call_next(request)

    process_time = (
        time.time() - start
    ) * 1000

    logger.info(
        f"{request.method} "
        f"{request.url.path} "
        f"{response.status_code} "
        f"{process_time:.2f}ms"
    )

    return response