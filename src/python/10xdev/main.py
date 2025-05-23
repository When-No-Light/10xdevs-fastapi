import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host="0.0.0.0",  # nosec B104
        port=5000,
        log_level="info",
        reload=True,
    )
