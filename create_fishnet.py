def create_fishnet(center_x, center_y, footprint_w, footprint_h, pixel_w, pixel_h, crs="EPSG:32610"):
    """
    Create a fishnet (grid) of polygons covering the sensor footprint area.

    Parameters:
        center_x (float): X coordinate (e.g., UTM Easting) of the center point.
        center_y (float): Y coordinate (e.g., UTM Northing) of the center point.
        footprint_w (float): Total width of the footprint (meters).
        footprint_h (float): Total height of the footprint (meters).
        pixel_w (float): Width of each pixel/grid cell (meters).
        pixel_h (float): Height of each pixel/grid cell (meters).
        crs (str): Coordinate Reference System for the output GeoDataFrame (default: "EPSG:32610").
                    This one should be changed according to your UTM zone. For example, if you are in UTM zone 12N, use "EPSG:32612".

    Returns:
        geopandas.GeoDataFrame: GeoDataFrame containing the grid polygons.
    """
    from shapely.geometry import box
    import geopandas as gpd

    cols = int(footprint_w / pixel_w)
    rows = int(footprint_h / pixel_h)

    minx = center_x - footprint_w / 2
    maxy = center_y + footprint_h / 2

    polygons = []
    for i in range(rows):
        for j in range(cols):
            x0 = minx + j * pixel_w
            y0 = maxy - i * pixel_h
            x1 = x0 + pixel_w
            y1 = y0 - pixel_h
            polygons.append(box(x0, y1, x1, y0))

    gdf = gpd.GeoDataFrame(geometry=polygons, crs=crs)
    return gdf
