# imported Python libraries
import folium
from folium import plugins
from folium.features import DivIcon
import pandas as pd
import geopandas as gpd
import branca


#folium map with a centre of your map (Mourne Mountain - close to Slieve Donard in this example), the name is map, more descriptive than only common m
#the latitude is first the longitude is the second
# zoom has to be tried to suit the required view, bigger number means more detailed map, decimal number can be used, zoom control add - and + to the map,
# default tiles are OpenStreetMap, but you can use Stamen Terrain, Stamen Toner, Stamen Watercolor, cartodbpositron, cartodbdark_matter, Mapbox Bright (needs api key), Mapbox Control Room (needs api key), Cloudmade (api key needed)
#control_scale shows the scale on the map,

map = folium.Map(location=[54.184431, -5.941592], control_scale='true', width='100%', left='0%', top='0%', height='100%',
                 zoom_start=14, zoom_control=True, tiles='Open Street Map', name='Open Street Map')

# add different types of the tiles as a base map

folium.raster_layers.TileLayer('Stamen Terrain', name='Stamen Terrain').add_to(map)
folium.raster_layers.TileLayer('Stamen Toner', name='Stamen Toner').add_to(map)
folium.raster_layers.TileLayer('Stamen Watercolor', name='Stamen Watercolor').add_to(map)
#TODO:add another layers with API key, Google, Bing, Tunderforest

df = pd.read_csv("./data_files/peaks.csv")

# Create point geometries
geometry = gpd.points_from_xy(df.Longitude, df.Latitude)
geo_df = gpd.GeoDataFrame(
    df[["Name", "Height", "Irish_Grid","Latitude", "Longitude", "Type"]], geometry=geometry
)

# Create a geometry list from the GeoDataFrame
geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in geo_df.geometry]

# Iterate through list and add a marker for each volcano, color-coded by its type.
i = 0
for coordinates in geo_df_list:
    # assign a color marker for the type of volcano, Strato being the most common
    if geo_df.Type[i] == "580m-630m":
        type_color = "pink"
    elif geo_df.Type[i] == "631m-700m":
        type_color = "orange"
    elif geo_df.Type[i] == "701m-750m":
        type_color = "purple"
    elif geo_df.Type[i] == "751m-850m":
        type_color = "lightgray"
    else:
        type_color = "blue"

    # Place the markers with the popup labels and data
    map.add_child(
        folium.Marker(
            location=coordinates,
            popup="Name: "
            + str(geo_df.Name[i])
            + "<br>"
            + "<br>"
            + "Height: "
            + str(geo_df.Height[i])
            + "<br>"
            + "<br>"
            + "Irish Grid:"
            + str(geo_df.Irish_Grid[i])
            + "<br>"
            + "<br>"
            + "Coordinates: "
            + str(geo_df_list[i]),
            icon=folium.Icon(color="%s" % type_color),
        )
    )
    i = i + 1

plugins.FloatImage('./images/legend_peaks.png', bottom=70,left=91, width='200px').add_to(map)

#adding text to the map - absolute position in the map
folium.map.Marker([54.2174, -5.8474],icon=DivIcon(icon_size=(250,50),icon_anchor=(0,0),
html='<div style="font-size: 25pt">12 km charity walk</div>',)).add_to(map)


#POINTS OF INTEREST ON THE WAY - Brandy Pad - NO 1 - 7 (Bloody Bridge Car Park to Meelmore Lodge)

#No.1 -adding custom pop up markers - Parking in this map, location lat, long and popup with the required name, pictures added, html styles apply
html1="""
    <h2><strong>START OF THE WALK<strong></h2><br><h3>Bloody Bridge Car Park</h3>"
    <p>
    <img src="images/BloodyBridge.jpg" alt="Bloody Bridge car park">
    </p>
    """
iconstart = folium.features.CustomIcon('./images/Start.png', icon_size=(100,60))
folium.Marker (location=[54.174232, -5.873921], tooltip="<h4>Clik here to see start of the walk</h4>", popup=html1,
               icon=iconstart).add_to(map)

