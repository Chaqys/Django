from django import forms


class UserRegister(forms.Form):
    name = forms.CharField(label='Логин', max_length=30)
    balance = forms.IntegerField(label='Депозит')
    age = forms.IntegerField(label='Возраст', max_value=120)
