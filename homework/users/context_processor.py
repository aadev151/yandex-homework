import datetime

from .models import User as Profile


def getting_birthday_today(request):
    birthday_today = Profile.objects.filter(
        birthday__day=datetime.date.today().day,
        birthday__month=datetime.date.today().month,
    ).only("email", "first_name")
    return locals()
