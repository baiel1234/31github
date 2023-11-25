from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def detail(request, world_id):
    return HttpResponse("You're looking at world %s." % world_id)


def results(request, world_id):
    response = "You're looking at the results of world %s."
    return HttpResponse(response % world_id)


def vote(request, world_id):
    return HttpResponse("You're voting on world %s." % world_id)