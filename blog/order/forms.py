from django import forms
from order.models import Order


class OrderForm(forms.ModelForm):
    title = forms.CharField(label='姓名', max_length=128)
    phone = forms.CharField(label='電話', max_length=128)
    paper= forms.CharField(label='紙張種類', max_length=128)
    page = forms.CharField(label='頁數', max_length=128)
    way = forms.CharField(label='裝訂方式', max_length=128)
    content = forms.CharField(label='內容', widget=forms.Textarea)
    
    class Meta:   
        model = Order
        fields = ['title', 'phone', 'paper' , 'page' , 'way'  , 'content']
    #   