# imported Python libraries
import folium
from folium import plugins
from folium.features import DivIcon
import pandas as pd
import geopandas as gpd


# 1. SECTION THAT CAN BE CHANGED IN THIS MAP

# Folium map with a centre of the map in Mourne Mountains, which is close to Slieve Donard in this example = location, the name set to 'map' (could be any name).
# Control scale and zoom_control added to the map here – set to True.
# Start zoom has to be tried to suit the required view, bigger number means more detailed map (14 in this example).


map = folium.Map(location=[54.184431, -5.941592], control_scale='true', width='100%', left='0%', top='0%', height='100%',
                 zoom_start=13.6, zoom_control=True, tiles='Open Street Map', name='Open Street Map')

# Default tiles are OpenStreetMap, but you can use Stamen Terrain, Stamen Toner, Stamen Watercolor, cartodbpositron, cartodbdark_matter without any restriction.
# With API key - Mapbox Bright, Mapbox Control Room, Cloudmade, Bing, Google and Thunderforest can be added.

folium.raster_layers.TileLayer('Stamen Terrain', name='Stamen Terrain').add_to(map)
folium.raster_layers.TileLayer('Stamen Toner', name='Stamen Toner').add_to(map)
folium.raster_layers.TileLayer('Stamen Watercolor', name='Stamen Watercolor').add_to(map)
#TODO:add another layers with API key, Google, Bing, Tunderforest

# CSV file for the highest peaks in the area added using panda. Change the file to get your own data.
df = pd.read_csv("./data_files/peaks.csv")

# Created points geometries using GeoPandas.

geometry = gpd.points_from_xy(df.Longitude, df.Latitude)
geo_df = gpd.GeoDataFrame(df[["Name", "Height", "Irish_Grid","Latitude", "Longitude", "Type"]], geometry=geometry)

# Created a geometry list from the GeoDataFrame.
geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in geo_df.geometry]

# Iterate through list and add a marker for each peak, color-coded by its type.
i = 0
for coordinates in geo_df_list:
    # Assign a colour marker for the type of peak, by the column ‘type’, peaks sorted into four categories.
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

    # Place the markers with the popup labels and data.
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

# Adding a legend for the peaks markers as a floating picture to the top right (number 70 and 91 are percentages from the bottom left).
plugins.FloatImage('./images/legend_peaks.png', bottom='55',left='91', width='200px').add_to(map)

# Adding a legend for the lines, polygons and GeoJson files
plugins.FloatImage('./images/legend_map.png', bottom='31',left='91', width='200px').add_to(map)

# Adding text to the map - absolute position in the map – DivIcon used.

folium.map.Marker([54.2174, -5.8474],icon=DivIcon(icon_size=(250,50),icon_anchor=(0,0),
html='<div style="font-size: 25pt">12 km charity walk</div>')).add_to(map)


#POINTS OF INTEREST ON THE WAY - Brandy Pad - NO 1 - 7 (Bloody Bridge Car Park to Meelmore Lodge)

#No.1 -adding custom pop up markers - Parking in this map, location lat, long and popup with the required name, pictures added, html styles apply.

html1="""
    <h2><strong>START OF THE WALK<strong></h2><br><h3>Bloody Bridge Car Park</h3>"
    <p>
    <img src="images/BloodyBridge.jpg" alt="Bloody Bridge car park">
    </p>
    """
iconstart = folium.features.CustomIcon('./images/Start.png', icon_size=(100,60))
folium.Marker (location=[54.174232, -5.873921], tooltip="<h4>Click here to see start of the walk</h4>", popup=html1,
               icon=iconstart).add_to(map)

# Point of interest No.2 – No.6 - HTML style for the description and a picture of the area. read from the file popup26.csv

marker_df=pd.read_csv('./data_files/popup26.csv')
for i in range(len(marker_df)):
    latitude=marker_df.loc[i]["latitude"]
    longitude=marker_df.loc[i]["longitude"]
    title=marker_df.loc[i]["title"]
    text=marker_df.loc[i]["text"]
    img_src=marker_df.loc[i]["img_src"]
    alt=marker_df.loc[i]["alt"]

    html="<h3>" + title + "</h3><br/><h4>" + text + "</h4><br/><p><img src=" + "'"+ img_src + "'" + "alt=" + alt +"></p>"
    folium.Marker(location=[latitude,longitude], tooltip="<h4>Click here to see the surrounding area</h4>", popup=html, icon=folium.features.CustomIcon('./images/icon_green.png', icon_size=(30,50))).add_to(map)

# Adding url to this marker popup, this will open Meelmore Lodge in a new web window, picture added.

html7="""
    <a href=http://www.meelmorelodge.co.uk/ target=_blank</a><br/>
    <h2><strong>FINISH</strong></h2><br><h3>Meelmore Lodge Hostel, campsite and parking</h3>
    <p>
    <img src="images/MeelmoreLodge.jpg" alt="Meelmore Lodge">
    </p>
    """

# Text FINISH in the html size h2 and bold (=strong) and image added into the popup. Png custom pictures used for an icon.

iconfinish = folium.features.CustomIcon('./images/Finish.png', icon_size=(100,60))
folium.Marker(location=[54.209130, -5.999262], tooltip="<h4>Clik here to see end of the walk</h4>", popup=html7, icon=iconfinish).add_to(map)

# Importing csv file (cracks_heading from data_files folder), using latitude and longitude as location (=column in csv file)
# in popups a column crack_name = climbing location in the Mournes and crack face used, custom icon used – png picture of mountain.

df=pd.read_csv("./data_files/cracks_heading.csv").apply(lambda row:folium.Marker(location=[row["latitude"], row["longitude"]],
popup="<h3>" + row['crack_name'] + "</h3>" + '' +"<h4>" + row['crack_faces'] + "</h4>" +"<h4>" + "orientation" + "</h4>", tooltip="<h4>Click here to see the climbing area</h4>",
                                                                                 icon=folium.features.CustomIcon('./images/cracks.png', icon_size=(50,50))).add_to(map), axis=1)

# Importing csv file (parking_all from data_files folder), custom icon used – png picture of parkings. A small anonymous function lambda is used here again.

pd.read_csv("./data_files/parking_all.csv").apply(lambda row:folium.Marker(location=[row["latitude"], row["longitude"]],
popup="<h3>" + row["parking_name"] + "</h3>", tooltip="<h4>Click here to see parking name</h4>",
                                                                           icon=folium.features.CustomIcon('./images/parking.png', icon_size=(50,50))).add_to(map), axis=1)

# Mourne Wall GeoJson polygon added from the folder data_files, style of the line set to yellow with the filling colour transparent = none.

Mourne_wall = f"data_files/wall.geojson"
style1={'fillColor':'none','color':'yellow', 'weight':'6', 'fillOpacity':'0.8'}
folium.GeoJson(Mourne_wall, name="Mourne Wall", style_function=lambda x:style1,  tooltip="<h3>Mourne Wall</h3>").add_to(map)

# Mourne paths GeoJson LineString added, style1 applied, style of the paths set to pink.

Mourne_paths = f"data_files/paths_all.geojson"
style2={'fillColor':'none','color':'purple', 'weight':'1.2', 'fillOpacity':'0.8'}
folium.GeoJson(Mourne_paths, name="walking path", style_function=lambda x:style2,  tooltip="<h3>Walking path</h3>").add_to(map)

# Adding PolyLine to the project in this example adding a waking trail to the map, add the name of the line while moving mouse over it = tooltip,
# colour set for green (colour for the line). Coordinates could be changed for any different.
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

# 2. SECTION YOU DO NOT NEED TO CHANGE IN THE MAP

# Latitude/longitude popovers - this can help users to find a geolocation on the map by clicking anywhere in the map.

my_popup = folium.LatLngPopup()
map.add_child(my_popup)

# Remove the next # if you want to see the line for the walk animated.
# plugins.AntPath(trail_coordinates).add_to(map)

# Add a field that shows the coordinates of the mouse position on the top right.
fmtr = "function(num) {return L.Util.formatNum(num, 4) + ' º ';};"
plugins.MousePosition(position="topright", separator="  //  ", num_digits=5, prefix="<h3>"+"Coordinates:"+"</h3>", lat_formatter=fmtr, lng_formatter=fmtr).add_to(map)

# Measure control added - check your position during walk and how long do you have to walk to reach another destination.
folium.plugins.MeasureControl(position='topleft', active_color='red', completed_color='red').add_to(map)

# Control plugin to locate the user - check your position during the walk!!!
plugins.LocateControl().add_to(map)

# Adding a floating image in HTML canvas on bottom left of the map with **kwargs - additional keyword argument as CSS properties – your logo can be here.
plugins.FloatImage('./images/j.png', bottom=6,left=1, width='60px').add_to(map)

# Full screen button in the map.
plugins.Fullscreen(force_separate_button=True, title='Click here to see Full Screen').add_to(map)

# Adding Mini Map to the map - bottom right corner.
plugins.MiniMap(width='300',height='300').add_to(map)

# A search box was added.
folium.plugins.Geocoder().add_to(map)

# Add layer control to show different maps.
folium.LayerControl().add_to(map)

# This will save your map - you can open this map from the finder at any time and see the changes.
map.save("walk.html")
