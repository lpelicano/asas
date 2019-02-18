from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from tools.forms import URIForm
from tools.methods import URIToSplitKev






def uri_to_domain_view(request):
	 # register the template filter with django

	if request.method == "POST":
		form = URIForm(request.POST)
		if form.is_valid():
			input_urls = request.POST['uri'].splitlines()
			subdomain_check = request.POST['subdomain']
			print("check this!!!! " + subdomain_check)
			url_parsed_list = URIToSplitKev(input_urls, subdomain_check).new_list
		else:
			url_parsed_list = []
		context = {
			"form": form,
			"urls": url_parsed_list,
		}
		return render(request, 'screens/tools/uri_to_domain.html', context)

	else:
		form = URIForm()

	context = {
		"form": form,
	}

	return render(request, 'screens/tools/uri_to_domain.html', context)