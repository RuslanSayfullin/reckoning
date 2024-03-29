from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from oauth2mailru.utils import get_user_uid
import json
from backend.pymymailru import PyMyMailRu, ApiError
from django.conf import settings
from django.urls import reverse


OAUTH_MAIL_RU_CLIENT_ID = settings.OAUTH_MAIL_RU_CLIENT_ID
OAUTH_MAIL_RU_CLIENT_SECRET = settings.OAUTH_MAIL_RU_CLIENT_SECRET
OAUTH_MAIL_RU_REDIRECT_URI = settings.OAUTH_MAIL_RU_REDIRECT_URI


class MailruOAuthView(View):
    """Класс отвечает за проверку подключения только авторизованных пользователей"""

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        error = request.GET.get('error')
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")

        if error:
            return render(request, 'appmain/login.html', {'error': 'Что то пошло не так. Попробуйте еще раз'})

        if not code:
            return render(request, 'appmain/login.html', {})

        uid = get_user_uid(code)
        if uid is None:
            return render(request, 'appmain/login.html', {'error': '2 Что то пошло не так. Попробуйте еще раз'})

        try:
            my_mail = PyMyMailRu(OAUTH_MAIL_RU_CLIENT_ID, OAUTH_MAIL_RU_CLIENT_SECRET)
            my_info = my_mail.users_get_info(uids=uid, session_key_or_uid=uid)
            my_info = json.loads(my_info)
        except ApiError:
            return render(request, 'appmain/login.html', {'error': 'Что то пошло не так. Попробуйте еще раз'})

        email = my_info[0]["email"]

        try:
            user = User.objects.get(email=email)

            if user.is_active:
                login(request, user, backend='oauth2mailru.auth.backends.MailRuBackend')
                return HttpResponseRedirect("/")

            raise User.DoesNotExist
        except User.DoesNotExist:
            return render(request, 'appmain/login.html',
                          {'error': u'<h4>{0}</h4>Вы не можете зайти <br>У Вас должна быть почта на <i>@re-forma.ru</i>'.format(email)})


def mailru_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("auth:login"))
