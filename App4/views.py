from django.shortcuts import render

# Create your views here.

def index(request) :
    my_dict ={'insert_content':"Hello I am Saksham"}
    return render(request,"index.html",my_dict)
