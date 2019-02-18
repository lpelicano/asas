from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from tools.forms import URIForm


def uri_to_domain_view(request):
	if request.method == "POST":
		form = URIForm(request.POST)
		if form.is_valid():
			x = request.POST['uri'].splitlines()
			print(type(x))


			# print(type(x.splitlines()))
			# print(x.splitlines())

			messages.success(request, message=x)
			# print(request.POST['uri'])
		return redirect("/tools/url-to-domain/", {"urls": x,})

	else:
		form = URIForm()

	context = {
		"form": form,
	}

	return render(request, 'screens/tools/uri_to_domain.html', context)