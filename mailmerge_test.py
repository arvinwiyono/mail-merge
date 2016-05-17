import unittest
from mailmerge import *

class MailMergeTest(unittest.TestCase):

	def setUp(self):
		self.scalar = "$(DANCER)$(FILM)"
		self.loop = "$FOR(DANCELIST, \"$(STEP)$()\")"
		self.dict = {'DANCER':'Ginger Rogers'}

	def test_fill_template(self):
		concat = self.scalar + ' ' + self.dict['DANCER']
		self.assertEqual(fill_template(self.scalar, self.dict), concat)

	# test parse_scalar_macro
	def test_psm(self):
		self.assertEqual(parse_scalar_macro(self.scalar), ['DANCER', 'FILM'])

	def test_psm_with_empty_input(self):
		self.assertEqual(parse_scalar_macro(''), [])	

	def test_psm_with_ugly_input_1(self):
		self.assertEqual(parse_scalar_macro("$(DANCER)$$$$$    $$$$$$(FILM)"), ['DANCER', 'FILM'])

	def test_psm_with_ugly_input_2(self):
		self.assertEqual(parse_scalar_macro('rqi23y4cpqw flqhwe br123!@#$%^&*('), [])

if __name__ == '__main__':
	unittest.main()