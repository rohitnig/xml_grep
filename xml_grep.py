import xml.etree.ElementTree as ET
import sys

def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem

if len (sys.argv)>1:
   ip_file = sys.argv[1]
else:
    print ('Missing file')
    exit()

country_name = sys.argv[2] if (len(sys.argv)>2) else  ''

with open (ip_file, 'r') as xml_file:
    xml_data = "<data>"+xml_file.read().replace('\n', '')+"</data>"

#tree = ET.parse(ip_file)
#root = tree.getroot()

root = ET.fromstring(xml_data)

for country in root.findall('country'):
    name = country.find('name').text
    if (name == country_name):
        root.remove(country)

indent (root)
#ET.dump(root)
xml_string=ET.tostring(root)#, encoding='utf8', method='xml')
print xml_string.replace('<data>', '').replace('</data>', '')
