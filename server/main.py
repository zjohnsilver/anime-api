from fastapi import FastAPI
from server.config import settings
from server.routers import router

app = FastAPI(
    title=settings.get("PROJECT_NAME"),
)


@app.get("/", include_in_schema=False)
async def root():
    return "Hello"


app.include_router(router, prefix="/api")
