from maplibre import Layer, LayerType, Map, MapLibreRenderer, MapOptions
from maplibre.basemaps import background, construct_basemap_style
from maplibre.controls import GlobeControl, NavigationControl
from maplibre.sources import RasterTileSource
from shiny import reactive
from shiny.express import input, render, ui

layer_id = "osm"

raster_tiles = RasterTileSource(
    tiles=["https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"],
    tile_size=256,
    attribution="&copy; OpenStreetMap Contributors",
    max_zoom=19,
)
style = construct_basemap_style(
    sources={"osm": raster_tiles},
    layers=[Layer(id=layer_id, type=LayerType.RASTER, source="osm")],
)


@MapLibreRenderer
def my_map():
    m = Map(
        MapOptions(style=style, zoom=2, hash=True),
        controls=[NavigationControl(), GlobeControl()],
    )
    return m
