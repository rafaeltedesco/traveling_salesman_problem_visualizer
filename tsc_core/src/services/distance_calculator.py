from geopy.distance import geodesic

def geo_distance(city_name_1, city_name_2, locations: dict):
    return geodesic(locations[city_name_1], locations[city_name_2]).km
