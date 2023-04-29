import folium
from folium import plugins
from folium.features import DivIcon
import pandas as pd
import branca

#folium map with a centre of your map (Mourne Mountain - close to Slieve Donard in this example), the name is map, more descriptive than only common m
#the latitude is first the longitude is the second
# zoom has to be tried to suit the required view, bigger number means more detailed map, decimal number can be used, zoom control add - and + to the map,
# default tiles are OpenStreetMap, but you can use Stamen Terrain, Stamen Toner, Stamen Watercolor, cartodbpositron, cartodbdark_matter, Mapbox Bright (needs api key), Mapbox Control Room (needs api key), Cloudmade (api key needed)
#control_scale shows the scale on the map,

map = folium.Map(location=[54.184431, -5.941592], control_scale='true', width='100%', left='0%', top='0%', height='100%',
                 zoom_start=14, zoom_control=True, tiles='Stamen Terrain', name='Stamen Terrain')


#adding text to the map - absolute position in the map
folium.map.Marker(
[54.2174, -5.8474],
icon=DivIcon(
icon_size=(250,50),
icon_anchor=(0,0),
html='<div style="font-size: 25pt">12 km charity walk</div>',
)
).add_to(map)

#adding Mini Map to the map - right bottom corner
plugins.MiniMap().add_to(map)

#POINTS OF INTEREST ON THE WAY - Brandy Pad - NO 1 - 7 (Bloody Bridge Car Park to Meelmore Lodge)

#No.1 -adding custom pop up markers - Parking in this map, location lat, long and popup with the required name, pictures added, html styles apply
html1="""
    <h2><strong>START OF THE WALK<strong></h2><br><h3>Bloody Bridge Car Park</h3>"
    <p>
    <img src="images/BloodyBridge.jpg" alt="Bloody Bridge car park" class="img2">
    </p>
    """
iconparking = folium.features.CustomIcon('./images/parking.png', icon_size=(50,50))
folium.Marker (location=[54.174232, -5.873921], tooltip="<h4>Clik here to see start of the walk</h4>", popup=html1,
               icon=iconparking).add_to(map)

#No.2 - adding green pop up marker with a camera icon inside - Point of Interest in this map, location lat, long and popup with html style - name and picture added,
# tooltip added with h4 size of the text
html2="""
    <h3>Walk up to Crannoge Quarry</h3><br/>
    <p>
    <img src="images/quarry.jpg" alt="Crannoge Quarry" class="img2">
    </p>
    """
folium.Marker (location=[54.170992, -5.912109], tooltip="<h4>Clik here to see what you can see walking up the hill</h4>", popup=html2, icon=folium.Icon(color="red", icon="camera"),).add_to(map)

#No.3 - adding simple pop up markers - Point of Interest in this map, location lat, long and popup with the required name and picture,
# tooltip added with h4 size of the text
html3="""
    <h3>Climb over Mourne Wall at Bog of Slieve Donard</h3><br/><h4>The hardest part done</h4><br/>
    <p>
    <img src="images/BogOfDonard.jpg" alt="Bog of Donard" class="img2">
    </p>
    """
folium.Marker (location=[54.172241, -5.927770], tooltip="<h4>Clik here to see first crossing over the Mourne Wall</h4>", popup=html3, icon=folium.Icon(color="red", icon="camera"),).add_to(map)

#No.4 - Point of Interest - next marker on the way - html style apply
html4="""
    <h3>Walk under the Castles</h3><br/><h4>You can walk using Brandy Pad - smugglers crossing way over the moutanin</h4><br/>
    <p>
    <img src="images/Castles.jpg" alt="The Castles" class="img2">
    </p>
    """
folium.Marker (location=[54.182497, -5.945436], tooltip="<h4>Clik here to see what is close to this point</h4>", popup=html4, icon=folium.Icon(color='red', icon="camera"),).add_to(map)

#No.5 - Point of Interest - next marker on the way - html style apply
html5="""
    <h3>Enjoy Ben Crom Reservoir view</h3><br/><h4>Enjoy the final part before walking down the hill</h4><br/>
    <p>
    <img src="images/BenCrom.jpg" alt="Ben Crom reservoir view" class="img2">
    </p>
    """
folium.Marker (location=[54.188887, -5.962319], tooltip="<h4>Clik here to see what is in near distance</h4>", popup=html5, icon=folium.Icon(color='red', icon="camera"),).add_to(map)

