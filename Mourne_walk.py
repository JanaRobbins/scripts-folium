import folium

#folium map with a centre of your map (Mourne Mountain - close to Slieve Donard in this example), the name is map, more descriptive than only common m
#the latitude is first the longitude is the second
# zoom has to be tried to suit the required view, bigger number means more detailed map, decimal number can be used, zoom control add - and + to the map,
# default tiles are OpenStreetMap, but you can use Stamen Terrain, Stamen Toner, Stamen Watercolor, cartodbpositron, cartodbdark_matter, Mapbox Bright (needs api key), Mapbox Control Room (needs api key), Cloudmade (api key needed)
#control_scale shows the scale on the map,

map = folium.Map(location=[54.184431, -5.941592], control_scale='true', width='100%', left='0%', top='0%', height='100%', position='relative', zoom_start=14, zoom_control=True, tiles="Stamen Terrain")

#adding simple pop up markers - Point of Interest in this map, location lat, long and popup with the required name

folium.Marker (location=[54.174232, -5.873921], popup="START - Bloody Bridge Car Park", icon=folium.Icon(icon="cloud"),).add_to(map)
folium.Marker (location=[54.170992, -5.912109], popup="Crannoge Quarry", icon=folium.Icon(color="green"),).add_to(map)
folium.Marker (location=[54.172241, -5.927770], popup="Bog of Donard", icon=folium.Icon(color="red", icon="info-sigh"),).add_to(map)
folium.Marker (location=[54.182497, -5.945436], popup="The Castles", icon=folium.Icon(icon="cloud"),).add_to(map)
folium.Marker (location=[54.188887, -5.962319], popup="Ben Crom Reservoir View", icon=folium.Icon(icon="cloud"),).add_to(map)
folium.Marker (location=[54.190175, -5.974230], popup="Hares' Gap", icon=folium.Icon(icon="glyphicon glyphicon-camera"),).add_to(map)
# color of the marker is purple, icon_color is color of the symbol inside the marker,
folium.Marker (location=[54.209130, -5.999262], popup="FINISH - Meelmore Lodge", icon=folium.Icon(color="purple", icon_color="black", icon="cloud"),).add_to(map)

#adding PolyLine to the project in this example adding one trail to the map, add the name of the line = tooltip
trail_coordinates = [
    (54.174232, -5.873921),
    (54.170992, -5.912109),
    (54.172241, -5.927770),
    (54.182497, -5.945436),
    (54.188887, -5.962319),
    (54.190175, -5.974230),
    (54.209130, -5.999262),
]
folium.PolyLine(trail_coordinates, tooltip="Bandy Pad charity walk 12 km").add_to(map)

#Latitude/longitude popovers - this can help users to find a location
map.add_child(folium.LatLngPopup())

#this will save your map - you can open this map at any time and see the changes
map.save("walk.html")



