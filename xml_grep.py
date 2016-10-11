import xml.etree.ElementTree as ET
import sys
tree = ET.parse('test.xml')

root = tree.getroot()
country_name = sys.argv[1]

for country in root.findall('country'):
    name = country.find('name').text
    if (name == country_name):
        root.remove(country)

tree.write(sys.stdout)
