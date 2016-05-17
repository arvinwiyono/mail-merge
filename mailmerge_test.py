import unittest
from mailmerge import *

class MailMergeTest(unittest.TestCase):

	def setUp(self):
		self.scalar = "$(DANCER) was in $(FILM). $(DANCER) is a dancer."
		self.dict = {'DANCER':'Ginger Rogers', 'FILM':'The Martian'}
		self.loop = "$FOR(DANCELIST, \"$(STEP)$(DANCER)\")"


	def test_fill_template_with_result(self):
		self.assertEqual(fill_template(self.scalar, self.dict), "Ginger Rogers was in The Martian. Ginger Rogers is a dancer.")

	# def test_fill_template_with_error(self):
	# 	temp = {'DANCER':'Ginger Rogers'}
	# 	self.assertEqual(fill_template(self.scalar, temp), "The Ginger Rogers is playing in The Martian")

	def test_is_scalar_returns_true_1(self):
		self.assertTrue(is_scalar("(DANCER"))

	def test_is_scalar_returns_true_2(self):
		self.assertTrue(is_scalar("(A"))

	def test_is_scalar_returns_false_1(self):
		self.assertFalse(is_scalar(""))

	def test_is_scalar_returns_false_2(self):
		self.assertFalse(is_scalar("F"))

	def test_translate_scalar(self):
		temp = {"fgh":"test"}
		self.assertEqual(translate_scalar("(fgh) ijk", **temp), "test ijk")

	def test_translate_scalar_with_error(self):
		temp = {}
		with self.assertRaises(KeyError) as raises: 
			translate_scalar("(fgh) ijk", **temp)
		self.assertEqual(str(raises.exception), '\'fgh\'')


if __name__ == '__main__':
	unittest.main()