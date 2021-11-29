import reader
import clean_message_script
import check_dominant_emotion
import text2emotion as te

csv = reader.file(r'C:\Users\rsamm\OneDrive - University of Delaware - o365\CISC367\CISC367-project\Golden Set Data\text2emotion\emotion_golden_set.csv')
count = 1
for row in csv:
    cleaned_message = clean_message_script.clean_message(row[0])
    #print(count, ':', te.get_emotion(cleaned_message), "Dominant Emotion:", check_dominant_emotion.check_emotion(cleaned_message))
    print(check_dominant_emotion.check_emotion(cleaned_message))
    count += 1