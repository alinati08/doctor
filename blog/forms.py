from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'نام شما',
            'email': 'ایمیل',
            'message': 'متن نظر',
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
