from django import forms

class ValidPhoneForm(forms.Form):
    phone = forms.CharField(label="Введите номер телефона")