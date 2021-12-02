This script uses csvreader to go through the csv file and check who the author is for each message. Once the author is obtained it checks the user dictionary
to see if we already have record of the user. If not we create a new entry. 

We use clean_message_script to first clean the messsage of code and other things we dont want to go through text2emotion
We use text2motion on each message to get the emotional values of each message. And then we calculate the average emotion the user uses based on the total 
messages that user has sent and their current average value for each emotion

Everything is stored on user dictionary and return it
