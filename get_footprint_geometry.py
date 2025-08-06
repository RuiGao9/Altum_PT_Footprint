def get_footprint_geometry(hfov_deg, vfov_deg, res_x, res_y, height_m):
    """
    Calculate the sensor footprint size and pixel size on the ground.

    Parameters:
        hfov_deg (float): Horizontal field of view in degrees.
        vfov_deg (float): Vertical field of view in degrees.
        res_x (int): Number of pixels in the horizontal direction (image width).
        res_y (int): Number of pixels in the vertical direction (image height).
        height_m (float): Sensor height above ground in meters.

    Returns:
        footprint_w (float): Footprint width on the ground (meters).
        footprint_h (float): Footprint height on the ground (meters).
        pixel_w (float): Pixel size in the width direction (meters).
        pixel_h (float): Pixel size in the height direction (meters).

    Notes:
        - The footprint is calculated using simple trigonometry, assuming a flat ground.
        - Pixel size is derived by dividing the footprint size by the number of pixels.
    """
    import math

    hfov_rad = math.radians(hfov_deg)
    vfov_rad = math.radians(vfov_deg)

    footprint_w = 2 * height_m * math.tan(hfov_rad / 2)
    footprint_h = 2 * height_m * math.tan(vfov_rad / 2)

    pixel_w = footprint_w / res_x
    pixel_h = footprint_h / res_y

    return footprint_w, footprint_h, pixel_w, pixel_h
