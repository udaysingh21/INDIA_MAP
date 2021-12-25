import folium
import pandas

data = pandas.read_csv("states.txt")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
states = list(data["States"])

info = pandas.read_csv("in (1).csv")
City = list(info["city"])
Lat = list(info["lat"])
Lon = list(info["lng"])
pop = list(info["population"])

maps = folium.Map(location=[20.5937, 78.9629], zoom_start=5, tiles='Stamen Terrain')

fgl = folium.FeatureGroup(name="Polygon")
fgl.add_child(folium.GeoJson(data=(open("india.json", "r", encoding="utf-8-sig").read())))

fg = folium.FeatureGroup(name="STATES")
for lt, ln, name in zip(lat, lon, states):
    fg.add_child(folium.Marker(location=[lt, ln], popup=name, icon=folium.Icon(color="red")))

fgi = folium.FeatureGroup(name="CITIES")
for lat_, lan_, cty, ppl in zip(Lat, Lon, City, pop):
    fgi.add_child(folium.Marker(location=[lat_, lan_],
                                popup="<b>City: </b>" + cty + "<br> <b>Population: </b> " + str(ppl) + "<br>"
                                , icon=folium.Icon(color="blue")))

maps.add_child(fgl)
maps.add_child(fg)
maps.add_child(fgi)
maps.add_child(folium.LayerControl())

maps.save("Map_I.html")
