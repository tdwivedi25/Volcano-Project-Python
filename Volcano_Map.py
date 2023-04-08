import folium
import pandas

data=pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name=list(data['NAME'])


def color_producer(elevation):
   if elevation < 1000:
      return 'green'
   elif 100 <= elevation < 3000:
      return 'orange'
   else:
      return 'red'

map=folium.Map(location=[37.777120000000025, -122.41963999999996],zoom_start=6, tiles='Stamen Terrain')
#map.add_child(folium.Marker(location=[37.777120000000025, -122.41963999999996], popup='San Franciso, California',icon=folium.Icon(color='red')))

fgv=folium.FeatureGroup(name='Volcanoes')
for lt,ln,el,na in zip(lat, lon, elev,name):
   fgv.add_child(folium.Marker(location = [lt,ln], popup = 'Volcano Name:\t'  + na +'\tElevation:\t' + str(el)+  '\tmeters\t', 
   icon = folium.Icon(color = color_producer(el))))

fgp=folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <=  x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('Map1.html')