'''
FIT4004 - Assigment 3
Simple mail merge facility for automatically generating email messages and sending the perrsonalized messages to a group of recipients.

@author: Wanyu Yin & Arvin Wiyono
@version: 1.0
@date: 17-05-2016
'''
import re
from string import Template

def fill_template(template, subvars):
	'''
	template: Python string that can contain two macro forms.
	subvars: Python dictionary which contains key-value pairs, with key is the macro name and value is the macro replacement.
	'''
	strings = template.split("$")
	output = ""
	for string in strings:
		if is_scalar(string):
			output += translate_scalar(string, subvars)
		else:
			output += string
	return output


def is_scalar(string):
	if (len(string) > 0) and (string[0] == '('):
		return True
	return False

def translate_scalar(input_string, word_hash):
	translation = str.maketrans("()", "{}")
	input_string = "$" + input_string.translate(translation)
	t = Template(input_string)
	return t.substitute(word_hash)
