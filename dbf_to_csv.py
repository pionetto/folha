print("start")
import csv, os
from dbfpy import dbf

input_path = r"/home/pio/folha"
output_path = r"/home/pio/folha/convertido"

for dirpath, dirnames, filenames in os.walk(input_path):
    for filename in filenames:
        if filename.endswith('.DBF'.upper()):
            print ("Convertendo {} para csv".format(filename))
            csv_fn1 = filename[:-8]+ ".csv"
            csv_fn = os.path.join(output_path, csv_fn1)
            with open(csv_fn, 'wb') as csvfile:
                in_db = dbf.Dbf(os.path.join(dirpath, filename))
                out_csv = csv.writer(csvfile)
                names = []
                for field in in_db.header.fields:
                    names.append(field.name)
                out_csv.writerow(names)
                for rec in in_db:
                    out_csv.writerow(rec.fieldData)
                in_db.close()
                print("Concluido!")
