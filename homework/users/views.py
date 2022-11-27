from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.dateformat import DateFormat

from users.forms import UpdateProfileForm, UpdateUserForm, SignupForm
from users.models import Profile


def signup(request):
    if request.user.is_authenticated:
        return redirect(reverse('users:profile'))

    template = 'users/signup.html'
    form = SignupForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = User.objects.create_user(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password')
        )
        Profile.objects.create(user=user)
        return redirect(reverse('users:profile'))

    context = {
        'form': form,
    }

    return render(request, template, context)


def user_list(request):
    template = 'users/user_list.html'
    context = {
        'users': User.objects.filter(is_active=True),
    }

    return render(request, template, context)


def user_detail(request, id):
    template = 'users/user_detail.html'
    context = {
        'user_': User.objects.get(id=id),
    }

    return render(request, template, context)


@login_required
def profile(request):
    template = 'users/user_profile.html'
    initial_user_data = {
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    }
    initial_birthday_data = {}
    if request.user.profile.birthday:
        initial_birthday_data['birthday'] = DateFormat(
            request.user.profile.birthday
        ).format('Y-m-d')

    user_form = UpdateUserForm(
        request.POST or None,
        initial=initial_user_data,
        instance=request.user
    )
    birthday_form = UpdateProfileForm(
        request.POST or None,
        initial=initial_birthday_data,
        instance=request.user.profile
    )

    if (request.method == 'POST'
            and user_form.is_valid() and birthday_form.is_valid()):

        user_form.save()
        birthday_form.save()

        return redirect('users:profile')

    context = {
        'user_form': user_form,
        'birthday_form': birthday_form,
    }

    return render(request, template, context)
