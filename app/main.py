from fastapi import FastAPI
from app.wallets.routers import router


app = FastAPI(root_path='/api/v1')

app.include_router(router)
