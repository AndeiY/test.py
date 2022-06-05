import json
import xml.etree.ElementTree as ET

with open('data_Source_3.json') as json_file:
    data = json.load(json_file, strict=False)

class Product1:
     def __init__(self, name, id, EANs):
        self.name = name
        self.id = id
        self.EANs = EANs

objects = []
objects.append(Product1(data[0]['name'], data[0]['Id'], data[0]['EANs']))
objects.append(Product1(data[1]['name'], data[1]['Id'], data[1]['EANs']))
objects.append(Product1(data[2]['name'], data[2]['Id'], data[2]['EANs']))

for el in range(len(data)):
    objects.append(Product1(data[el]['name'], data[el]['Id'], data[el]['EANs']))
    # print(data[el]['name'], data[el]['Id'], data[el]['EANs'])

class Product2:
    def __init__(self, name, EAN, id):
        self.name = name
        self.id = id
        self.EAN = EAN



object1 = []
tree = ET.parse("data_Soruce_1.xml")
for element in tree.findall("SHOPITEM"):
    name = element.find("NAME").text
    id = element.find("id").text
    try:
        EAN = element.find("EAN").text
    except:
        EAN="none"
    object1.append(Product2(name, EAN, id))


class Product3:
    def __init__(self, name, EAN, id):
        self.name = name
        self.EAN = EAN
        self.id = id


object2 = []
tree = ET.parse("data_Source_2.xml").getroot()
for element in tree.findall("Product"):
    EAN = element.find("EAN").text
    id = element.find("id").text
    name = element.find("Description").text
    object2.append(Product3(name, EAN, id))

#print(len(object))

sort = []
for el1 in range(len(objects)):
    el11 = objects[el1].__dict__
    el111 = el11['EANs'][0]
    for el2 in range(len(object1)):
        el22 = object1[el2].__dict__
        el222 = el22['EAN']
        if el111 == el222:
            for el3 in range(len(object2)):
                el33 = object2[el3].__dict__
                el333 = el33['EAN']
                if el111 == el222 and el111 == el333:
                    sort.append(el22)
                    sort.append(el33)
                    sort.append(el11)
                else:
                    pass
        else:
            pass

jsonString = json.dumps(sort, indent=4)
print(jsonString)