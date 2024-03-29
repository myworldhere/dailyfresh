# coding=utf-8
from django.http import HttpResponseRedirect


def login(func):
    """如果未登录则转到登录页面"""
    def login_fun(request, *args, **kwargs):
        if request.session.has_key('user_id'):
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login')
            if request.is_ajax():
                pass
            else:
                red.set_cookie('url', request.get_full_path())
            return red

    return login_fun
