"""
    tabalisr forms
    ==============

    Forms for tabalisr.

    :copyright: (c) 2013 by Thomas O'Donnell.
    :license: BSD, see LICENSE for more details.
    :version: 0.1
"""

from flask_wtf import Form, TextField, Required, TextAreaField

#------------------------------------------------------------------------------#
# Forms
#------------------------------------------------------------------------------#
class csv_form(Form):
    content = TextAreaField('CSV string',
                            validators = [Required()],
                            description = """The CSV string to be converted 
                            into a table"""
                           )

