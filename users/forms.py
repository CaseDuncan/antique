from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Evaluation , VerificationCode , CustomUser
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
   
    class Meta:
        model = CustomUser
        fields = ['username' , 'email', 'phone_number', 'first_name' , 'last_name' ,'password1' ,'password2']


class EvaluationRequestForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)
    contact_method = forms.ChoiceField(choices=[('phone', 'Phone'), ('email', 'Email')])
    class Meta:
        model = Evaluation
        fields = ['comment', 'contact_method', 'antique_img']
    
    def clean_photo(self):
        antique_img = self.cleaned_data.get('antique_img')

        # Check if a photo is provided
        if not antique_img:
            raise forms.ValidationError("Please upload a photo.")

        # Check the file size 5 MB
        max_size = 5 * 1024 * 1024  
        if antique_img.size > max_size:
            raise forms.ValidationError("File size must be no more than 5 MB.")
        return antique_img
    
class VerificationCodeForm(forms.ModelForm):
    code = forms.CharField(label='code', help_text='enter SMS verification Number')
    class Meta:
        model = VerificationCode
        fields = ['code']