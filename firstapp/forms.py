from django import forms


class UserForm(forms.Form):
   name = forms.CharField(label="Имя клиента",
                             widget=forms.TextInput(attrs={"class": "myfield"}))
   age = forms.IntegerField(label="Возраст клиента",
                            widget=forms.NumberInput(attrs={"class": "myfield"}))
# class UserForm(forms.Form):
#    basket = forms.BooleanField(label="Положить товар в корзику")
#
# class UserForm(forms.Form):
#    basket = forms.BooleanField(label="Положить в корзину", required=False)
#
# class UserForm(forms.Form):
#    vyb = forms.NullBooleanField(label="Вы поедете в Сочи этик летом?")
#
# class UserForm(forms.Form):
#    name = forms.CharField(label="Имя клиента", max_length=15, help_text="ФИО не более 15 синволов")
#

