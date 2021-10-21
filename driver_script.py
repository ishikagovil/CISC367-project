import input_script
import authors_script
import os
import csv
directory_name = os.getcwd()
csvreader = input_script.read_input_csv(directory_name, "merged-pythondev-help-concat-group.csv")
user_dict = authors_script.get_user_info(csvreader)


filename = "master.csv"
fields = ['user_ID', 'total_messages', 'profane_messages', 'avg_angry_score', 'avg_happy_score', 'avg_sad_score', 'avg_surprised_score', 'avg_fear_score']
rows = []
for key in user_dict.keys():
    rows.append([key, user_dict[key].total_messages, user_dict[key].profane_messages, user_dict[key].avg_angry_score, user_dict[key].avg_happy_score, user_dict[key].avg_sad_score, user_dict[key].avg_surprised_score, user_dict[key].avg_fear_score])
with open(directory_name + "/" + filename, 'w') as csvfile:  
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)          
    csvwriter.writerows(rows)