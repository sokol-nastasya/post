from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'size': '155'}))
	descriptions = forms.CharField(widget = forms.Textarea(
		attrs = {
		'class': 'form-control'
		}))
	class Meta:
		model = Post
		fields = ('title', 'descriptions',)
