# Shiny Express

from maplibre import Layer, LayerType, Map, MapLibreRenderer, MapOptions
from maplibre.basemaps import OpenFreeMap
from maplibre.controls import GlobeControl, NavigationControl
from maplibre.sources import GeoJSONSource
from shiny import reactive
from shiny.express import input, render, ui

data = "https://docs.mapbox.com/mapbox-gl-js/assets/earthquakes.geojson"
layer_id = "earthquakes"

earthquakes = Layer(
    id=layer_id, type=LayerType.CIRCLE, source=GeoJSONSource(data=data)
).set_paint_props(circle_color="yellow")


@MapLibreRenderer
def my_map():
    m = Map(
        MapOptions(style=OpenFreeMap.LIBERTY, zoom=2, hash=True),
        controls=[NavigationControl(), GlobeControl()],
        layers=[earthquakes],
    )
    m.set_projection("globe")
    return m
