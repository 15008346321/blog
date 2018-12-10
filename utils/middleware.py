from typing import re

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from backweb.models import TokenUser, MyUser


class LoginStatusMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print('test1 request')
        # 在访问登录和注册的时候不需要做一下的登录校验功能

        # if re('/web/*', request.path):
        #     return None
        #
        # if request.path == '/':
        #     return

        if request.path in ['/backweb/index/']:
            user_id = request.session.get('user_id')
            if user_id:
                # 向request.user中赋值,赋值为当前的登录系统的用户对象
                user = MyUser.objects.get(pk=user_id)
                request.user = user
                return None
            else:
                return HttpResponseRedirect('/backweb/login/')
        else:
            return None
