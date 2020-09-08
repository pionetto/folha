import psycopg2
import pandas as pd
import sys

def pg_load_table(file_path, table_name, dbname, host, port, user, pwd):
    '''
    This function upload csv to a target table
    '''
    try:
        conn = psycopg2.connect(dbname=dbname, host=host, port=port,\
         user=user, password=pwd)
        print("Connecting to Database")
        cur = conn.cursor()
        f = open(file_path, "r", encoding='ISO-8859-1')
        # Truncate the table first
        cur.execute("Truncate {} Cascade;".format(table_name))
        print("Truncated {}".format(table_name))
        # Load table from the file with header
        cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format(table_name), f)
        cur.execute("commit;")
        print("Loaded data into {}".format(table_name))
        conn.close()
        print("DB connection closed.")
    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)

# Execution Example
file_path = '/home/pio/folha/convertido/S.csv'
table_name = 'public.tb_servidores_geral'
dbname = 'folha'
host = 'localhost'
port = '5432'
user = 'postgres'
pwd = '12345678'
pg_load_table(file_path, table_name, dbname, host, port, user, pwd)

#https://www.mydatahack.com/how-to-bulk-load-data-into-postgresql-with-python/
