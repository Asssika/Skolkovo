from fastapi import FastAPI
from app.wallets.routers import router


app = FastAPI(openapi_prefix='/api/v1')

app.include_router(router)
