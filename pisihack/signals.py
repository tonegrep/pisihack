from allauth.socialaccount.signals import pre_social_login
from django.core.signals import request_finished

def test_this(sender, **kwargs):
    print(sender)
    print('----')

    print(kwargs)


pre_social_login.connect(test_this)
request_finished.connect(test_this)
print('signalsdffwssfsdfg')
