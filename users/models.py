from django.db import models
import requests
from django.contrib.auth.models import AbstractUser


from allauth.socialaccount.signals import pre_social_login

class PisiUser(AbstractUser):
    pass

def test_this(sender, **kwargs):
    print(sender)
    print('----')

    token = kwargs['sociallogin'].token
    print("Token:", token)
    print('client_id=Iv1.28217937759dad51&client_secret=1c4757f1bd8ad67bf76c8367014a9da0746c66f9&code={0}'.format(
        token))
    xd = requests.post(url='https://github.com/login/oauth/access_token',
                       data='client_id=Iv1.28217937759dad51&client_secret=1c4757f1bd8ad67bf76c8367014a9da0746c66f9&code={0}&redirect_uri=http://127.0.0.1:8000/accounts/github/login/callback/'.format(
                           token))

    print(xd.content)


pre_social_login.connect(test_this)
print('signalsdffwssfsdfg')
