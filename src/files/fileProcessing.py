from lxml import etree
import os
import json
import xmltodict


initial_xml_file = os.path.abspath("file_samples/xml/test_data.xml")
updated_xml_file = os.path.abspath("file_samples/xml/new_data.xml")
new_json = os.path.abspath("file_samples/json/updated_test_data.json")
# expected_json = os.path.abspath("file_samples/json/expected_test_data.json")
# expected_xml_file = os.path.abspath("file_samples/xml/expected_data.xml")

first_name = 'Ivan'
last_name = 'Ivanov'
project = 'ABC'
role = 'TL'
birthday = '33'
room = '11'
hobby = 'Gamer'


def parse_xml(file):
    return etree.parse(file)


def change_values(file):
    tree = parse_xml(file)
    root = tree.getroot()
    for elem in root.iter('FIRST_NAME'):
        elem.text = first_name
    for elem in root.iter('LAST_NAME'):
        elem.text = last_name
    for elem in root.iter('PROJECT'):
        elem.text = project
    for elem in root.iter('DAY_OF_BIRTH'):
        elem.text = birthday
    for elem in root.iter('ROLE'):
        elem.text = role
    for elem in root.iter('ROOM'):
        elem.text = room
    for elem in root.iter('HOBBY'):
        elem.text = hobby
    tree.write(updated_xml_file)


def convert_xml_to_json():
    with open(updated_xml_file, 'r') as f:
        xmlString = f.read()
    jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)

    with open(new_json, 'w') as f:
        f.write(jsonString)


change_values(initial_xml_file)
convert_xml_to_json()

