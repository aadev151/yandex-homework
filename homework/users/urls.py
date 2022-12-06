from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from users import forms, views


app_name = 'users'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path(
        'users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'
    ),
    path(
        'profile/', login_required(views.ProfileView.as_view()), name='profile'
    ),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='users/login.html',
            authentication_form=forms.BootstrapLoginForm,
            extra_context={'btn_name': 'Вход'},
        ),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout',
    ),
    path(
        'password/change/',
        auth_views.PasswordChangeView.as_view(
            template_name='users/form.html',
            form_class=forms.BootstrapPasswordChangeForm,
            success_url=reverse_lazy('users:password_change_done'),
            extra_context={
                'page_name': 'Смена пароля',
                'btn_name': 'Сменить пароль',
            },
        ),
        name='password_change',
    ),
    path(
        'password/change/done/',
        auth_views.PasswordChangeView.as_view(
            template_name='users/password_change_done.html'
        ),
        name='password_change_done',
    ),
    path(
        'password/reset/',
        auth_views.PasswordResetView.as_view(
            template_name='users/form.html',
            email_template_name='users/emails/password_reset.html',
            form_class=forms.BoostrapPasswordResetForm,
            success_url=reverse_lazy('users:password_reset_done'),
            extra_context={
                'page_name': 'Сброс пароля',
                'btn_name': 'Отправить письмо',
            },
        ),
        name='password_reset',
    ),
    path(
        'password/reset/sent/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'
        ),
        name='password_reset_done',
    ),
    path(
        'password/reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/form.html',
            form_class=forms.BootstrapPasswordResetConfirmForm,
            success_url=reverse_lazy('users:password_reset_complete'),
            extra_context={
                'page_name': 'Сброс пароля',
                'btn_name': 'Сбросить пароль',
            },
        ),
        name='password_reset_confirm',
    ),
    path(
        'password/reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'
        ),
        name='password_reset_complete',
    ),
]
