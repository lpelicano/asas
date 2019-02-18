from django.test import TestCase

from tools.methods import URIToSplit


class URLToSplitTestCase(TestCase):
	def setUp(self):
		self.uri_list = [
			"https://www.rebootonline.com/asdsadsd",
			"https://rebootonline.com/asdsadsd",
			"rebootonline.com/asdsadsd",
			"www.rebootonline.com/asdsadsd",
			"aspsd.rebootonline.com/asdsadsd",
			"https://wew.easpsd.rebootonline.com/sdsdsd",
			"wew.easpsd.rebootonline.com/sdsdsd"
		]
		self.uri_subdomain_list = [
			"www.rebootonline.com",
			"rebootonline.com",
			"rebootonline.com",
			"www.rebootonline.com",
			"aspsd.rebootonline.com",
			"rebootonline.com",
			"wew.easpsd.rebootonline.com",
			"wew.easpsd.rebootonline.com"
		]
		self.uri_no_subdomain_list = [
			"rebootonline.com",
			"rebootonline.com",
			"rebootonline.com",
			"rebootonline.com",
			"rebootonline.com",
			"rebootonline.com",
			"rebootonline.com",
			"rebootonline.com"
		]

	def test_return_domain_and_suffix(self):
		self.assertEqual(URIToSplit(self.uri_list[0]).domain, "rebootonline.com")
		self.assertEqual(URIToSplit(self.uri_list[1]).domain, "rebootonline.com")
		self.assertEqual(URIToSplit(self.uri_list[2]).domain, "rebootonline.com")
		self.assertEqual(URIToSplit(self.uri_list[3]).domain, "rebootonline.com")
		self.assertEqual(URIToSplit(self.uri_list[4]).domain, "rebootonline.com")
		self.assertEqual(URIToSplit(self.uri_list[5]).domain, "rebootonline.com")
		self.assertEqual(URIToSplit(self.uri_list[6]).domain, "rebootonline.com")

	def test_return_sub_domain_domain_and_suffix(self):
		self.assertEqual(URIToSplit(self.uri_list).new_uri, self.uri_no_subdomain_list)
		# self.assertEqual(self.rebootonline_uri_list, self.uri_subdomain_list)




