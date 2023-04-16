import folium

#folium map with a centre of your map (Mourne Mountain - close to Slieve Donard in this example)
#the latitude is first the longitude is the second
# zoom has to be tried to suit the required view, bigger number means more detailed map, decimal number can be used
# default tiles are Open Street Map, but you can use Stamen Terrain, Stamen Toner, cartodb positron, Mapbox Bright (needs api key), Mapbox Control Room

map = folium.Map(location=[54.184431, -5.941592], zoom_start=14, tiles="Stamen Terrain")

folium.Marker (location=[54.174232, -5.873921], popup="Bloody Bridge Car Park", icon=folium.Icon(icon="cloud"),).add_to(map)
folium.Marker (location=[54.170992, -5.912109], popup="Crannoge Quarry", icon=folium.Icon(color="green"),).add_to(map)
folium.Marker (location=[54.172241, -5.927770], popup="Bog of Donard", icon=folium.Icon(color="red", icon="info-sigh"),).add_to(map)
folium.Marker (location=[54.182588, -5.873921], popup="The Castles", icon=folium.Icon(icon="cloud"),).add_to(map)
folium.Marker (location=[54.188887, -5.962319], popup="Ben Crom Reservoir View", icon=folium.Icon(icon="cloud"),).add_to(map)
folium.Marker (location=[54.190175, -5.974230], popup="Hares' Gap", icon=folium.Icon(icon="cloud"),).add_to(map)
folium.Marker (location=[54.209130, -5.999262], popup="Meelmore Lodge", icon=folium.Icon(icon="cloud"),).add_to(map)



map.save("walk.html")



