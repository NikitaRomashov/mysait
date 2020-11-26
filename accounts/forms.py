from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
   username = forms.CharField(label='Имя пользователя', widget = forms.TextInput(attrs={'class':'myClass'}))
   password = forms.CharField(label='Пароль', widget = forms.PasswordInput(attrs={'class': 'myClass'}))


class UserRegisterForm(UserCreationForm):
   username = forms.CharField(label='Имя пользователя', widget = forms.TextInput(attrs={'class':'myClass'})) #!Для кастомизации формы задается класс
   password1 = forms.CharField(label='Пароль', widget = forms.PasswordInput(attrs={'class': 'myClass'}))
   password2 = forms.CharField(label='Подтверждение пароля', widget = forms.PasswordInput(attrs={'class': 'myClass'}))
   email = forms.EmailField( label='Email',widget=forms.EmailInput(attrs={'class': 'myClass'}))
   first_name = forms.CharField(label = 'Имя', widget= forms.TextInput(attrs={'class': 'myClass'}))
   last_name = forms.CharField(label = 'Фамилия', widget= forms.TextInput(attrs={'class': 'myClass'}))

   class Meta:
      model = User
      fields = ('username','first_name','last_name','email', 'password1', 'password2')
   
   def clean_email(self):
      data = self.cleaned_data['email']
      if User.objects.filter(email=data).exists():
         raise forms.ValidationError("This email already used")
      return data
