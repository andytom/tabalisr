"""
    tabalisr
    ========

    A simple app for converting csv files into a nicely formatted
    ascii table.

    The first row is assumed to be the header.

    foo,bar,baz
    1,2,3
    4,5,6

    +-----+-----+-----+
    | foo | bar | baz |
    +-----+-----+-----+
    | 1   | 2   | 3   |
    | 4   | 5   | 6   |
    +-----+-----+-----+

    :copyright: (c) 2013 by Thomas O'Donnell
    :license: BSD, see LICENSE for more details.
    :version: 0.1
"""
#-----------------------------------------------------------------------------#
# Setup
#-----------------------------------------------------------------------------#
from flask import Flask, render_template, flash
from flask_wtf import Form, TextField, Required, TextAreaField
from prettytable import from_csv
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO


app = Flask(__name__)
app.config.from_pyfile('main.cfg')


#-----------------------------------------------------------------------------#
# Helper methods
#-----------------------------------------------------------------------------#
def process_string(csv_string):
    """Take a raw csv string and convert it into an ascii table"""
    csv_io = StringIO.StringIO(csv_string)
    table = from_csv(csv_io)

    table.align = 'l'

    return table.get_string()


#-----------------------------------------------------------------------------#
# Forms
#-----------------------------------------------------------------------------#
class csv_form(Form):
    content = TextAreaField('CSV string',
                            validators=[Required()],
                            description="""The CSV string to be converted
                            into a table"""
                            )


#-----------------------------------------------------------------------------#
# Routes
#-----------------------------------------------------------------------------#
@app.route('/', methods=['GET', 'POST'])
def index():
    form = csv_form()

    if form.validate_on_submit():
        table = process_string(form.content.data)
        flash("All done", "alert-success")
        return render_template('download.html', table=table)
    return render_template('index.html', form=form)
