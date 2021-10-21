import csv
def read_input_csv(directory_name, filename):
    csvreader = csv.reader(open(directory_name + "/" + filename, 'rt'))
    return csvreader