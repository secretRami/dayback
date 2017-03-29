"""
Integrate custom user model (MyUser) to admin page.
생성한 커스텀 유저 모델(MyUser)을 admin 페이지에 반영한다.

Referred to Django Documentation v1.10
공식문서 참조
https://docs.djangoproject.com/en/1.10/topics/auth/customizing/
"""
from django import forms

from .models import MyUser


class UserCreationForm(forms.ModelForm):
    """
    Modelform for creating users including required fields and repeated passwords.
    필수 필드와 비밀번호를 이용해 이용자를 생성하는 모델폼.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'nickname')

    def clean_password2(self):
        """
        Check if the repeated passwords match.
        입력한 두 비밀번호가 같은지 확인한다.
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("재입력한 비밀번호가 다릅니다.")
        return password2

    def save(self, commit=True):
        """
        Save given password hashed.
        비밀번호를 해쉬로 변환해 저장한다.
        """
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
