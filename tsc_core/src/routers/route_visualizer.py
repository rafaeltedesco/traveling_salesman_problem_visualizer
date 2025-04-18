from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from tsc_core.src.data import locations
from tsc_core.src.services import greedy_tsp
import folium

router = APIRouter(tags=["Route Visualizer"])
templates = Jinja2Templates(directory="tsc_core/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("map.html", {"request": request, "locations": locations})

@router.post("/route", response_class=HTMLResponse)
async def route(request: Request, start_city: str = Form(...)) :
    route, distance = greedy_tsp(start_city, locations)
    m = folium.Map(location=locations[start_city], zoom_start=5)

    for city, coord in locations.items():
        folium.Marker(coord, popup=city).add_to(m)
    folium.PolyLine([locations[city] for city in route], color="blue", weight=2.5, opacity=1).add_to(m)
    folium.Marker(locations[start_city], popup=start_city, icon=folium.Icon(color='green')).add_to(m)

    map_html = m._repr_html_()
    
    return templates.TemplateResponse("map.html", {"request": request, "selected_city": start_city, "locations": locations, "route": route, "distance": distance, "map_html": map_html})