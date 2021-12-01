clean_message_script.py:

This script consists of one function, clean_message(message).

Usage:
	import clean_message_script
	clean_message_script.clean_message("SOME TEXT HERE")

Function:
	Calling this function with some 'uncleaned' string as var:message will return
	a new string, with common punctuation, URLs, and emoticons removed from the
	original message.

	It is important to call this function before using either the profanity 			checking functions or emotion analysis functions as not removing punctuation
	and other mesasge features (URLs, etc.) can cause the results of the scripts to
	be off.