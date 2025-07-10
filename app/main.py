from fastapi import FastAPI
from app.api.v1.routes_user import router as user_router

app = FastAPI(title="My FastAPI App with JWT & SQLAlchemy")

app.include_router(user_router, prefix="/api/v1/users", tags=["users"])
