import json
import numpy as np
import codecs
import networkx as nx
from PIL import Image, ImageDraw
import folium
import station
import requests


response = requests.get('https://api.hh.ru/metro/2')
todos = json.loads(response.text)
print()
colors={'D6083B':'red','0078C9':'blue','009A49':'green','EA7125':'orange','702785':'purple'}

all_stations_all_lines=[]

for i in todos['lines']:
    all_stations_one_line=[]

    for j in i['stations']:
        one_station=station.stop()
        one_station.set_name(j['name'])
        one_station.set_color(colors.get(i['hex_color']))
        one_station.set_lat(j['lat'])
        one_station.set_lng(j['lng'])
        all_stations_one_line.append(one_station)
        print()
    all_stations_all_lines.append(all_stations_one_line)
    all_stations_one_line=[]
print()

map = folium.Map(location=[59.9386,30.3141], zoom_start = 12)

for i in all_stations_all_lines:
    for j in i:
        print()

        #folium.Marker(location=[j.get_lat(),j.get_lng()], popup = "Google HQ", icon=folium.Icon(color = j.get_color())).add_to(map)
        folium.CircleMarker(location=[j.get_lat(), j.get_lng()], radius = 9, popup=j.get_name(), fill_color=j.get_color(), color="black", fill_opacity = 0.9).add_to(map)
"""
for i in all_stations_all_lines:
    temp_list=[]
    for j in i:
        kk=[]
        kk.append(j.get_lat())
        kk.append(j.get_lng())
        temp_list.append(kk)
    #color_line = folium.ColorLine(temp_list, colors='blue', colormap='blue',
                                  #nb_steps=4, weight=5, opacity=0.7).add_to(map)
    color_line = folium.ColorLine(temp_list,[0],colormap=['blue','orange']).add_to(map)
"""
for i in all_stations_all_lines:
    for j in range(1,len(i)):
        lat1=i[j-1].get_lat()
        lat2=i[j].get_lat()
        lng1=i[j-1].get_lng()
        lng2=i[j].get_lng()
        color=i[j].get_color()


        color_line = folium.ColorLine([[lat1,lng1],[lat2,lng2]], [0], colormap=[i[j].get_color(), 'orange'],nb_steps=12, weight=5, opacity=0.7).add_to(map)

"""
color_line = folium.ColorLine(
        [[0, 0], [0, 45], [45, 45], [45, 0], [0, 0]],
        [0, 1, 2, 3],
        colormap=['b', 'g', 'y', 'r'],
        nb_steps=4,
        weight=10,
        opacity=1)
        """
"""
color_line = folium.ColorLine([[60.050182,30.443045],[60.034969,30.418224]],[0,1],colormap=['b','g'],nb_steps=4,
        weight=5,
        opacity=0.7)
color_line.add_to(map)
"""
map.save("map1.html")
print()


















#map = folium.Map(location=[59.9386,30.3141], zoom_start = 12)
#folium.Marker(location=[37.4074687,-122.086669], popup = "Google HQ", icon=folium.Icon(color = 'gray')).add_to(map)

#map.save("map1.html")

#stop = station.stop
#stop.id=1
#stop.name='abc'
#temp_list =[]
#for i in range(2):
    #one_stop = station.stop('abc'+str(i))
    #one_stop = station.stop()
    #one_stop.set_name('abc'+str(i))

    #one_stop.id = i
    #one_stop.name = 'abc'+str(i)
    #one_stop.set_name(one_stop,'abc'+str(i))

    #one_stop.set_id(i)
    #temp_list.append(one_stop)






print()
"""
names = json.loads(codecs.open('l10n.json','r','utf_8_sig').read())
graph = json.loads(codecs.open('data.json','r','utf_8_sig').read())

nodeStdict={}
for stop in graph['stops']['items']:
    nodeStdict[stop['nodeId']]=stop['stationId']
coorDict={}
for node in graph['nodes']['items']:
    coorDict[node['id']]=(node['attributes']['geoPoint']['lon'],node['attributes']['geoPoint']['lat'])
lats=[]
longs=[]
for value in coorDict.values():
    lats.append(value[1])
    longs.append(value[0])

for k,v in coorDict.items():
    coorDict[k]=((v[0]-np.min(longs))/(np.max(longs)-np.min(longs)),(v[1]-np.min(lats))/(np.max(lats)-np.min(lats)))
"""
"""
for i in coorDict.values():
    draw.point((i[0]+cc,i[1]+cc),(255, cc, 255))
    cc+=1
"""

"""
G=nx.Graph()
for node in graph['nodes']['items']:
    G.add_node(node['id'])
#graph['links']
for link in graph['links']['items']:
    #G.add_edges_from([(link['fromNodeId'],link['toNodeId'])])
    G.add_edge(link['fromNodeId'], link['toNodeId'], length=link['attributes']['time'])
nodestoremove=[]
for node in G.nodes():
    if len(G.edges(node))<2:
        nodestoremove.append(node)
for node in nodestoremove:
    G.remove_node(node)
labels={}
for node in G.nodes():
    try:
        labels[node]=names['keysets']['generated'][nodeStdict[node]+'-name']['ru']
    except: labels[node]='error'

"""
print()