from fastapi import FastAPI
from routers import orders
from database import Base, engine


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(orders.router, prefix="/orders", tags=["orders"])

