import text2emotion as te

#Note this requires a CLEANED message to function

def check_emotion(message):
    
    output = te.get_emotion(message)
    
    dominant_value_names = []
    dominant_value_number = 0
    dominant_value_names.append('Neutral')
    
    emotions = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
    
    for emotion in emotions:
        if output[emotion] > dominant_value_number:
            dominant_value_number = output[emotion]
            dominant_value_names = []
            dominant_value_names.append(emotion)
            
        elif output[emotion] == dominant_value_number and dominant_value_names != ['Neutral']:
            dominant_value_names.append(emotion)
            
    return(dominant_value_names)
    