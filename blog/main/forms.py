from django import forms
from main.models import Main
class MainForm(forms.ModelForm):
    title = forms.CharField(label='標題', max_length=128)
    content = forms.CharField(label='內容', widget=forms.Textarea)
    
    
    class Meta:
        model = Main
        fields = ('title', 'content')