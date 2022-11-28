from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.dateformat import DateFormat

from users.forms import UpdateUserForm, SignupForm
from users.models import User


def signup(request):
    if request.user.is_authenticated:
        return redirect(reverse('users:profile'))

    template = 'users/signup.html'
    form = SignupForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        User.objects.create_user(
            email=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password')
        )
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
    initial_data = {
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    }
    if request.user.birthday:
        initial_data['birthday'] = DateFormat(
            request.user.birthday
        ).format('Y-m-d')

    form = UpdateUserForm(
        request.POST or None,
        initial=initial_data,
        instance=request.user
    )

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('users:profile')

    context = {
        'form': form,
    }

    return render(request, template, context)
