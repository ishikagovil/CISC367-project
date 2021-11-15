from profanity_check import predict

#Takes in a string and returns a boolean value representing whether
#profanity-check thinks the message is profane or not.

#True = Message Contains Profanity
#False = Message DOES NOT Contain Profanity
      
def check_profanity(message:str) -> bool:
    output_numpy = predict([message])
    return bool(output_numpy[0])