import folium
from folium import plugins
import geopandas as gpd

#folium map with a centre of your map (Mourne Mountain - close to Slieve Donard in this example), the name is map, more descriptive than only common m
#the latitude is first the longitude is the second
# zoom has to be tried to suit the required view, bigger number means more detailed map, decimal number can be used, zoom control add - and + to the map,
# default tiles are OpenStreetMap, but you can use Stamen Terrain, Stamen Toner, Stamen Watercolor, cartodbpositron, cartodbdark_matter, Mapbox Bright (needs api key), Mapbox Control Room (needs api key), Cloudmade (api key needed)
#control_scale shows the scale on the map,

map = folium.Map(location=[54.184431, -5.941592], control_scale='true', width='100%', left='0%', top='0%', height='100%',
                 zoom_start=14, zoom_control=True, tiles='Stamen Terrain', name='Stamen Terrain')

#adding Mini Map to the map - right bottom corner

plugins.MiniMap().add_to(map)

#adding custom pop up markers - Parking in this map, location lat, long and popup with the required name, html styles apply

iconparking = folium.features.CustomIcon('./images/parking.png', icon_size=(50,50))
folium.Marker (location=[54.174232, -5.873921], popup="<h2><strong>START<strong></h2><br><h4>Bloody Bridge Car Park</h4>",
               icon=iconparking).add_to(map)

#adding simple pop up markers - Point of Interest in this map, location lat, long and popup with the required name

folium.Marker (location=[54.170992, -5.912109], popup="<h4>Crannoge Quarry</h4>", icon=folium.Icon(color="green", icon="camera"),).add_to(map)
folium.Marker (location=[54.172241, -5.927770], popup="<h4>Bog of Donard</h4>", icon=folium.Icon(color="green", icon="camera"),).add_to(map)
folium.Marker (location=[54.182497, -5.945436], popup="<h4>The Castles</h4>", icon=folium.Icon(color='green', icon="camera"),).add_to(map)
folium.Marker (location=[54.188887, -5.962319], popup="<h4>Ben Crom Reservoir View</h4>", icon=folium.Icon(color='green', icon="camera"),).add_to(map)
folium.Marker (location=[54.190175, -5.974230], popup="<h4>Hares' Gap</h4>", icon=folium.Icon(color='green', icon="glyphicon glyphicon-camera"),).add_to(map)

# color of the marker is purple, icon_color is color of the symbol inside the marker,

folium.Marker (location=[54.209130, -5.999262], popup="<a href=http://www.meelmorelodge.co.uk/ target=_blank</a>""<h2><strong>FINISH</strong></h2><br><h4>Meelmore Lodge</h4>",
               icon=folium.Icon(color="red", icon_color="black", icon="glyphicon glyphicon-cutlery"),).add_to(map)


#adding geojson layer to the map - file is in data_files/xy.geosjson folder. Location is a name of one column from the geojson file
#Mourne Wall geojson polygon added, style1 applied, tooltip H3 added, style set to yellow with the filling color transprent =none,

Mourne_wall = f"data_files/wall.geojson"
style1={'fillColor':'none','color':'yellow', 'weight':'6', 'fillOpacity':'0.8'}
folium.GeoJson(Mourne_wall, name="Mourne Wall", style_function=lambda x:style1,  tooltip="<h3>Mourne Wall</h3>").add_to(map)

#Mourne paths geojson Linestring added, style1 applied, tooltip H3 added, style set to pink

Mourne_paths = f"data_files/paths_all.geojson"
style2={'fillColor':'none','color':'pink', 'weight':'4', 'fillOpacity':'0.9'}
folium.GeoJson(Mourne_paths, name="walking path", style_function=lambda x:style2,  tooltip="<h3>Walking path</h3>").add_to(map)



#adding PolyLine to the project in this example adding one trail to the map, add the name of the line = tooltip
# color=purple (color for the line), opacity of the line is 3

trail_coordinates = [
    (54.174232, -5.873921),
    (54.170992, -5.912109),
    (54.172241, -5.927770),
    (54.182497, -5.945436),
    (54.188887, -5.962319),
    (54.190175, -5.974230),
    (54.209130, -5.999262),
]
folium.PolyLine(trail_coordinates, color='purple', weight='5', opacity=1, tooltip="<h3>Bandy Pad charity walk 12 km</h3>").add_to(map)

#Latitude/longitude popovers -  this can help users to find a location

map.add_child(folium.LatLngPopup())

# remove the next # if you want to see the line for the walk animated
#plugins.AntPath(trail_coordinates).add_to(map)

# add different types of the tiles as a base map

folium.raster_layers.TileLayer('Open Street Map', name='Open Street Map').add_to(map)
folium.raster_layers.TileLayer('Stamen Toner', name='Stamen Toner').add_to(map)
folium.raster_layers.TileLayer('Stamen Watercolor', name='Stamen Watercolor').add_to(map)



# add layer control to show different maps

folium.LayerControl().add_to(map)


#this will save your map - you can open this map at any time and see the changes

map.save("walk.html")



