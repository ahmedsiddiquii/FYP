from sqlalchemy import MetaData, create_engine
from sqlalchemy_schemadisplay import create_schema_graph
import argparse
import os
import sys
import tempfile
import subprocess
import pandas as pd
import pymysql
from sqlalchemy import create_engine

cnx = create_engine("mysql+pymysql://root:Ahmed12345@localhost:3306/test")
df = pd.read_sql('SELECT * FROM person_role', cnx)


# get connection string
db_conn_string = "mysql+pymysql://root:Ahmed12345@localhost:3306/test"

# get connection
try:
    e = create_engine(db_conn_string)
    m = MetaData()

    m.reflect(bind = e, schema = "test")

    tables_in_db = m.tables.keys()
except Exception as e:
    print('Problems accessing database: %s' % e)
    sys.exit(1)



# generate the schema graph
graph = create_schema_graph(tables = [m.tables[x] for x in list(m.tables.keys())],
                            show_datatypes=False,
                            show_indexes=False,
                            rankdir='TB',
                            concentrate=True,
                            )

# Write out graph to the corresponding file
if True:
    # get file extension
    filename, fileext = "piaza",".png"
    fn = "piaza.png"
    print(fn)
    if fileext == '.pdf':
        graph.write_pdf(fn)
    elif fileext == '.png':
        graph.write_png(fn)
    elif fileext == '.svg':
        graph.write_svg(fn)
    else:
        graph.write_pdf(fn)


e.dispose()

# open up the file
print('-- Opening %s' % fn)
subprocess.Popen('open %s' % fn, shell=True)
