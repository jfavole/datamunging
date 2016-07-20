from urllib import urlopen
import lxml
import xml.etree.ElementTree as ET
import pandas as pd

xml = urlopen("http://www.w3schools.com/xml/plant_catalog.xml")
tree = ET.parse(xml)
root = tree.getroot()
root.tag
root.attrib

for child in root[0]:
    print child.tag, child.attrib
    
common_list = []
botanical_list = []
zone_list = []
light_list = []
price_list = []
availability_list = []

for plant in root.findall("PLANT"):
    common = plant.find("COMMON").text
    common_list.append(common)
    botanical = plant.find("BOTANICAL").text
    botanical_list.append(botanical)
    zone = plant.find("ZONE").text
    zone_list.append(zone)
    light = plant.find("LIGHT").text
    light_list.append(light)
    price = plant.find("PRICE").text
    price_list.append(price)
    availability = plant.find("AVAILABILITY").text
    availability_list.append(availability)
    
print common_list
print botanical_list
print zone_list
print light_list
print price_list
print availability_list   

df = pd.DataFrame({'common':common_list, 'botanical':botanical_list, 'zone':zone_list, 'light':light_list, 'price':price_list, 'availability':availability_list})
print df
    
df.describe()