import unittest
import json

from tabalisr.app import app
from tabalisr.lib import process_string


#-----------------------------------------------------------------------------#
# Helper functions
#-----------------------------------------------------------------------------#
def load_json_tests(filename):
    with open(filename, 'r') as f:
        return json.loads(f.read())


#-----------------------------------------------------------------------------#
# Test Cases
#-----------------------------------------------------------------------------#
class LibTestCase(unittest.TestCase):
    """Tests to test the libary functions"""
    def setUp(self):
        json_file = 'test/table_construction_tests.json'
        self.all_tests = load_json_tests(json_file)

    def _run_test(self, test_name):
        test = self.all_tests[test_name]
        self.assertEqual(process_string(test['input']), test['result'])

    def test_table_construction(self):
        self._run_test("Basic Construction test")

    def test_whitespace_in_string(self):
        self._run_test("Whitespace Test")


#-----------------------------------------------------------------------------#
if __name__ == '__main__':
    unittest.main()
