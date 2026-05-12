# import Python libraries
import folium
from folium import plugins
from folium.features import DivIcon
import pandas as pd
import geopandas as gpd


def create_popup_html(title, text="", image_path=None, alt_text="", image_width="700px"):
    """
    Create HTML content for a Folium popup.
    The image_width value controls how large photos appear when a marker is clicked.
    """

    image_html = ""

    if image_path:
        image_html = f"""
        <p>
            <img src="{image_path}"
                 style="width:{image_width}; max-width:100%; border-radius:10px;"
                 alt="{alt_text}">
        </p>
        """

    html = f"""
    <div style="width:720px;">
        <h3>{title}</h3>
        <h4>{text}</h4>
        {image_html}
    </div>
    """

    return html


def add_custom_marker(map_object, location, tooltip, popup_html,
                      icon_path, icon_size=(50, 50), popup_width=800):
    """
    Add a custom marker with popup and icon to the Folium map.
    popup_width controls the size of the popup window.
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
    Return marker colour based on the peak height category.
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


# PEAK MARKERS
peaks_df = pd.read_csv("./data_files/peaks.csv")

geometry = gpd.points_from_xy(
    peaks_df.Longitude,
    peaks_df.Latitude
)

geo_df = gpd.GeoDataFrame(
    peaks_df[
        ["Name", "Height",
         "Irish_Grid",
         "Latitude",
         "Longitude",
         "Type"]
    ],
    geometry=geometry
)

# Created a geometry list from the GeoDataFrame.
geo_df_list = [
    [point.xy[1][0], point.xy[0][0]]
    for point in geo_df.geometry
]

# Iterate through list and add marker for each peak.
for i, coordinates in enumerate(geo_df_list):

    type_color = get_peak_colour(
        geo_df.Type[i]
    )

    popup_html = f"""
    <div style="width:500px;">

    <h2>{geo_df.Name[i]}</h2>

    <h3>
    Height: {geo_df.Height[i]}
    </h3>

    <h3>
    Irish Grid:
    {geo_df.Irish_Grid[i]}
    </h3>

    <h3>
    Coordinates:
    {geo_df_list[i]}
    </h3>

    </div>
    """

    folium.Marker(

        location=coordinates,

        popup=folium.Popup(
            popup_html,
            max_width=600
        ),

        icon=folium.Icon(
            color=type_color
        )

    ).add_to(walk_map)


# Adding legends as floating images.
plugins.FloatImage(
    "./images/legend_peaks.png",
    bottom="55",
    left="91",
    width="200px"
).add_to(walk_map)

plugins.FloatImage(
    "./images/legend_map.png",
    bottom="31",
    left="91",
    width="200px"
).add_to(walk_map)


# Adding text to the map using DivIcon.
folium.map.Marker(
    [54.2174, -5.8474],
    icon=DivIcon(
        icon_size=(250, 50),
        icon_anchor=(0, 0),
        html='<div style="font-size: 25pt">12 km charity walk</div>'
    )
).add_to(walk_map)


# POINTS OF INTEREST ON THE WAY

# No. 1 - Start point.
html_start = create_popup_html(
    title="<strong>START OF THE WALK</strong>",
    text="Bloody Bridge Car Park",
    image_path="images/BloodyBridge.jpg",
    alt_text="Bloody Bridge car park",
    image_width="700px"
)

add_custom_marker(
    map_object=walk_map,
    location=[54.174232, -5.873921],
    tooltip="<h4>Click here to see start of the walk</h4>",
    popup_html=html_start,
    icon_path="./images/Start.png",
    icon_size=(100, 60),
    popup_width=800
)


# Points of interest No. 2 to No. 6.
marker_df = pd.read_csv("./data_files/popup26.csv")

for _, row in marker_df.iterrows():

    html = create_popup_html(
        title=row["title"],
        text=row["text"],
        image_path=row["img_src"],
        alt_text=row["alt"],
        image_width="700px"
    )

    add_custom_marker(
        map_object=walk_map,
        location=[row["latitude"], row["longitude"]],
        tooltip="<h4>Click here to see the surrounding area</h4>",
        popup_html=html,
        icon_path="./images/icon_green.png",
        icon_size=(30, 50),
        popup_width=800
    )


# No. 7 - Finish point.
html_finish = """
<div style="width:720px;">
    <a href="http://www.meelmorelodge.co.uk/" target="_blank">
    Visit Meelmore Lodge website
    </a>
    <br>
    <h2><strong>FINISH</strong></h2>
    <h3>Meelmore Lodge Hostel, campsite and parking</h3>
    <p>
        <img src="images/MeelmoreLodge.jpg"
             style="width:700px; max-width:100%; border-radius:10px;"
             alt="Meelmore Lodge">
    </p>
</div>
"""

add_custom_marker(
    map_object=walk_map,
    location=[54.209130, -5.999262],
    tooltip="<h4>Click here to see end of the walk</h4>",
    popup_html=html_finish,
    icon_path="./images/Finish.png",
    icon_size=(100, 60),
    popup_width=800
)


# CLIMBING AREAS
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


# PARKING AREAS
add_csv_icon_markers(
    map_object=walk_map,
    csv_path="./data_files/parking_all.csv",
    icon_path="./images/parking.png",
    tooltip="<h4>Click here to see parking name</h4>",
    name_column="parking_name",
    icon_size=(50, 50)
)


# GEOJSON LAYERS
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


# WALKING TRAIL
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
walk_map.add_child(folium.LatLngPopup())

# Remove the next # if you want to see the line for the walk animated.
# plugins.AntPath(trail_coordinates).add_to(walk_map)

# Add coordinates of mouse position on the top right.
fmtr = "function(num) {return L.Util.formatNum(num, 4) + ' º ';};"

# Add a field that shows the coordinates
# of the mouse position on the top right.

fmtr = """
function(num) {
return L.Util.formatNum(num, 4) + ' º ';
};
"""

plugins.MousePosition(
    position="topright",
    separator=" | ",
    empty_string="Move mouse over map",
    num_digits=4,
    prefix="""
    <span style="
    font-size:12px;
    font-weight:bold;
    ">
    Coordinates:
    </span>
    """,
    lat_formatter=fmtr,
    lng_formatter=fmtr
).add_to(walk_map)

# Measure control.
folium.plugins.MeasureControl(
    position="topleft",
    active_color="red",
    completed_color="red"
).add_to(walk_map)

# Locate user.
plugins.LocateControl().add_to(walk_map)

# Logo.
plugins.FloatImage(
    "./images/j.png",
    bottom=6,
    left=1,
    width="60px"
).add_to(walk_map)

# Full screen button.
plugins.Fullscreen(
    force_separate_button=True,
    title="Click here to see Full Screen"
).add_to(walk_map)

# Small MiniMap.
plugins.MiniMap(
    width=150,
    height=150,
    position="bottomright"
).add_to(walk_map)

# Search box.
folium.plugins.Geocoder().add_to(walk_map)

# Layer control.
folium.LayerControl().add_to(walk_map)

# Save the interactive map as an HTML file.
walk_map.save("walk.html")
