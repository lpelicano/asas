from tldextract import extract


class URIToSplit():
	def __init__(self, uri_list: list, subdomain=False):
		# self.uri = uri
		self.subdomain = subdomain
		self.uri_list = uri_list
		self.new_uri_list = self.return_uri_list_of_domain_suffix()

	def return_domain_suffix(self, url: str):
		uri = extract(url)
		print("the parsed domain is = {uri.domain}.{uri.suffix}".format(uri=uri))
		return "{uri.domain}.{uri.suffix}".format(uri=uri)

	def return_uri_list_of_domain_suffix(self):
		new_uri_list = [self.return_domain_suffix(url) for url in self.uri_list]
		print(new_uri_list)
		return new_uri_list



	# def return_subdomain_domain_and_suffix(self):
	# 	pass

	# def check_if_subdomain_true_false(self):
	# 	if self.subdomain:
