import requests as rq
import os

"""Return (latitude, longitude) for a place name, or None if not found."""
def get_coords(place_name): 
    
    api_key = os.getenv("KAKAO_REST_API")
    if api_key is None:
        return None
    
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {"Authorization": f"KakaoAK {api_key}"}
    params = {"query": place_name}
    response = rq.get(url, headers = headers, params= params)
    if response.status_code != 200: #wrong_key
        return None
    
    result = response.json()

    docs = result["documents"]
    if len(docs) == 0:
        return None
    
    x = float(docs[0]["x"])
    y = float(docs[0]["y"])

    return (y, x)
# {
#   "documents": [                 # list of results (up to 15 by default, sorted by relevance)
#     {
#       "place_name": "경복궁",                      # place name
#       "address_name": "서울 종로구 세종로 1-1",      # lot-number address
#       "road_address_name": "서울 종로구 사직로 161", # road-name address ("" if none)
#       "x": "126.97689786832184",   # longitude  NOTE: string, not float
#       "y": "37.577613288258206",   # latitude   NOTE: string, not float
#       "category_group_code": "AT4",       # category code ("" if none)
#       "category_group_name": "관광명소",   # category name ("" if none)
#       "category_name": "여행 > 관광,명소 > 문화유적 > 고궁,궁",  # full category path
#       "phone": "02-3700-3900",     # phone number ("" if none)
#       "place_url": "http://place.map.kakao.com/18619553",  # Kakao Map detail page
#       "id": "18619553",            # Kakao place ID
#       "distance": ""               # distance in meters from given point ("" if no point given)
#     },
#     ...
#   ],
#   "meta": {
#     "total_count": 550,      # total number of matches
#     "pageable_count": 38,    # number of results actually retrievable
#     "is_end": False,         # whether this is the last page
#     "same_name": {...}       # region info when the query includes a place name
#   }
# }
#
# No results -> documents == [] (empty list, not an error)





