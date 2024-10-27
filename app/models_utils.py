


from math import radians, sin, cos, sqrt, atan2
 

def haversine(lon1, lat1, lon2, lat2):
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    r = 6371000  # Radius of Earth in meters
    return r * c


# # Example coordinates
# lon1, lat1 = 120.9822, 14.6042  # Example: Manila, Philippines
# lon2, lat2 = 121.0583, 14.6760  # Example: Quezon City, Philippines

# distance = haversine(lon1, lat1, lon2, lat2)


def is_within_15_meters(lon1, lat1, lon2, lat2):
    # Earth’s radius in meters
    R = 6371000

    # Convert latitude and longitude from degrees to radians
    lat1_rad = radians(lat1)
    lat2_rad = radians(lat2)
    lon1_rad = radians(lon1)
    lon2_rad = radians(lon2)

    # Differences in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * sqrt(a)
    distance = R * c

    # Check if distance is within 15 meters
    return distance <= 15

