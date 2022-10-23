from django.http import HttpResponse


def item_list(request):
    return HttpResponse(
        '<h1>Catalog of Items</h1>'
        '<h2>Some test links:</h2>'
        '<ol>'
        '   <li><a href="/catalog/1">Item 1</a></li>'
        '   <li><a href="/catalog/2">Item 2</a></li>'
        '   <li><a href="/catalog/3">Item 3</a></li>'
        '   <li><a href="/catalog/999">Item 999</a></li>'
        '   <li><a href="/catalog/ABC">Item ABC</a> (FAKE!)</li>'
        '</ol>'
        '<br><br>'
        '<p><a href="/">Back to the homepage</a></p>'
    )


def item_detail(request, pk):
    return HttpResponse(
        f'<h1>Item {pk}</h1>'
        '<h2>Some info will probably some day be here</h2>'
        '<p><a href="/catalog">Back to the catalog</a></p>'
    )
