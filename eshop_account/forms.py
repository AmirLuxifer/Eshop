from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class EditUserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خود را وارد نمایید', 'class': 'form-control'}),
        label='نام'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'class': 'form-control'}),
        label='نام خانوادگی'
    )


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': ' نام کاربری '}),
        label='نام کاربری'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': ' کلمه عبور '}),
        label='کلمه ی عبور'
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        qs = User.objects.filter(username=user_name)
        if not qs.exists():
            raise forms.ValidationError("این نام کاربری وجود ندارد")
        return user_name


class RegisterForm(forms.Form):
    user_name = forms.CharField(min_length=8, max_length=15, label='نام کاربری', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}))

    password = forms.CharField(min_length=8, label='رمز عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}))

    re_password = forms.CharField(min_length=8, label='رمز عبور خود را دوباره وارد کنید', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را دوباره وارد کنید'}))

    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        qs = User.objects.filter(username=user_name)
        if qs.exists():
            raise forms.ValidationError("این نام کاربری قبلا استفاده شده است")
        return user_name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("این ایمیل قبلا استفاده شده است")
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('لطفا رمز عبور خود را درست وارد کنید')
        return password
