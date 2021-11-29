import csv

'''
    This function reads in the original csv file
    and removes an lines with no data.
'''

def file(file_to_open:str):
    
    file = open(file_to_open, encoding='utf-8')
    #file = open("merged-pythondev-help-concat-group.csv", encoding='utf-8')
    csvreader = csv.reader(file)
    
    #Skip past the CSV header line
    next(csvreader)
    
    return_csv = []
    for row in csvreader:
        if(row != []):
            return_csv.append(row)

    return return_csv
