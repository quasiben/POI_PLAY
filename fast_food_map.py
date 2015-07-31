import pandas as pd

from bokeh.plotting import ColumnDataSource, figure, show, output_file
from bokeh.models import HoverTool

from utils import within_bbox



df = pd.read_csv("POIWorld.csv")
df = df[['amenity', 'Latitude', 'Longitude', 'name']]
df = df[df.amenity == 'fast_food']

# US Bounding Box
bbox = {
  'lon': -5.23636,
  'lat': 53.866772,
  'll_lon': -127.350792,
  'll_lat': 24.983787,
  'ur_lon': -59.75925,
  'ur_lat': 44.951620 
}

df['locations'] = [within_bbox(bbox, loc) for loc in zip(df.Longitude.values, df.Latitude.values)]

df = df[df['locations']]

source = ColumnDataSource(data={'long': list(df.Longitude), 'lat': list(df.Latitude), 'name': list(df.name)})

output_file("fast_food.html", title="legend.py example")

TOOLS="pan,wheel_zoom,box_zoom,reset,hover"

p1 = figure(title="Fast Food of North America", tools=TOOLS, plot_width=800, plot_height=600)


p1.circle(df.Longitude, df.Latitude, size=2, source=source)
hover = p1.select(dict(type=HoverTool))

hover.tooltips = [
    ("Name", "@name"),
    ("Lat", "@lat"),
    ("Long", "@long"),
]

show(p1)

