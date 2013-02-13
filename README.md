#Tabalisr
Turn csv into ascii tables.

##About

A simple app for converting csv files into a nicely formatted
ascii table.

The first row is assumed to be the header.

<pre>
foo,bar,baz
1,2,3
4,5,6
</pre>

<pre>
+-----+-----+-----+
| foo | bar | baz |
+-----+-----+-----+
| 1   | 2   | 3   |
| 4   | 5   | 6   |
+-----+-----+-----+
</pre>

##Usage

A list of requirements can be found in the requirements.pip file.

You should change the SECRET_KEY in the main.cfg file to be something more secure.

A development server can be started by running "<pre>python run_dev_server.py</pre>".


