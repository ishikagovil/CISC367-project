profanity_check_script.py:

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
	(ie. flagging pass as profane since it contains 'ass')

	There are commented out print commands, which are helpful when trying to see the progress
	of a program when calling check_profanity() over a number of messages.