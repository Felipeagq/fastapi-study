from fastapi import FastAPI
import uvicorn
from app.config.settings import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

@app.get("/")
async def hello_world_check():
        return {
            "title":settings.PROJECT_NAME,
            "version":settings.PROJECT_VERSION
        }


if __name__ == "__main__":
    uvicorn.run(
        "entrypoint:app",
        host="localhost",
        port=5000,
        workers=1,
        reload=True,
        log_level="info",
        use_colors=False
    )