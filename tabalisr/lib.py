"""
    tabalisr libs
    =============

    A libary containing helper functions for dealing with converting csv
    strings to ascii tables.

    :copyright: (c) 2013 by Thomas O'Donnell.
    :license: BSD, see LICENSE for more details.
    :version: 0.1
"""
import csv
import StringIO

#------------------------------------------------------------------------------#
# CSV 
#------------------------------------------------------------------------------#
def csv_to_array( content ):
    """Turn the passed csv string into an array."""
    csv_io = StringIO.StringIO(content)

    dialect = csv.Sniffer().sniff( csv_io.read(1024) )
    csv_io.seek(0)

    return [i for i in csv.reader(csv_io, dialect)]

#------------------------------------------------------------------------------#
# Ascii Table generation
#------------------------------------------------------------------------------#
def generate_table( array_iterator ):
    """Take a square array of arrays and return an ascii table."""
    max_length = get_max_length(array_iterator)

    final_array = []

    # Insert the top spacer row
    final_array.append(make_spacer(max_length))

    # Build all the individual rows
    for i in array_iterator:
        final_array.append(make_row(i, max_length))
    
    # Add a second spacer to make the header
    final_array.insert(2, make_spacer(max_length))
    final_array.append(make_spacer(max_length))

    return "\n".join(final_array)

def make_spacer( length_array ):
    """Make a spacer."""
    inner = '+'.join([ '-' * ( i + 2 ) for i in length_array])
    return ''.join(['+',inner ,'+'])

def make_row( row, max_length ):
    """Make a row"""
    final_row = ""
    for i, string in enumerate(row):
        padding = ' ' * ( max_length[i] - len(string) + 1 )
        final_row += '| '+string + padding

    return final_row + '|'

def get_max_length(array_iterator):
    """Return an array of the longest string at each index in each array
       in the passed array iterator.
    """
    max_length = [ 0 ] * len( array_iterator[0] )

    for line in array_iterator:
       for i, string in enumerate(line):
          if len(string) > max_length[i]:
             max_length[i] = len(string) 

    return max_length

def process_string( csv_string ):
    """Take a raw csv string and convert it into an ascii table"""
    csv_arrays = csv_to_array( csv_string )

    return generate_table(csv_to_array(csv_string))

#------------------------------------------------------------------------------#
# Use for testing
#------------------------------------------------------------------------------#
if __name__ == '__main__':
    test_data = "Foo, bar, baz,a\nspam,ham,spam and eggs,b\n4,5,6,c"
    print process_string( test_data )
