"""Django views are Python functions that takes http requests and returns http response, like HTML documents.
"""
from django.http import HttpResponse


def home(request):
    """Take an request and shwo it on web page.

    Args:
        request (_type_): Django sends a request to render data on web
    """
    return HttpResponse("<center><h1>This is From Django Web FrameWork</h1></center>")
