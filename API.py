import uvicorn
import asyncio
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/about")
def read_root():
    return JSONResponse({"Version": "0.1",
                         "AppName": "dockerContainerAPI",
                         "Description": """An API to be deployed in raspberry
                         pi slaves and master in order to control the 
                         docker containers running on that server."""})


async def runEvery10Seconds():
    while True:
        print('Running every 10 seconds')
        await asyncio.sleep(10)


async def runEverySecond():
    while True:
        print('Running every second')
        await asyncio.sleep(1)


# Define the lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    task = asyncio.create_task(runEvery10Seconds())
    task = asyncio.create_task(runEverySecond())
    yield
    # Teardown logic
    task.cancel()
    await task

app.router.lifespan_context = lifespan


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)