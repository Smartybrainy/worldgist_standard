from django.shortcuts import render


def index_view(request):
    map_access_token = 'pk.eyJ1Ijoic21hcnR5YnJhaW55IiwiYSI6ImNrZzdzemh3dzBhZGUycW52MXFkemsyaXAifQ.VVUcjKN3yEwtVYM6TqCgdA'
    context = {
        'map_access_token': map_access_token,
    }
    return render(request, 'core/index.html', context)
