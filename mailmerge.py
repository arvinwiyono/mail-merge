'''
FIT4004 - Assigment 3
Simple mail merge facility for automatically generating email messages and sending the perrsonalized messages to a group of recipients.

@author: Wanyu Yin & Arvin Wiyono
@version: 1.0
@date: 17-05-2016
'''
import re

def fill_template(template, subvars):
	'''
	template: Python string that can contain two macro forms.
	subvars: Python dictionary which contains key-value pairs, with key is the macro name and value is the macro replacement.
	'''
	return template + ' ' + subvars['DANCER']

def parse_scalar_macro(template):
	parse_result = re.findall('\$\((\w+)\)', template)
	return parse_result