from user_class import user
import text2emotion as te
import clean_message_script
import profanity_check_script

def get_user_info(csvreader):
   user_dict = {}
   csvreader.__next__()
   
   count = 0
   
   for line in csvreader:
        
        count += 1
        
        #Blacklist Lines Commented Out 11/30/2021 since the new profanity_check script
        #was just implemented :)
        
        #blackList from here: https://github.com/web-mech/badwords/blob/master/lib/lang.json
        #blackList = {"ahole", "anus", "ash0le", "ash0les", "asholes", "ass", "Ass Monkey", "Assface", "assh0le", "assh0lez", "asshole", "assholes", "assholz", "asswipe", "azzhole", "bassterds", "bastard", "bastards", "bastardz", "basterds", "basterdz", "Biatch", "bitch", "bitches", "Blow Job", "boffing", "butthole", "buttwipe", "c0ck", "c0cks", "c0k", "Carpet Muncher", "cawk", "cawks", "Clit", "cnts", "cntz", "cock", "cockhead", "cock-head", "cocks", "CockSucker", "cock-sucker", "crap", "cum", "cunt", "cunts", "cuntz", "dick", "dild0", "dild0s", "dildo", "dildos", "dilld0", "dilld0s", "dominatricks", "dominatrics", "dominatrix", "dyke", "enema", "f u c k", "f u c k e r", "fag", "fag1t", "faget", "fagg1t", "faggit", "faggot", "fagg0t", "fagit", "fags", "fagz", "faig", "faigs", "fart", "flipping the bird", "fuck", "fucker", "fuckin", "fucking", "fucks", "Fudge Packer", "fuk", "Fukah", "Fuken", "fuker", "Fukin", "Fukk", "Fukkah", "Fukken", "Fukker", "Fukkin", "g00k", "God-damned", "h00r", "h0ar", "h0re", "hells", "hoar", "hoor", "hoore", "jackoff", "jap", "japs", "jerk-off", "jisim", "jiss", "jizm", "jizz", "knob", "knobs", "knobz", "kunt", "kunts", "kuntz", "Lezzian", "Lipshits", "Lipshitz", "masochist", "masokist", "massterbait", "masstrbait", "masstrbate", "masterbaiter", "masterbate", "masterbates", "Motha Fucker", "Motha Fuker", "Motha Fukkah", "Motha Fukker", "Mother Fucker", "Mother Fukah", "Mother Fuker", "Mother Fukkah", "Mother Fukker", "mother-fucker", "Mutha Fucker", "Mutha Fukah", "Mutha Fuker", "Mutha Fukkah", "Mutha Fukker", "n1gr", "nastt", "nigger;", "nigur;", "niiger;", "niigr;", "orafis", "orgasim;", "orgasm", "orgasum", "oriface", "orifice", "orifiss", "packi", "packie", "packy", "paki", "pakie", "paky", "pecker", "peeenus", "peeenusss", "peenus", "peinus", "pen1s", "penas", "penis", "penis-breath", "penus", "penuus", "Phuc", "Phuck", "Phuk", "Phuker", "Phukker", "polac", "polack", "polak", "Poonani", "pr1c", "pr1ck", "pr1k", "pusse", "pussee", "pussy", "puuke", "puuker", "qweir", "recktum", "rectum", "retard", "sadist", "scank", "schlong", "screwing", "semen", "sex", "sexy", "Sh!t", "sh1t", "sh1ter", "sh1ts", "sh1tter", "sh1tz", "shit", "shits", "shitter", "Shitty", "Shity", "shitz", "Shyt", "Shyte", "Shytty", "Shyty", "skanck", "skank", "skankee", "skankey", "skanks", "Skanky", "slag", "slut", "sluts", "Slutty", "slutz", "son-of-a-bitch", "tit", "turd", "va1jina", "vag1na", "vagiina", "vagina", "vaj1na", "vajina", "vullva", "vulva", "w0p", "wh00r", "wh0re", "whore", "xrated", "xxx", "b!+ch", "bitch", "blowjob", "clit", "arschloch", "fuck", "shit", "ass", "asshole", "b!tch", "b17ch", "b1tch", "bastard", "bi+ch", "boiolas", "buceta", "c0ck", "cawk", "chink", "cipa", "clits", "cock", "cum", "cunt", "dildo", "dirsa", "ejakulate", "fatass", "fcuk", "fuk", "fux0r", "hoer", "hore", "jism", "kawk", "l3itch", "l3i+ch", "masturbate", "masterbat*", "masterbat3", "motherfucker", "s.o.b.", "mofo", "nazi", "nigga", "nigger", "nutsack", "phuck", "pimpis", "pusse", "pussy", "scrotum", "sh!t", "shemale", "shi+", "sh!+", "slut", "smut", "teets", "tits", "boobs", "b00bs", "teez", "testical", "testicle", "titt", "w00se", "jackoff", "wank", "whoar", "whore", "*damn", "*dyke", "*fuck*", "*shit*", "@$$", "amcik", "andskota", "arse*", "assrammer", "ayir", "bi7ch", "bitch*", "bollock*", "breasts", "butt-pirate", "cabron", "cazzo", "chraa", "chuj", "Cock*", "cunt*", "d4mn", "daygo", "dego", "dick*", "dike*", "dupa", "dziwka", "ejackulate", "Ekrem*", "Ekto", "enculer", "faen", "fag*", "fanculo", "fanny", "feces", "feg", "Felcher", "ficken", "fitt*", "Flikker", "foreskin", "Fotze", "Fu(*", "fuk*", "futkretzn", "gook", "guiena", "h0r", "h4x0r", "hell", "helvete", "hoer*", "honkey", "Huevon", "hui", "injun", "jizz", "kanker*", "kike", "klootzak", "kraut", "knulle", "kuk", "kuksuger", "Kurac", "kurwa", "kusi*", "kyrpa*", "lesbo", "mamhoon", "masturbat*", "merd*", "mibun", "monkleigh", "mouliewop", "muie", "mulkku", "muschi", "nazis", "nepesaurio", "nigger*", "orospu", "paska*", "perse", "picka", "pierdol*", "pillu*", "pimmel", "piss*", "pizda", "poontsee", "poop", "porn", "p0rn", "pr0n", "preteen", "pula", "pule", "puta", "puto", "qahbeh", "queef*", "rautenberg", "schaffer", "scheiss*", "schlampe", "schmuck", "screw", "sh!t*", "sharmuta", "sharmute", "shipal", "shiz", "skribz", "skurwysyn", "sphencter", "spic", "spierdalaj", "splooge", "suka", "b00b*", "testicle*", "titt*", "twat", "vittu", "wank*", "wetback*", "wichser", "wop*", "yed", "zabourah"}
        
        cleanedMessg = clean_message_script.clean_message(line[3])
        
        ##print(line[0])
        message =  te.get_emotion(cleanedMessg)
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

           if(profanity_check_script.check_profanity(cleanedMessg) == True):
                user_dict[line[2]].profane_messages += 1
        else:
            user_dict[line[2]] = user(1, 0, angryMessage, happyMessage, sadMessage, surprisedMessage, fearMessage)
            if(profanity_check_script.check_profanity(cleanedMessg) == True):
                user_dict[line[2]].profane_messages += 1

#if predict(line[3]):
            #user_dict[line[2]].profane_messages += 1
                
        print("Processed Message", count, "/ 17546")
   return user_dict
