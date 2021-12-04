# CISC367-project

/////////////////////
//   BASIC USAGE   //
/////////////////////

In order to use this script on a set of data, copy the csv into the root of
the project directory. Then, go into driver_script.py and adjust the name
of the input file (LINE 6), to whatever the filename of your dataset is.

It will produce your results in master.csv

The script expects the input CSV to be formatted in the following way:
Thread, Timestamp, Speaker, Message

The first two columns get ignored by the script, so it will not affect the
script to have no data in the Thread and Timestamp columns, so long as there
are blank spaces there so the speaker and message data are in the 3rd and
4th columns respectively.




==================
authors_script.py:
==================

This script uses csvreader to go through the csv file and check who the author
is for each message. Once the author is obtained it checks the user dictionary
to see if we already have record of the user. If not we create a new entry.

We use clean_message_script to first clean the messsage of code and other things
we dont want to go through text2emotion. We use text2motion on each message to
get the emotional values of each message. And then we calculate the average
emotion the user uses based on the total messages that user has sent and their
current average value for each emotion

Everything is stored on user dictionary and return it

========================
clean_message_script.py:
========================

This script consists of one function, clean_message(message).

Usage:
	import clean_message_script
	clean_message_script.clean_message("SOME TEXT HERE")

Function:
	Calling this function with some 'uncleaned' string as var:message will return
	a new string, with common punctuation, URLs, and emoticons removed from the
	original message.

	It is important to call this function before using either the profanity
	checking functions or emotion analysis functions as not removing punctuation
	and other mesasge features (URLs, etc.) can cause the results of the scripts to
	be off.


================
driver_script.py
================

  This code sole purpose is to take the results which are stored in our user
	dictionary and then to write it to a file, called master.csv

==========================
profanity_check_script.py:
==========================

  This script consists of one function, check_profanity(message).

  Usage:
  	import profanity_check_script
  	profanity_check_script.check_profanity("SOME TEXT HERE")

  Function:
  	Calling this function with some 'cleaned' text as var:message will return
  	a boolean value representing whether there is profanity contained within
  	the input (True) or not (False).

  	The program works by first checking against the results of the profanity_check
  	library, which uses NLP to identify if a message is profane based on the tone
  	in the message. This will result in returning True for messages that are profane,
  	despite not having a word that falls on a blacklist. If the profanity_check library
  	does not believe there to be profanity, we will then check against a team-curated
  	blacklist with words that we believe would automatically deem a message to be profane.
  	It checks the message word-by-word rather than as a whole to avoid false positives
  	(ie. flagging pass as profane since it contains substring 'ass')

  	There are commented out print commands, which are helpful when trying to see the progress
  	of a program when calling check_profanity() over a number of messages.
