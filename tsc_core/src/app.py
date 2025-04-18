from fastapi import FastAPI
from tsc_core.src.routers.route_visualizer import router as route_visualizer_router

app = FastAPI()

app.include_router(route_visualizer_router)

