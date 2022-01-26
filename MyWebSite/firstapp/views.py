from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def heloo(request):
    text = """<h1>Welcome</h1>"""

    return HttpResponse(text)


def index(request):
    return HttpResponse("""<h1>Welcome to main page</h1>""")


def about(request):
    return HttpResponse("""<h1>About us:</h1>""")

def contact(request):
    return HttpResponse("""<h1>Contact us:</h1>""")
