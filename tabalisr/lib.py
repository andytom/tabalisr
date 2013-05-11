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


#-----------------------------------------------------------------------------#
# CSV
#-----------------------------------------------------------------------------#
def csv_to_array(content):
    """Turn the passed csv string into an array."""
    csv_io = StringIO.StringIO(content)

    try:
        dialect = csv.Sniffer().sniff(csv_io.read(1024))
    except:
        # Sniffing didn't work assume it is excel
        dialect = 'excel'
    csv_io.seek(0)

    return [i for i in csv.reader(csv_io, dialect)]


#-----------------------------------------------------------------------------#
# Ascii Table generation
#-----------------------------------------------------------------------------#
def generate_table(array_iterator):
    """Take a square array of arrays and return an ascii table."""
    max_lengths = get_max_length(array_iterator)

    final_array = []

    # Build all the individual rows
    for i in array_iterator:
        final_array.append(make_row(i, max_lengths))

    # Add spacers to make the header and close off the bottom
    spacer = make_spacer(max_lengths)
    final_array.insert(0, spacer)
    final_array.insert(2, spacer)
    final_array.append(spacer)

    return "\n".join(final_array)


def make_spacer(length_array):
    """Make a spacer."""
    inner = '+'.join(['-' * (i + 2)for i in length_array])
    return ''.join(['+', inner, '+'])


def make_row(row, max_length):
    """Make a row"""
    final_row = []
    for i, max_size in enumerate(max_length):
        if len(row) > i:
            string = row[i]
        else:
            string = ''
        final_row.append('| {:<{max_size}} '.format(string, max_size=max_size))

    final_row.append('|')
    return "".join(final_row)


def get_max_length(array_iterator):
    """Return an array of the longest string at each index in each array
       in the passed array iterator.
    """
    longest_array = max([len(i)for i in array_iterator])
    max_length = [0] * longest_array

    for line in array_iterator:
        for i, string in enumerate(line):
            if len(string) > max_length[i]:
                max_length[i] = len(string)

    return max_length


def process_string(csv_string):
    """Take a raw csv string and convert it into an ascii table"""
    csv_arrays = csv_to_array(csv_string)

    return generate_table(csv_to_array(csv_string))


#-----------------------------------------------------------------------------#
# Use for testing
#-----------------------------------------------------------------------------#
if __name__ == '__main__':
    test_data = """Foo,Bar,Baz,a
spam,ham,spam and eggs,
4,5,6,c"""
    print process_string(test_data)
