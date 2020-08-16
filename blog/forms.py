from django import forms

from .models import Post
from .models import CV

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CVForm(forms.ModelForm):

	class Meta:
		model = CV
		fields = ('first_name', 'last_name','address','nationality','phonenumber','email_address','personal_statement','employment_history','academic_achievements','interests','other','references')