from user_class import user
#from profanity_check import predict

def get_user_info(csvreader):
   user_dict = {}
   csvreader.__next__()
   for line in csvreader:
        if line[2] in user_dict.keys():
           user_dict[line[2]].total_messages+= 1
        else:
            user_dict[line[2]] = user(1, 0, 0, 0, 0, 0, 0)
        #if predict(line[3]):
            #user_dict[line[2]].profane_messages += 1
   return user_dict
