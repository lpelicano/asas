from tldextract import extract

class URIToSplitKev():
	def __init__(self, uri_list: list, subdomain=False):
		self.uri_list = uri_list
		self.subdomain = subdomain
		self.new_list = self.check_if_url_list_is_valid()

	def return_new_list(self):
		if self.subdomain:
			return self.create_new_list_subdomains()
		else:
			return self.create_new_list_no_subdomains()

	def create_new_list_subdomains(self):
		return [self.return_subdomain_domain_suffix(i) for i in self.uri_list]

	def create_new_list_no_subdomains(self):
		return [self.return_domain_suffix(i) for i in self.uri_list]

	def return_domain_suffix(self, url: str):
		parsed_url = extract(url)
		return "{parsed_url.domain}.{parsed_url.suffix}".format(parsed_url=parsed_url)

	def return_subdomain_domain_suffix(self, url: str):
		parsed_url = extract(url)
		if parsed_url.subdomain == "" or parsed_url.subdomain == "www":
			subdomain = ""
		else:
			subdomain = "{x.subdomain}.".format(x=parsed_url)
		return "{}{parsed_url.domain}.{parsed_url.suffix}".format(subdomain, parsed_url=parsed_url)

	def check_if_url_list_is_valid(self):
		if len(self.uri_list) == 0:
			return []
		else:
			check = False
			for url in self.uri_list:
				parsed_url = extract(url)
				print(parsed_url.suffix)
				if len(parsed_url.suffix) > 0:
					check = True
				else:
					check = False
					break
			try:
				if check:
					return self.return_new_list()
			except:
				raise ValueError

				  











# class URIToSplit():
# 	def __init__(self, uri_list: list, subdomain=False):
# 		# self.uri = uri
# 		self.subdomain = subdomain
# 		self.uri_list = uri_list
# 		self.new_uri_list = self.new_uri_list

# 	def return_subdomain_domain_suffix(self, url: str):
# 		uri = extract(url)
# 		print("the parsed domain is = {uri.subdomain}.{uri.domain}.{uri.suffix}".format(uri=uri))
		


# 		return "{uri.subdomain}.{uri.domain}.{uri.suffix}".format(uri=uri)

# 	def return_domain_suffix(self, url: str):
# 		uri = extract(url)
# 		print("the parsed domain is = {uri.domain}.{uri.suffix}".format(uri=uri))
# 		return "{uri.domain}.{uri.suffix}".format(uri=uri)

# 	def return_uri_list_of_domain_suffix(self):
# 		new_uri_list = [self.return_domain_suffix(url) for url in self.uri_list]
# 		print(new_uri_list)
# 		return new_uri_list

# 	def return_uri_list_of_subdomain_domain_suffix(self):
# 		new_uri_list = [self.return_subdomain_domain_suffix(url) for url in self.uri_list]
# 		print(new_uri_list)
# 		return new_uri_list

# 	def return_new_domain)_list(self):
# 		if self.subdomain:
# 			return self.return_uri_list_of_subdomain_domain_suffix()
# 		else:
# 			return self.return_uri_list_of_domain_suffix()


