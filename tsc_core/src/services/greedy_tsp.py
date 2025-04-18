from .distance_calculator import geo_distance

def greedy_tsp(start, locations: dict):
    unvisited = set(locations.keys())
    unvisited.remove(start)
    path = [start]
    total = 0
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: geo_distance(current, city, locations))
        total += geo_distance(current, next_city, locations)
        path.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    
    total += geo_distance(current, start, locations)
    path.append(start)
    return path, total