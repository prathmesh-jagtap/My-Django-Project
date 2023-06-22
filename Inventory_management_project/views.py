"""Django views are Python functions that takes http requests and returns http response, like HTML documents.
"""
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string


def home(request):
    """Take an request and shwo it on web page.

    Args:
        request (_type_): Django sends a request to render data on web
    """
    temp = render_to_string("home.html")
    HttpResponse(temp)
