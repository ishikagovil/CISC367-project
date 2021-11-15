import re

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
    
    return(cleaned_message)