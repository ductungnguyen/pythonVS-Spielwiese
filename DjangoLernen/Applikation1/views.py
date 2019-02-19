from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Basic view without render.

#def index(request):
#    now=datetime.now()

#    html_content = "<html><head><title>Hello, Django</title></head><body>"
#    html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
#    html_content += "</body></html>"

#    return HttpResponse(html_content)


#2.4: Render a view with a view template
def index(request):
    now = datetime.now()

    return render(
        request,
        "Applikation1/index.html",  # RELATIVE path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'content': '<strong>Hello Django!</strong> on ' + now.strftime("%A, %d %B, %Y at %X"),
            'message': 'Nachricht: '
        }
    )

def about(request):
    return render(
        request,
        "Applikation1/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )