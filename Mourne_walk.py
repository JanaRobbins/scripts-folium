# import Python libraries
import folium
from folium import plugins
from folium.features import DivIcon
import pandas as pd
import geopandas as gpd


# FUNCTIONS USED IN THIS SCRIPT
# These functions make the code shorter, easier to read and easier to change.
# Instead of repeating the same marker, popup or GeoJSON code many times,
# the function is written once and then reused later in the script.

def create_popup_html(title, text="", image_path=None, alt_text="", image_width="500px"):
    """
    Create HTML content for a Folium popup.

    This function is used for popups that contain a title, description
    and optional image. The image width can be changed to make popup
    photos larger or smaller.

    Parameters:
    title (str): title displayed in the popup.
    text (str): description displayed below the title.
    image_path (str): path to the image displayed in the popup.
    alt_text (str): alternative text for the image.
    image_width (str): width of the image in the popup.

    Returns:
    str: HTML formatted popup content.
    """

    image_html = ""

    if image_path:
        image_html = f"""
        <p>
            <img src="{image_path}"
                 style="width:{image_width}; max-width:100%;"
                 alt="{alt_text}">
        </p>
        """

    html = f"""
    <h3>{title}</h3>
    <h4>{text}</h4>
    {image_html}
    """

    return html


def add_custom_marker(map_object, location, tooltip, popup_html,
                      icon_path, icon_size=(50, 50), popup_width=600):
    """
    Add a custom marker with popup and icon to the Folium map.

    This function is used for start, finish and walk point markers.
    It also allows the popup window to be larger, which is useful
    when photos are displayed in the popup.

    Parameters:
    map_object: Folium map object.
    location (list): latitude and longitude coordinates.
    tooltip (str): text displayed when hovering over the marker.
    popup_html (str): HTML content displayed when marker is clicked.
    icon_path (str): path to the custom icon image.
    icon_size (tuple): size of the custom icon.
    popup_width (int): maximum width of the popup window.
    """

    icon = folium.features.CustomIcon(icon_path, icon_size=icon_size)

    folium.Marker(
        location=location,
        tooltip=tooltip,
        popup=folium.Popup(popup_html, max_width=popup_width),
        icon=icon
    ).add_to(map_object)


def get_peak_colour(peak_type):
    """
    Return a marker colour based on the peak height category.

    This function replaces the repeated if/elif code in the marker loop.
    The colour is selected from the Type column in peaks.csv.

    Parameters:
    peak_type (str): peak height category.

    Returns:
    str: Folium marker colour.
    """

    if peak_type == "580m-630m":
        return "pink"
    elif peak_type == "631m-700m":
        return "orange"
    elif peak_type == "701m-750m":
        return "purple"
    elif peak_type == "751m-850m":
        return "lightgray"
    else:
        return "blue"


def add_geojson_layer(map_object, file_path, layer_name, style, tooltip_text):
    """
    Add a GeoJSON layer to the Folium map.

    This function is used for the Mourne Wall and walking paths.
    The style dictionary controls the colour, line weight and opacity.

    Parameters:
    map_object: Folium map object.
    file_path (str): path to the GeoJSON file.
    layer_name (str): name shown in the layer control.
    style (dict): style settings for the GeoJSON layer.
    tooltip_text (str): tooltip displayed when hovering over the layer.
    """

    folium.GeoJson(
        file_path,
        name=layer_name,
        style_function=lambda x: style,
        tooltip=tooltip_text
    ).add_to(map_object)


