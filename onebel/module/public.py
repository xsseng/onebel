# -*- coding: UTF-8 -*-
#权限控制
from flask import session
from functools import wraps

def user_login_status_check(func):
    """
    校验登录状态
    """
    @wraps(func)
    def wapper(*args, **kwargs):
        # 获取session
        _session = session.get("isLogin", "1")
        # 校验是否登录状态
        if _session:
            return func(*args, **kwargs)
        else:
            return '系统检测到您还未登录，请先登录'
    return wapper

def get_user():
    """
    获取用户名
    """
    return session.get("username")