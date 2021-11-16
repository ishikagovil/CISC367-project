from user_class import user
import text2emotion as te
#from profanity_check import predict

def get_user_info(csvreader):
   user_dict = {}
   csvreader.__next__()
   for line in csvreader:
        #example blackList here: https://github.com/web-mech/badwords/blob/master/lib/lang.json
        ##blackList = {"shit" , "fuck", "damn"}
        ##containsWord = any(ext in line[3] for ext in blackList)
        ##if(containsWord == True):
            ##user_dict[line[2]].profane_messages += 1
        
        ##print(line[0])
        message =  te.get_emotion(line[3])
        angryMessage = message.get("Angry")
        happyMessage = message.get("Happy")
        sadMessage = message.get("Sad")
        surprisedMessage = message.get("Surprise")
        fearMessage = message.get("Fear")
        if line[2] in user_dict.keys():
           totalAngry = user_dict[line[2]].avg_angry_score * user_dict[line[2]].total_messages
           totalHappy = user_dict[line[2]].avg_happy_score * user_dict[line[2]].total_messages
           totalSad = user_dict[line[2]].avg_sad_score * user_dict[line[2]].total_messages
           totalSurprised = user_dict[line[2]].avg_surprised_score * user_dict[line[2]].total_messages
           totalFear = user_dict[line[2]].avg_fear_score * user_dict[line[2]].total_messages
           
           
           avgAngry = (totalAngry + angryMessage) / (user_dict[line[2]].total_messages + 1)
           avgHappy = (totalHappy + happyMessage) / (user_dict[line[2]].total_messages + 1)
           avgSad = (totalSad + sadMessage) / (user_dict[line[2]].total_messages + 1)
           avgSurprised = (totalSurprised + surprisedMessage) / (user_dict[line[2]].total_messages + 1)
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
