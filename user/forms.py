from django import forms
from .models import UMessage
from ckeditor.fields import RichTextField

class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password",widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "Username")
    password = forms.CharField(max_length=20,label = "Password",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="Confirm Password",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords Do Not Match")

        values = {
            "username" : username,
            "password" : password
        }
        return values

class ContactForm(forms.Form):
    Name = forms.CharField(max_length = 50,label = "Your Name",required=True)
    Email = forms.EmailField(max_length=30,label = "Your Email Address",required=True)
    Message = forms.CharField(required=True, widget=forms.Textarea, max_length=1000,label ="Describe what you want to contact us for here")
    class Meta:
        model = UMessage
        fields = ('Name', 'Email', 'Message')
