from django import forms


# create form that takes a bunch of urls
class URIForm(forms.Form):
	uri = forms.CharField(widget=forms.Textarea)
	subdomain = forms.BooleanField(default=False,required=False)

	def clean(self):
		cleaned_data = super(URIForm, self).clean()
		uri = cleaned_data.get('uri')
		subdomain = cleaned_data.get('subdomain')
		if not uri:
			raise forms.ValidationError("URL input cannot be None")
		if not subdomain:
			raise forms.ValidationError("Subdomain must be false or true")
