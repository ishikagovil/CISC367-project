from user_class import user
import text2emotion as te
#from profanity_check import predict

def get_user_info(csvreader):
   user_dict = {}
   csvreader.__next__()
   for line in csvreader:
        print(line[0])
        angryMessage = te.get_emotion(line[3]).get("Angry")
        happyMessage = te.get_emotion(line[3]).get("Happy")
        sadMessage = te.get_emotion(line[3]).get("Sad")
        surprisedMessage = te.get_emotion(line[3]).get("Surprise")
        fearMessage = te.get_emotion(line[3]).get("Fear")
        if line[2] in user_dict.keys():
           totalAngry = user_dict[line[2]].avg_angry_score * user_dict[line[2]].total_messages
           totalHappy = user_dict[line[2]].avg_happy_score * user_dict[line[2]].total_messages
           totalSad = user_dict[line[2]].avg_sad_score * user_dict[line[2]].total_messages
           totalSurprised = user_dict[line[2]].avg_surprised_score * user_dict[line[2]].total_messages
           totalFear = user_dict[line[2]].avg_fear_score * user_dict[line[2]].total_messages
           
           if(totalAngry + angryMessage == 0):
               avgAngry = 0
           else:
               avgAngry = (totalAngry + angryMessage) / (user_dict[line[2]].total_messages + 1)


           if(totalHappy + happyMessage == 0):
               avgHappy = 0
           else:
               avgHappy = (totalHappy + happyMessage) / (user_dict[line[2]].total_messages + 1)
           

           if(totalSad + sadMessage == 0):
               avgSad = 0
           else:
               avgSad = (totalSad + sadMessage) / (user_dict[line[2]].total_messages + 1)
           

           if(totalSurprised + surprisedMessage == 0):
               avgSurprised = 0
           else:
               avgSurprised = (totalSurprised + surprisedMessage) / (user_dict[line[2]].total_messages + 1)
            
           
           if(totalFear + fearMessage == 0):
               avgFear = 0
           else:
                avgFear = (totalFear + fearMessage) / (user_dict[line[2]].total_messages + 1)
           

           user_dict[line[2]].avg_angry_score = avgAngry
           user_dict[line[2]].avg_happy_score = avgHappy
           user_dict[line[2]].avg_sad_score = avgSad
           user_dict[line[2]].avg_surprised_score = avgSurprised
           user_dict[line[2]].avg_fear_score = avgFear

        
           user_dict[line[2]].total_messages+= 1
        else:
            user_dict[line[2]] = user(1, 0, angryMessage, happyMessage, sadMessage, surprisedMessage, fearMessage)
        #if predict(line[3]):
            #user_dict[line[2]].profane_messages += 1
   return user_dict
