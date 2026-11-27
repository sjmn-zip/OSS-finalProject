from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.map_view import HTMLmaker

router = APIRouter()


@router.get("/map", response_class=HTMLResponse) #"http://localhost:8000/map?lat=*&lng=*&name=*" 
def get_map(lat: float | None = None, lng: float | None = None, name : str | None = None):    
    return HTMLmaker(lat, lng, name)