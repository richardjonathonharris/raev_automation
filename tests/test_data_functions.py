import json 
from nose.tools import *

def test_card_data_provides_valid_json():
    testing_suite = ['action.json', 'deployment.json', 'class.json', 'agenda.json']
    for file in testing_suite:
        with open('data/%s' % file) as data_file:
            data = json.load(data_file)


