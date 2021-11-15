import csv
def read_input_csv(directory_name, filename):
    csvreader = csv.reader(open(directory_name + "/" + filename, 'rt', encoding="utf-8"))
    return csvreader