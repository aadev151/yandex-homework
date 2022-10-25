from django.http import HttpResponse


def description(request):
    return HttpResponse(
        '<h1>This is an about page</h1>'
        '<h2>Cool, isn\'t it?</h2>'
        '<p><a href="/">Back to the homepage</a></p>'
    )
