import unittest
from mailmerge import *

class MailMergeTest(unittest.TestCase):

	def setUp(self):
		self.scalar = "$(DANCER) was in $(FILM). $(DANCER) is a dancer."
		self.dict = {'DANCER':'Ginger Rogers', 'FILM':'The Martian'}
		self.loop = "$FOR(DANCELIST, \"$(STEP) mama $(DANCER)\")"


	def test_fill_template_with_result_1(self):
		self.assertEqual(fill_template(self.scalar, self.dict), "Ginger Rogers was in The Martian. Ginger Rogers is a dancer.")

	def test_fill_template_with_result_2(self):
		self.assertEqual(fill_template('$(DANCER)$(FILM)$(FILM)', self.dict), "Ginger RogersThe MartianThe Martian")

	def test_fill_template_with_result_3(self):
		self.assertEqual(fill_template(self.loop, self.dict), "DANCELIST, \"(STEP) mama (DANCER)\"")

	def test_fill_template_with_result_4(self):
		self.assertEqual(fill_template("$FOR(DANCELIST, \"test\")", self.dict), "DANCELIST, \"test\"")

	def test_fill_template_with_result_5(self):
		self.assertEqual(fill_template("$FOR(abc123, \"test$(HELLO)\")", self.dict), "abc123, \"test(HELLO)\"")

	# test is_scalar()
	def test_is_scalar_returns_true_1(self):
		self.assertTrue(is_scalar("(DANCER"))

	def test_is_scalar_returns_true_2(self):
		self.assertTrue(is_scalar("("))

	def test_is_scalar_returns_false_1(self):
		self.assertFalse(is_scalar(""))

	def test_is_scalar_returns_false_2(self):
		self.assertFalse(is_scalar("F"))

	# test is_loop()
	def test_is_loop_returns_true_1(self):
		self.assertTrue(is_loop("FOR( something"))

	def test_is_loop_returns_true_2(self):
		self.assertTrue(is_loop("FOR("))

	def test_is_loop_returns_false_1(self):
		self.assertFalse(is_loop(""))

	def test_is_loop_returns_false_2(self):
		self.assertFalse(is_loop("FO"))

	def test_is_loop_returns_false_3(self):
		self.assertFalse(is_loop("FOR"))

	def test_is_loop_returns_false_4(self):
		self.assertFalse(is_loop("FORA"))

	def test_translate_scalar(self):
		temp = {"fgh":"test"}
		self.assertEqual(translate_scalar("(fgh) ijk", temp), "test ijk")

	def test_translate_scalar_with_error(self):
		temp = {}
		with self.assertRaises(KeyError) as raises: 
			translate_scalar("(fgh) ijk", temp)
		self.assertEqual(str(raises.exception), '\'fgh\'')


if __name__ == '__main__':
	unittest.main()