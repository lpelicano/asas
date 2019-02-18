from django import forms


# create form that takes a bunch of urls
class URIForm(forms.Form):
	uri = forms.CharField(widget=forms.Textarea)

	def clean(self):
		cleaned_data = super(URIForm, self).clean()
		uri = cleaned_data.get('uri')
		if not uri:
			raise forms.ValidationError("URL input cannot be None")
