from django.views.generic import TemplateView


class Description(TemplateView):
    template_name = 'about/index.html'
