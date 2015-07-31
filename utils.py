def within_bbox(bbox, loc):
  """Determine whether given location is within given bounding box.

    Bounding box is a dict with ll_lon, ll_lat, ur_lon and ur_lat keys
    that locate the lower left and upper right corners.

    The loction argument is a tuple of longitude and latitude values.
    """

  return bbox['ll_lon'] < loc[0] < bbox['ur_lon'] and bbox['ll_lat'] < loc[1] < bbox['ur_lat']
