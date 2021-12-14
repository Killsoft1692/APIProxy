import os

import uvicorn
from motor import motor_asyncio
from fastapi import FastAPI

app = FastAPI()
client = motor_asyncio.AsyncIOMotorClient(os.environ.get("DB_URL"))

from views import *


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=9090,
        reload=True
    )
