from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
                                                            'class': 'form-control',
                                                            'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                                            'class': 'form-control',
                                                            'placeholder': 'password'}))
    remember = forms.BooleanField()

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с ником "{username}" не найден')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("Неверный пароль")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'password', 'remember')


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={
                                                                    'class': 'form-control',
                                                                    'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                                                                    'class': 'form-control',
                                                                    'placeholder': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
                                                                    'class': 'form-control',
                                                                    'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                                                                'class': 'form-control',
                                                                'placeholder': 'confirm password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Данный почтовый адрес уже зарегистрирован в системе')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Ник {username} занят')
        return username

    def clean(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Неправильный пароль!')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email',)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('genre', 'photo',)