def add_csv_icon_markers(map_object, csv_path, icon_path, tooltip,
                         name_column, extra_column=None, icon_size=(50, 50)):
    """
    Add markers to the map from a CSV file.

    This function is useful when many points have the same type of marker,
    for example parking locations or climbing locations.

    Parameters:
    map_object: Folium map object.
    csv_path (str): path to the CSV file.
    icon_path (str): path to the custom marker icon.
    tooltip (str): tooltip displayed when hovering over markers.
    name_column (str): CSV column used as popup title.
    extra_column (str): optional extra CSV column displayed in popup.
    icon_size (tuple): size of the custom icon.
    """

    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        popup_html = f"<h3>{row[name_column]}</h3>"

        if extra_column:
            popup_html += f"<h4>{row[extra_column]}</h4>"

        add_custom_marker(
            map_object=map_object,
            location=[row["latitude"], row["longitude"]],
            tooltip=tooltip,
            popup_html=popup_html,
            icon_path=icon_path,
            icon_size=icon_size
        )


# 1. SECTION THAT CAN BE CHANGED IN THIS MAP

# Folium map with the centre of the map in the Mourne Mountains,
# close to Slieve Donard in this example.
# The map object is called walk_map.
# control_scale and zoom_control are added to the map and set to True.
# zoom_start has to be tested to suit the required view.
# A bigger zoom number means a more detailed map.
walk_map = folium.Map(
    location=[54.184431, -5.941592],
    control_scale=True,
    width="100%",
    left="0%",
    top="0%",
    height="100%",
    zoom_start=13.6,
    zoom_control=True,
    tiles="OpenStreetMap",
    name="OpenStreetMap"
)

# Default tiles are OpenStreetMap.
# Other tile layers can be added, for example Stamen Terrain,
# Stamen Toner, Stamen Watercolor, CartoDB Positron and CartoDB Dark Matter.
# Some map providers require an API key, for example Google, Bing,
# Mapbox and Thunderforest.
folium.raster_layers.TileLayer(
    "Stamen Terrain",
    name="Stamen Terrain"
).add_to(walk_map)

folium.raster_layers.TileLayer(
    "Stamen Toner",
    name="Stamen Toner"
).add_to(walk_map)

folium.raster_layers.TileLayer(
    "Stamen Watercolor",
    name="Stamen Watercolor"
).add_to(walk_map)

# TODO: add other layers with an API key, such as Google, Bing or Thunderforest.


# PEAK MARKERS
# CSV file for the highest peaks in the area is added using pandas.
# Change the file to use your own peak data.
peaks_df = pd.read_csv("./data_files/peaks.csv")

# Create point geometries using GeoPandas from Longitude and Latitude columns.
geometry = gpd.points_from_xy(peaks_df.Longitude, peaks_df.Latitude)

geo_df = gpd.GeoDataFrame(
    peaks_df[
        ["Name", "Height", "Irish_Grid", "Latitude", "Longitude", "Type"]
    ],
    geometry=geometry
)

# Create a geometry list from the GeoDataFrame.
geo_df_list = [
    [point.xy[1][0], point.xy[0][0]]
    for point in geo_df.geometry
]

# Iterate through the list and add a marker for each peak.
# Markers are colour-coded by Type column.
for i, coordinates in enumerate(geo_df_list):

    type_color = get_peak_colour(geo_df.Type[i])

    popup_html = f"""
    Name: {geo_df.Name[i]}
    <br><br>
    Height: {geo_df.Height[i]}
    <br><br>
    Irish Grid: {geo_df.Irish_Grid[i]}
    <br><br>
    Coordinates: {geo_df_list[i]}
    """

    folium.Marker(
        location=coordinates,
        popup=folium.Popup(popup_html, max_width=400),
        icon=folium.Icon(color=type_color)
    ).add_to(walk_map)


# Adding a legend for the peak markers as a floating picture.
# The bottom and left values are percentages from the bottom-left corner.
plugins.FloatImage(
    "./images/legend_peaks.png",
    bottom="55",
    left="91",
    width="200px"
).add_to(walk_map)

# Adding a legend for the lines, polygons and GeoJSON files.
plugins.FloatImage(
    "./images/legend_map.png",
    bottom="31",
    left="91",
    width="200px"
).add_to(walk_map)


# Adding text to the map using absolute position.
# DivIcon is used to place a text label directly onto the map.
folium.map.Marker(
    [54.2174, -5.8474],
    icon=DivIcon(
        icon_size=(250, 50),
        icon_anchor=(0, 0),
        html='<div style="font-size: 25pt">12 km charity walk</div>'
    )
).add_to(walk_map)


# POINTS OF INTEREST ON THE WAY
# Brandy Pad walk: Bloody Bridge Car Park to Meelmore Lodge.

# No. 1 - Start point.
# Custom popup marker for the start of the walk.
# The popup contains text and a larger photo.
html_start = create_popup_html(
    title="<strong>START OF THE WALK</strong>",
    text="Bloody Bridge Car Park",
    image_path="images/BloodyBridge.jpg",
    alt_text="Bloody Bridge car park",
    image_width="500px"
)

add_custom_marker(
    map_object=walk_map,
    location=[54.174232, -5.873921],
    tooltip="<h4>Click here to see start of the walk</h4>",
    popup_html=html_start,
    icon_path="./images/Start.png",
    icon_size=(100, 60),
    popup_width=650
)


# Points of interest No. 2 to No. 6.
# The data is read from popup26.csv.
# The CSV file should contain latitude, longitude, title, text,
# img_src and alt columns.
marker_df = pd.read_csv("./data_files/popup26.csv")

for _, row in marker_df.iterrows():

    html = create_popup_html(
        title=row["title"],
        text=row["text"],
        image_path=row["img_src"],
        alt_text=row["alt"],
        image_width="500px"
    )

    add_custom_marker(
        map_object=walk_map,
        location=[row["latitude"], row["longitude"]],
        tooltip="<h4>Click here to see the surrounding area</h4>",
        popup_html=html,
        icon_path="./images/icon_green.png",
        icon_size=(30, 50),
        popup_width=650
    )


# No. 7 - Finish point.
# Adding URL to the marker popup.
# This opens Meelmore Lodge website in a new browser window.
# Text FINISH is displayed in HTML h2 and bold.
# A photo is added into the popup and a PNG custom image is used for the icon.
html_finish = """
<a href="http://www.meelmorelodge.co.uk/" target="_blank">
Visit Meelmore Lodge website
</a>
<br>
<h2><strong>FINISH</strong></h2>
<h3>Meelmore Lodge Hostel, campsite and parking</h3>
<p>
    <img src="images/MeelmoreLodge.jpg"
         style="width:500px; max-width:100%;"
         alt="Meelmore Lodge">
</p>
"""

add_custom_marker(
    map_object=walk_map,
    location=[54.209130, -5.999262],
    tooltip="<h4>Click here to see end of the walk</h4>",
    popup_html=html_finish,
    icon_path="./images/Finish.png",
    icon_size=(100, 60),
    popup_width=650
)


# Importing CSV file cracks_heading.csv from the data_files folder.
# Latitude and longitude are used as marker locations.
# In popups, crack_name is used as the climbing location
# and crack_faces is used as information about the crack face.
# A custom PNG icon of a mountain is used.
cracks_df = pd.read_csv("./data_files/cracks_heading.csv")

for _, row in cracks_df.iterrows():

    popup_html = f"""
    <h3>{row["crack_name"]}</h3>
    <h4>{row["crack_faces"]}</h4>
    <h4>Orientation</h4>
    """

    add_custom_marker(
        map_object=walk_map,
        location=[row["latitude"], row["longitude"]],
        tooltip="<h4>Click here to see the climbing area</h4>",
        popup_html=popup_html,
        icon_path="./images/cracks.png",
        icon_size=(50, 50)
    )


# Importing CSV file parking_all.csv from the data_files folder.
# A custom PNG parking icon is used.
# This section uses the add_csv_icon_markers function to avoid repeating code.
add_csv_icon_markers(
    map_object=walk_map,
    csv_path="./data_files/parking_all.csv",
    icon_path="./images/parking.png",
    tooltip="<h4>Click here to see parking name</h4>",
    name_column="parking_name",
    icon_size=(50, 50)
)


