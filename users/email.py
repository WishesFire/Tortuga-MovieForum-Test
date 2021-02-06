from django.views.generic.base import View
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import reverse

User = get_user_model()


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User._default_manager.get(pk=uid)

        except User.DoesNotExists:
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('main-page')
        else:
            return HttpResponse("You don't active your account!")


def create_email_message(request, email_to, user):
    email_subject = 'Activate your acccount'
    current_domain = get_current_site(request).domain
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    link = reverse('activate', kwargs={
                                    'uidb64': uidb64, 'token': token
    })
    activate_link = 'https://' + current_domain + link
    email_body = f'Confirm your email {user.username}. ' \
                 f'Используй эту силку чтобы подтвердить аккаунт свой - {activate_link}'

    email = EmailMessage(email_subject, email_body, to=[email_to])
    email.send(fail_silently=False)