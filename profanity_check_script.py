from profanity_check import predict
import re

#Takes in a string and returns a boolean value representing whether
#profanity-check thinks the message is profane or not.

#True = Message Contains Profanity
#False = Message DOES NOT Contain Profanity

def clean_message(message:str) -> str:
    
    #First clean out code blocks and tags to other forum
    #posters, which are identified with ``` and <> respectively
    message = re.sub(r'\```[^```]*\```', '', message)
    message = re.sub(r'\`[^`]*\`', '', message)
    message = re.sub(r'\<[^>]*\>', '', message)
    
    #Now we are going to remove emoticons:
    #Checks to see if any words begin and end with ':',
    #Which symbolizes an emoticon in the default CSV format.
    
    message = message.split()
    cleaned_message = ""
    for word in message:
        if(word[0] != ':' and word[-1] != '!'):
            cleaned_message += word
            cleaned_message += " "
    
    print(cleaned_message)
    
#Call check_profanity() on an uncleaned message and it will
#automatically clean it for you!
    
def check_profanity(message:str) -> bool:
    message = clean_message(message)
    output_numpy = predict([message])
    return bool(output_numpy[0])