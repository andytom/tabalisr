from __future__ import unicode_literals
import unittest

from tabalisr.app import app, process_string


#-----------------------------------------------------------------------------#
# Test Cases
#-----------------------------------------------------------------------------#
class LibTestCase(unittest.TestCase):
    """Tests to test the libary functions"""
    def test_table_construction(self):
        test_csv = "Foo,Bar,Baz\nspam,ham,spam and eggs"
        result = """+------+-----+---------------+
| Foo  | Bar | Baz           |
+------+-----+---------------+
| spam | ham | spam and eggs |
+------+-----+---------------+"""

        self.assertEqual(process_string(test_csv), result)


#-----------------------------------------------------------------------------#
if __name__ == '__main__':
    unittest.main()
