from models.route import Route


def find_cost(origin_id, destination_id):
    route = Route.query.filter_by(origin_id=origin_id, dest_id=destination_id).first()
    if route is None:
        return -1
    return route.time


def closest_point(current_place, places):
    min_value = 9999999
    closest = ''
    distance = 0
    for place in places:
        distance = find_cost(current_place, place)
        if distance < min_value:
            min_value = distance
            closest = place
    return closest, distance


def find_ideal_route(places, start_point, origin_id):
    result = [start_point]
    total_distance = 0
    route = [x for x in places if x != start_point]

    while len(route) > 0:
        (closest, distance) = closest_point(result[len(result) - 1], route)
        result.append(closest)
        total_distance += distance
        route = [x for x in route if x != closest]

    index = result.index(origin_id)
    if index != 0:
        route = result[index:] + result[:index]
    else:
        route = result

    return route


def find_extreme_route(places, origin_id):
    candidates = []
    for i in range(0, len(places)):
        candidates.append(find_ideal_route(places, places[i], origin_id))

    min_value = 9999999
    best = []

    for i in range(0, len(places)):
        route = candidates[i]
        total_distance = 0
        for j in range(0, len(route)):
            if j == len(route) - 1:
                ideal_distance = find_cost(route[j], route[0])
            else:
                ideal_distance = find_cost(route[j], route[j+1])
            total_distance = total_distance + total_distance % ideal_distance
        if total_distance < min_value:
            min_value = total_distance
            best = route
    return best
