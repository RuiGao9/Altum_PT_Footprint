def latlon_to_utm(lat, lon):
    """
    Convert latitude and longitude (WGS84) to UTM coordinates.

    Parameters:
        lat (float): Latitude in decimal degrees.
        lon (float): Longitude in decimal degrees.

    Returns:
        x (float): UTM Easting (meters).
        y (float): UTM Northing (meters).

    Note:
        - The target UTM zone is currently set to EPSG:32610 (UTM zone 10N).
        - If your area of interest is not in UTM zone 10N, replace "EPSG:32610" with the correct EPSG code.
        - For example, use "EPSG:32612" for UTM zone 12N (covers most of Utah).
    """
    from pyproj import Transformer

    transformer = Transformer.from_crs("EPSG:4326", "EPSG:32610", always_xy=True)  # Replace EPSG if you're not in UTM zone 10
    x, y = transformer.transform(lon, lat)
    
    return x, y
