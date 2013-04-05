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
from tabalisr.forms import csv_form
from tabalisr.lib import process_string

app = Flask(__name__)
app.config.from_pyfile('main.cfg')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = csv_form()

    if form.validate_on_submit():
        table = process_string(form.content.data)
        flash("All done", "alert-success")
        return render_template('download.html', table=table)

    return render_template('index.html', form=form)
