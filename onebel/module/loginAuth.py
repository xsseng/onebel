# -*- coding: UTF-8 -*-
#权限控制
from flask import session, redirect

def loginAuth(func):
    def inner(*args,**kwargs):
        if not session.get('isLogin'):
            return redirect('/admin/login')
        return func(*args,**kwargs)
    return inner