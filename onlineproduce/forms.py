from django import forms
from onlineproduce.models import customer,Login



class contact(forms.Form):
    name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()
    feedback = forms.CharField(max_length=100,
                              widget=forms.Textarea(attrs={
                               "placeholder" : "Enter your feedback",
                           }))


# login authentication
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = ["username", "email", "password"]

class SigninForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)







