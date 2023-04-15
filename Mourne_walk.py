import folium

#folium map with a centre of your map (Mourne Mountain - close to Slieve Donard in this example)
#the latitude is first the longitude is the second
map = folium.Map(location=[54.184431, -5.941592], zoom=12.3)
map.save("walk.html")



