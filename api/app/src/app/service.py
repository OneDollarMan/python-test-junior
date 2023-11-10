from src.app.models import UserEventModel
from src.init_database import sess
from datetime import datetime


def get_last_5_events():
    return sess.query(UserEventModel).order_by(UserEventModel.date_created.desc()).limit(5)


def create_event(request):
    event = UserEventModel(date_created=datetime.now(), user_ip=get_user_ip(request))
    sess.add(event)
    sess.commit()
    return True


def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def check_user_ip(request):
    abc = '0123456789'
    ip = get_user_ip(request)
    even = 0
    odd = 0
    for ch in ip:
        if ch in abc:
            if int(ch) % 2 == 0:
                even += 1
            else:
                odd += 1
    if even == odd:
        return True
    else:
        return False
