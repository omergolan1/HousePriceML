"""
import folium
m= folium.Map(location=[42.034534,-93.620369])
m.save('index.html')

"""
import os
import tempfile
os.system("attrib -h -s -r "+tempfile.gettempdir()+r"\temp.temp")
os.system("del "+tempfile.gettempdir()+r"\temp.temp")