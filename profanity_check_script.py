from profanity_check import predict

#More advanced profanity_check function, that checks against a manually curated blacklist if
#profanity_check believes there is no profanity in the message.

###########################################################
#  This function expects to take in a "cleaned" message!  #
###########################################################

#Takes in a string and returns a boolean value representing whether
#profanity-check thinks the message is profane or not.

#True = Message Contains Profanity
#False = Message DOES NOT Contain Profanity
      
def check_profanity(message:str) -> bool:
    
    print("Now checking for profanity:")
    print("\tSOURCE:", message)
    
    profanity_dict = {
        'a' : ["ahole","anus","arse","arse","arseh0le","arseh0les","arsehole","arseholes","arsewipes","ass","ass","assh0le","assh0les","asshat","asshole","assholes","assholz","asswipe"],
        'b' : ["b!+ch","b!tch","bastard","bastard","bastards","batshit","bitch","bitch","bitches","blowjob","bullshit"],
        'c' : ["c0ck","c0ck","c0cks","clit","clit","cock","cocks","cocksucker","cum","cunt","cunts","cuntz"],
        'd' : ["dick","dicks","dildo","dildos","dumbass","dyke"],
        'f' : ["f***", "f*ck", "fag","fagg0t","faggot","fags","fatass","fuck","fuck","fucker","fuckin","fuckin'","fucking","fucks","fuk","fukin"],
        'g' : ["goddam","goddamit","goddamn","goddamned","goddamnit"],
        'h' : ["horseshit"],
        'j' : ["jerk-off", "jerkoff"],
        'm' : ["masterbate","mother-fucker","motherfucker"],
        'n' : ["nigga","nigger"],
        'p' : ["p0rn","pen1s","penis","piss","pissing","porn","pr0n","prick","pussy"],
        'r' : ["retard", "retarded"],
        's' : ["sh!+","sh!t","sh!t","sh1t","shi+","shit","shit","shitting","skank","slut","son-of-a-bitch","sonofabitch"],
        't' : ["tits", "twat"],
        'v' : ["vagina", "vaginal"],
        'w' : ["wank","wanker","whore"]
    }
    
    output_numpy = predict([message])
    check_profanity_output = bool(output_numpy[0])
    if check_profanity_output:
        print("\tExplicit = TRUE; profanity_check() determinite")
        return True
    
    else:
        message = message.lower()
        split_message = message.split()
        for word in split_message:
            if(word[0] in "abcdfghjmnprstvw"):
                if(word in profanity_dict[word[0]]):
                    print("\tExplicit = TRUE; Blacklisted Word:", word)
                    return True
                
    return False