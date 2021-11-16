import reader
import clean_message_script
import profanity_check_script

csv = reader.file(r'C:\Users\rsamm\OneDrive - University of Delaware - o365\CISC367\CISC367-project\Golden Set Data\profanity_check\profanity_golden_set.csv')
count = 1
for row in csv:
    cleaned_message = clean_message_script.clean_message(row[0])
    print(count, ':', profanity_check_script.check_profanity(cleaned_message))
    count += 1