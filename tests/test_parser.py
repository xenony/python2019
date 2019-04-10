from src.files.fileProcessing import parse_xml, change_values, convert_xml_to_json
import filecmp
import os
import json


initial_xml_file = os.path.abspath("file_samples/xml/test_data.xml")
updated_xml_file = os.path.abspath("file_samples/xml/new_data.xml")
new_json = os.path.abspath("file_samples/json/updated_test_data.json")
expected_json = os.path.abspath("file_samples/json/expected_test_data.json")
expected_xml_file = os.path.abspath("file_samples/xml/expected_data.xml")


class TestParser:

    def test_initial_xml_file_exists(self):
        assert os.path.isfile(initial_xml_file)

    def test_parse_xml(self):
        assert parse_xml(initial_xml_file)
        os.remove(updated_xml_file)

    def test_updated_xml_file_exists(self):
        change_values(initial_xml_file)
        assert os.path.isfile(updated_xml_file)
        os.remove(updated_xml_file)

    def test_compare_updated_and_expected_xml(self):
        change_values(initial_xml_file)
        assert filecmp.cmp(updated_xml_file, expected_xml_file) == True
        os.remove(updated_xml_file)

    def test_negative_compare_updated_and_expected_xml(self):
        change_values(initial_xml_file)
        assert filecmp.cmp(updated_xml_file, initial_xml_file) == False
        os.remove(updated_xml_file)

    def test_check_updated_first_name_field_xml(self):
        change_values(initial_xml_file)
        tree = parse_xml(updated_xml_file)
        root = tree.getroot()
        for elem in root.iter('FIRST_NAME'):
            assert elem.text == 'Ivan'
        os.remove(updated_xml_file)

    def test_check_updated_project_field_xml(self):
        change_values(initial_xml_file)
        tree = parse_xml(updated_xml_file)
        root = tree.getroot()
        for elem in root.iter('PROJECT'):
            assert elem.text == 'ABC'
        os.remove(updated_xml_file)

    def test_new_json_file_exists(self):
        change_values(initial_xml_file)
        convert_xml_to_json()
        assert os.path.isfile(new_json)

    def test_compare_new_and_expected_json(self):
        change_values(initial_xml_file)
        convert_xml_to_json()
        assert os.path.isfile(new_json)
        assert filecmp.cmp(new_json, expected_json) == True

    def test_check_updated_first_name_field_json(self):
        change_values(initial_xml_file)
        convert_xml_to_json()
        with open(new_json) as f:
            data = json.load(f)
        assert data["PERSONS"]["PERSON"][0]["FIRST_NAME"] == "Ivan"