# Mourne Wall GeoJSON polygon/line added from the data_files folder.
# The style of the line is set to yellow.
# The fill colour is set to none.
wall_style = {
    "fillColor": "none",
    "color": "yellow",
    "weight": "6",
    "fillOpacity": "0.8"
}

add_geojson_layer(
    map_object=walk_map,
    file_path="data_files/wall.geojson",
    layer_name="Mourne Wall",
    style=wall_style,
    tooltip_text="<h3>Mourne Wall</h3>"
)


# Mourne paths GeoJSON LineString added from the data_files folder.
# The paths are styled as purple lines.
paths_style = {
    "fillColor": "none",
    "color": "purple",
    "weight": "1.2",
    "fillOpacity": "0.8"
}

add_geojson_layer(
    map_object=walk_map,
    file_path="data_files/paths_all.geojson",
    layer_name="Walking path",
    style=paths_style,
    tooltip_text="<h3>Walking path</h3>"
)


# Adding PolyLine to the project.
# In this example, the PolyLine adds a walking trail to the map.
# The tooltip shows the name of the trail when the mouse moves over it.
# The colour is set to green.
# Coordinates can be changed for any different walking route.
trail_coordinates = [
    (54.174232, -5.873921),
    (54.170992, -5.912109),
    (54.172241, -5.927770),
    (54.182497, -5.945436),
    (54.188887, -5.962319),
    (54.190175, -5.974230),
    (54.209130, -5.999262),
]

folium.PolyLine(
    trail_coordinates,
    color="green",
    weight="5",
    opacity=1,
    tooltip="<h3>Brandy Pad charity walk 12 km</h3>"
).add_to(walk_map)


# 2. SECTION YOU DO NOT NEED TO CHANGE IN THE MAP

# Latitude/longitude popups.
# This helps users find a geolocation by clicking anywhere on the map.
walk_map.add_child(folium.LatLngPopup())


# Remove the next # if you want to see the line for the walk animated.
# plugins.AntPath(trail_coordinates).add_to(walk_map)


# Add a field that shows the coordinates of the mouse position
# on the top right of the map.
fmtr = "function(num) {return L.Util.formatNum(num, 4) + ' º ';};"

plugins.MousePosition(
    position="topright",
    separator="  //  ",
    num_digits=5,
    prefix="<h3>Coordinates:</h3>",
    lat_formatter=fmtr,
    lng_formatter=fmtr
).add_to(walk_map)


# Measure control added.
# This can be used to check distances during the walk
# and estimate how far it is to another destination.
folium.plugins.MeasureControl(
    position="topleft",
    active_color="red",
    completed_color="red"
).add_to(walk_map)


# Control plugin to locate the user.
# This can help users check their position during the walk.
plugins.LocateControl().add_to(walk_map)


# Adding a floating image in the HTML canvas on the bottom left of the map.
# Additional keyword arguments are used as CSS properties.
# A logo or project image can be displayed here.
plugins.FloatImage(
    "./images/j.png",
    bottom=6,
    left=1,
    width="60px"
).add_to(walk_map)


# Full screen button in the map.
plugins.Fullscreen(
    force_separate_button=True,
    title="Click here to see Full Screen"
).add_to(walk_map)


# Adding MiniMap to the map.
# This creates a small overview map in the bottom right corner.
# The size has been changed from 300 x 300 to 150 x 150
# to make the small map less intrusive.
plugins.MiniMap(
    width=150,
    height=150,
    position="bottomright"
).add_to(walk_map)


# A search box is added to the map.
folium.plugins.Geocoder().add_to(walk_map)


# Add layer control to show and hide different map layers.
folium.LayerControl().add_to(walk_map)


# Save the interactive map as an HTML file.
# You can open walk.html from your folder at any time
# and see the changes in a web browser.
walk_map.save("walk.html")
