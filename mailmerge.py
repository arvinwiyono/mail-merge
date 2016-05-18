'''
FIT4004 - Assigment 3
Simple mail merge facility for automatically generating email messages and sending the perrsonalized messages to a group of recipients.

@author: Wanyu Yin & Arvin Wiyono
@version: 1.0
@date: 17-05-2016
'''
import re
from string import Template

def fill_template(template="", subvars={}):
	'''
	template: Python string that can contain two macro forms.
	subvars: Python dictionary which contains key-value pairs, with key is the macro name and value is the macro replacement.
	'''
	strings = template.split("$")
	output = ""
	
	i = 0
	while i < len(strings):	
		processed_as_loop = False
		current = strings[i]
		
		if is_scalar(current):
			output += translate_scalar(current, subvars)

		elif is_loop(current):
			processed_as_loop = True
			end_is_found = False
			temp = ""

			while(not end_is_found):
				current = strings[i]
				if '")' in current:
					end_is_found = True
				temp += current
				i += 1

			# exclude the first four letters 'FOR('
			temp = temp[4:-1]
			[key, macro] = temp.split(",")

			# strip off double quote marks
			macro = macro[1:-1]
			if not key in subvars:
				raise  MacroNotDefined("The macro: '" + key + "' is not defined")

			output += translate_loop(macro, subvars[key])

		else:
			output += current
		
		if not processed_as_loop:
			i += 1
			
	return output


def is_scalar(string=""):
	if (len(string) > 0) and (string[0] == '('):
		return True
	return False

def is_loop(string=""):
	if(len(string) >= 4) and (string[0:4] == 'FOR('):
		return True
	return False

def translate_scalar(input_string, word_hash):
	translation = str.maketrans("()", "{}")

	input_string = input_string.translate(translation)

	# To avoid attaching $ to the input given by translate_loop()
	if input_string[0] == '{':
		input_string = '$'+ input_string

	t = Template(input_string)
	try:
		result = t.substitute(word_hash)
		return result
	except KeyError as e:
		raise MacroNotDefined("The macro: " + str(e) + " is not defined")

def translate_loop(macro, loop_dicts):
	macro = macro.replace("(", "$(")
	output = ""
	for ld in loop_dicts:
		output += translate_scalar(macro, ld)
		output += " "
	return output.rstrip()

class MacroNotDefined(Exception):
	pass