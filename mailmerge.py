'''
FIT4004 - Assigment 3
Simple mail merge facility for automatically generating email messages and sending the perrsonalized messages to a group of recipients.

@author: Wanyu Yin & Arvin Wiyono
@version: 1.0
@date: 17-05-2016
'''
import re
from string import Template
import smtplib

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
				raise  MacroNotDefined("'" + key + "'")

			output += translate_loop(macro, subvars[key])

		else:
			output += current
		
		if not processed_as_loop:
			i += 1
			
	return output


def is_scalar(string=""):
	if re.match(r"\(\w+\)", string):
		return True
	return False

def is_loop(string=""):
	if re.match(r"FOR\(\w+", string):
		return True
	return False

def translate_scalar(input_string, word_hash):
	'''
	Substitute the scalar with the value from the word_hash
	'''
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
		raise MacroNotDefined(str(e))

def translate_loop(macro, loop_dicts):
	'''
	Substitute the loop with the value from the loop_dicts dictionary.
	It calls function translate_scalar to substitute each scalar inside the loop
	'''
	macro = macro.replace("(", "$(")
	output = ""
	for ld in loop_dicts:
		output += translate_scalar(macro, ld)
		output += " "
	return output.rstrip()

class MacroNotDefined(Exception):
	def __init__(self, missing_macro):
		Exception.__init__(self, "The macro: " + missing_macro + " is not defined")

class MailMerge():
	def __init__(self, host, username, password, from_address):
		self.host = host
		self.username = username
		self.password = password
		self.from_address = from_address
		
	def build_message(self, to, subject, body):
		message = "\r\n".join([
		 "From: " + self.from_address,
		 "To: " + to,
		 "Subject: " + subject,
		 "",
		 body
		])
		return message
	
	def send_mail(self, to, msg):
		'''
		Start and run the SMTP server to send the messge msg to the email address 
		'''
		server = smtplib.SMTP(self.host)
		server.ehlo()
		server.starttls()
		try:
			server.login(self.username, self.password)
			server.sendmail(self.from_address, to, msg)
		except smtplib.SMTPAuthenticationError:
			raise Exception("Invalid username or password")
		except smtplib.SMTPRecipientsRefused:
			raise Exception("Invalid recipient")
		server.quit()
		return True

	def mailmerge(self, template, subject, subvarlist):
		'''
		Send messages to multiple email addresses
		'''
		output = []
		for dictionary in subvarlist:
			try:
				to = dictionary['to']
				body = fill_template(template, dictionary)
				message = self.build_message(to, subject, body)
				self.send_mail(to, message)
				output.append("Message is successfully sent to " + to)
			except KeyError:
				raise MacroNotDefined("'to'")
			except:
				output.append("Failed to send message to " + to)
		return output

			


		