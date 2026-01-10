import csv

file_path = './products.csv'
updated_file_path = './products_updated.csv'

with open(file_path, mode="r") as file:
    csv_reader = csv.DictReader(file)
    #Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ['total_value'] + ['sku'] + ['IVA']

    with open(updated_file_path, mode="w", newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames= fieldnames)
        csv_writer.writeheader() #Escribir encabezado
        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            row['sku'] = row['name']+'_'+row['brand']
            row['IVA'] = float(row['price']) * 0.16
            csv_writer.writerow(row)