#htmls=pd.read.csv
#pd.read.csv=("./data_files/popup26.csv").apply(popup=row["text"])
#neco jako <br/> aby to bylo na druhem radku a row[“image”] a  alt=row[“alt”]
#TODO: cycling the popup

#No.2 - 6 Popup - HTML style for the description (h3 style apply) and a picture of the area

html2="""
    <h3>Walk up to Crannoge Quarry</h3><br/>
    <p>
    <img src="images/quarry.jpg" alt="Crannoge Quarry">
    </p>
    """

html3="""
    <h3>Climb over Mourne Wall at Bog of Slieve Donard</h3><br/><h4>The hardest part done</h4><br/>
    <p>
    <img src="images/BogOfDonard.jpg" alt="Bog of Donard">
    </p>
    """

html4="""
    <h3>Walk under the Castles</h3><br/><h4>You can walk using Brandy Pad - smugglers crossing way over the mountain</h4><br/>
    <p>
    <img src="images/Castles.jpg" alt="The Castles">
    </p>
    """

html5="""
    <h3>Enjoy Ben Crom Reservoir view</h3><br/><h4>Enjoy the final part before walking down the hill</h4><br/>
    <p>
    <img src="images/BenCrom.jpg" alt="Ben Crom reservoir view">
    </p>
    """

html6="""
    <h3>Reaching Hares Gap walk down the hill</h3><br/><h4>Cross over the Mourne Wall for the second time</h4><br/>
    <p>
    <img src="images/HaresGap.jpg" alt="Hares Gap">
    </p>
    """

# Cycling through all the points of interest

x_coordinates = [54.170992, 54.172241, 54.182497, 54.188887, 54.190175]
y_coordinates = [-5.912109, -5.927770, -5.945436, -5.962319, -5.974230]
htmls = [html2, html3, html4, html5, html6]

for myMarker in range(len(x_coordinates)):
    folium.Marker(location=[x_coordinates[myMarker], y_coordinates[myMarker]],
                  tooltip="<h4>Clik here to see the surrounding area</h4>",
                  popup=htmls[myMarker], icon=folium.features.CustomIcon('./images/icon_green.png', icon_size=(30,50))).add_to(map)

# color of the marker is red, icon_color is color of the symbol inside the marker - black, glyphicon is set to cutlery
# adding url to this marker popup, this will open Meelmore Lodge in a new web window, picture added
# FINISH is in the size h2 and bold (=strong)

html7="""
    <a href=http://www.meelmorelodge.co.uk/ target=_blank</a><br/>
    <h2><strong>FINISH</strong></h2><br><h3>Meelmore Lodge Hostel, campsite and parking</h3>
    <p>
    <img src="images/MeelmoreLodge.jpg" alt="Meelmore Lodge">
    </p>
    """

iconfinish = folium.features.CustomIcon('./images/Finish.png', icon_size=(100,60))
folium.Marker(location=[54.209130, -5.999262], tooltip="<h4>Clik here to see end of the walk</h4>", popup=html7, icon=iconfinish).add_to(map)

# importing csv file (cracks_heading from data_files folder), using latitude and longitude as location (=column in csv file),
# popup is a column crack_name = climbing location in the Mournes, icon set to red
# set markers to custom png pictures

#icon_climb=folium.features.CustomIcon('./images/0-250.png', icon_size=(50,50)
#def image:
    #if crack_elevation_m in range(0,250):
      #  return "./images/0-250.png"
   # elif crack_elevation_m  in range(251,400):
       # return "./images/251-400.png"
  #  elif crack_elevation_m  in range(401,550):
    #    return "./images/401-550.png"
  #  else:
   #     return "./images/551-800.png"
  #  return "./images/0-250.png"


#for MyImg in range(0,len(df)):
	#    df=df['crack_elevation_m'].iloc[i]
	#    if  crack_elevation_m in range(0,250):
	 #       image ='./images/0-250.png'
     #   if crack_elevation_m in range(251, 400):
     #       image = './images/251-400.png'
	 #   elif crack_elevation_m in range(401,550):
	  #      image ='./images/401-550.png'
	 #   else:
	    #     image ='./images/551-800.png'

