from django.utils.dateformat import DateFormat
from django.views.generic import FormView, ListView, DetailView

from users.forms import UpdateUserForm, SignupForm
from users.models import User


class SignupView(FormView):
    form_class = SignupForm
    template_name = 'users/signup.html'
    success_url = '/profile/'

    def form_valid(self, form):
        User.objects.create_user(
            email=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password'),
        )
        return super().form_valid(form)


class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/user_list.html'


class UserDetailView(DetailView):
    model = User
    context_object_name = 'user_'
    template_name = 'users/user_detail.html'


class ProfileView(FormView):
    form_class = UpdateUserForm
    template_name = 'users/user_profile.html'
    success_url = '/profile/'

    def get_initial(self):
        initial = super().get_initial()
        initial['email'] = self.request.user.email
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name

        if self.request.user.birthday:
            initial['birthday'] = DateFormat(
                self.request.user.birthday
            ).format('Y-m-d')

        return initial

    def get_form(self):
        form = super().get_form()
        form.initial = self.get_initial()
        form.instance = self.request.user
        return form

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
