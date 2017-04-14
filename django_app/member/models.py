"""
Design user information and creation models.
이용자 정보 및 생성 모델 작성.

Referred to Django Documentation v1.10
공식문서 참조
https://docs.djangoproject.com/en/1.10/topics/auth/customizing/
"""

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        """
        Create user using email, nickname and password.
        이메일, 닉네임, 비밀번호를 이용해 이용자를 생성한다.
        """
        if not email:
            raise ValueError('이메일 주소는 필수로 입력하셔야 합니다.')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        """
        Create superuser using email, nickname and password.
        이메일, 닉네임, 비밀번호를 이용해 운영자를 생성한다.
        """
        user = self.create_user(
            email=email,
            nickname=nickname,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True,
    )

    nickname = models.CharField(
        verbose_name='nickname',
        max_length=30,
        blank=False,
        default='user unknown'
    )
    created_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', ]

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.nickname

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """
        User has a specific permission.
        이용자는 특정 권한이 있다.
        """
        return True

    def has_module_perms(self, app_label):
        """
        User has permissions to view 'app_label'.
        이용자는 '앱 이름'을 볼 권한이 있다.
        """
        return True

    @property
    def is_staff(self):
        """
        All admins are staff.
        모든 관리자 계정은 운영자 권한을 갖는다.
        """
        return self.is_admin