df=pd.read_csv("./data_files/cracks_heading.csv").apply(lambda row:folium.Marker(location=[row["latitude"], row["longitude"]],
popup="<h3>" + row['crack_name'] + "</h3>" + '' +"<h4>" + row['crack_faces'] + "</h4>" +"<h4>" + "orientation" + "</h4>", tooltip="<h4>Clik here to see the climbing area</h4>", icon=folium.features.CustomIcon('./images/cracks.png', icon_size=(50,50))).add_to(map), axis=1)


pd.read_csv("./data_files/parking_all.csv").apply(lambda row:folium.Marker(location=[row["latitude"], row["longitude"]],
popup="<h3>" + row["parking_name"] + "</h3>", tooltip="<h4>Clik here to see parking name</h4>", icon=folium.features.CustomIcon('./images/parking.png', icon_size=(50,50))).add_to(map), axis=1)


# adding geojson layer to the map - file is in data_files/xy.geosjson folder. Location is a name of one column from the geojson file
# Mourne Wall geojson polygon added, style1 applied, tooltip H3 added, style set to yellow with the filling color transparent =none,

Mourne_wall = f"data_files/wall.geojson"
style1={'fillColor':'none','color':'yellow', 'weight':'6', 'fillOpacity':'0.8'}
folium.GeoJson(Mourne_wall, name="Mourne Wall", style_function=lambda x:style1,  tooltip="<h3>Mourne Wall</h3>").add_to(map)

# Mourne paths geojson Linestring added, style1 applied, tooltip H3 added, style set to pink

Mourne_paths = f"data_files/paths_all.geojson"
style2={'fillColor':'none','color':'purple', 'weight':'1.2', 'fillOpacity':'0.8'}
folium.GeoJson(Mourne_paths, name="walking path", style_function=lambda x:style2,  tooltip="<h3>Walking path</h3>").add_to(map)

# adding PolyLine to the project in this example adding one trail to the map, add the name of the line = tooltip
# color=purple (color for the line), opacity of the line is 1 and weight is 5
trail_coordinates = [
    (54.174232, -5.873921),
    (54.170992, -5.912109),
    (54.172241, -5.927770),
    (54.182497, -5.945436),
    (54.188887, -5.962319),
    (54.190175, -5.974230),
    (54.209130, -5.999262),
]
folium.PolyLine(trail_coordinates, color='green', weight='5', opacity=1, tooltip="<h3>Bandy Pad charity walk 12 km</h3>").add_to(map)

# Latitude/longitude popovers -  this can help users to find a geolocation on the map
my_popup = folium.LatLngPopup()
map.add_child(my_popup)

# remove the next # if you want to see the line for the walk animated
# plugins.AntPath(trail_coordinates).add_to(map)

# Add a field that shows the coordinates of the mouse position on the top right
fmtr = "function(num) {return L.Util.formatNum(num, 4) + ' º ';};"
plugins.MousePosition(position="topright", separator="  //  ", num_digits=5, prefix="<h3>"+"Coordinates:"+"</h3>", lat_formatter=fmtr, lng_formatter=fmtr).add_to(map)

# measure control added - check your position during walk and how long do you have to walk to reach another destination
folium.plugins.MeasureControl(position='topleft', active_color='red', completed_color='red').add_to(map)

# control plugin to geolocate the user
plugins.LocateControl().add_to(map)

# adding a floating image in HTML canvas on buttom left of the map with **kwargs - additional keyword argument as CSS properties
plugins.FloatImage('./images/j.png', bottom=6,left=1, width='60px').add_to(map)

# full screen button in the map
plugins.Fullscreen(force_separate_button=True, title='Click here to see Full Screen').add_to(map)

# adding Mini Map to the map - right bottom corner
plugins.MiniMap(width='300',height='300').add_to(map)

# a search box was added
folium.plugins.Geocoder().add_to(map)

# add layer control to show different maps
folium.LayerControl().add_to(map)

# this will save your map - you can open this map from the finder at any time and see the changes
map.save("walk.html")
