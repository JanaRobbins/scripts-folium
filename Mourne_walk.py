import folium

#folium map with a centre of your map (Mourne Mountain - close to Slieve Donard in this example)
#the latitude is first the longitude is the second
# zoom has to be tried to suit the required view, bigger number means more detailed map, decimal number can be used
# default tiles are Open Street Map, but you can use Stamen Terrain, Stamen Toner, Mapbox Bright, Mapbox Control Room

map = folium.Map(location=[54.184431, -5.941592], zoom_start=14, tiles="Stamen Terrain")


map.save("walk.html")



