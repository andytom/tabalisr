import unittest
import json

from tabalisr.app import app
from tabalisr.lib import process_string


#-----------------------------------------------------------------------------#
def load_json_tests(filename):
    with open(filename, 'r') as f:
        return json.loads(f.read())


#-----------------------------------------------------------------------------#
class LibTestCase(unittest.TestCase):
    def test_table_construction(self):
        json_file = 'test/table_construction_tests.json'
        for test in load_json_tests(json_file):
            assert process_string(test['input']) == test['result']


#-----------------------------------------------------------------------------#
if __name__ == '__main__':
        unittest.main()