#No.6- Point of Interest - next marker on the way - html style apply
html6="""
    <h3>Reaching Hares Gap walk down the hill</h3><br/><h4>Cross over the Mourne Wall for the second time</h4><br/>
    <p>
    <img src="images/HaresGap.jpg" alt="Hares Gap" class="img2">
    </p>
    """
folium.Marker (location=[54.190175, -5.974230], tooltip="<h4>Clik here to see second crossing over the Mourne Wall</h4>", popup=html6, icon=folium.Icon(color='red', icon="glyphicon glyphicon-camera"),).add_to(map)

# color of the marker is red, icon_color is color of the symbol inside the marker - black, glyphicon is set to cutlery
# adding url to this marker popup, this will open Meelmore Lodge in a new web window, picture added
# FINISH is in the size h2 and bold (=strong)

html7="""
    <a href=http://www.meelmorelodge.co.uk/ target=_blank</a><br/>
    <h2><strong>FINISH</strong></h2><br><h3>Meelmore Lodge</h3>
    <p>
    <img src="images/MeelmoreLodge.jpg" alt="Meelmore Lodge" class="img2">
    </p>
    """
folium.Marker (location=[54.209130, -5.999262],tooltip="<h4>Clik here to see end of the walk</h4>", popup=html7,
               icon=folium.Icon(color="red", icon_color="black", icon="glyphicon glyphicon-cutlery"),).add_to(map)

#TODO:add navigator to the map...
#navigator.geolocation.watchPosition(showPosition)

#importing csv file (cracks_heading from data_files folder), using latitude and longitude as location (=column in csv file),
#popup is a column crack_name = climbing location in the Mournes, icon set to red

pd.read_csv("./data_files/cracks_heading.csv").apply(lambda row:folium.Marker(location=[row["latitude"], row["longitude"]],
popup=row["crack_name"], tooltip="<h4>Clik here to see name of the climbing area</h4>", icon=folium.features.CustomIcon('./images/Mountains-icon.png', icon_size=(50,50))).add_to(map), axis=1)
#TODO:change size for the crack_name

pd.read_csv("./data_files/parking_all.csv").apply(lambda row:folium.Marker(location=[row["latitude"], row["longitude"]],
popup=row["parking_name"], tooltip="<h4>Clik here to see parking name</h4>", icon=folium.features.CustomIcon('./images/parking.png', icon_size=(50,50))).add_to(map), axis=1)
#TODO:change size for the crack_name

#adding geojson layer to the map - file is in data_files/xy.geosjson folder. Location is a name of one column from the geojson file
#Mourne Wall geojson polygon added, style1 applied, tooltip H3 added, style set to yellow with the filling color transparent =none,

Mourne_wall = f"data_files/wall.geojson"
style1={'fillColor':'none','color':'yellow', 'weight':'6', 'fillOpacity':'0.8'}
folium.GeoJson(Mourne_wall, name="Mourne Wall", style_function=lambda x:style1,  tooltip="<h3>Mourne Wall</h3>").add_to(map)

#Mourne paths geojson Linestring added, style1 applied, tooltip H3 added, style set to pink

Mourne_paths = f"data_files/paths_all.geojson"
style2={'fillColor':'none','color':'pink', 'weight':'4', 'fillOpacity':'0.9'}
folium.GeoJson(Mourne_paths, name="walking path", style_function=lambda x:style2,  tooltip="<h3>Walking path</h3>").add_to(map)

#adding PolyLine to the project in this example adding one trail to the map, add the name of the line = tooltip
#color=purple (color for the line), opacity of the line is 1 and weight is 5

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

#Latitude/longitude popovers -  this can help users to find a location of the place

map.add_child(folium.LatLngPopup())

# remove the next # if you want to see the line for the walk animated
#plugins.AntPath(trail_coordinates).add_to(map)


# add different types of the tiles as a base map

folium.raster_layers.TileLayer('Open Street Map', name='Open Street Map').add_to(map)
folium.raster_layers.TileLayer('Stamen Toner', name='Stamen Toner').add_to(map)
folium.raster_layers.TileLayer('Stamen Watercolor', name='Stamen Watercolor').add_to(map)
#TODO:add another layers with API key, Google, Bing, Tunderforest

# add layer control to show different maps

folium.LayerControl().add_to(map)

#this will save your map - you can open this map at any time and see the changes

map.save("walk.html")



