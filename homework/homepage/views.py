from django.http import HttpResponse


def home(request):
    return HttpResponse(
        '<h1>It\'s not 404</h1>'
        '<h2>___________</h2>'
        '<p>It\'s a homepage :)'
        '<br>'
        '<a href="/catalog/">Catalog</a>'
        '<br>'
        '<a href="/about/">About</a>'
        '</p>'
    )
