from django.shortcuts import render

# Create your views here.

# index
def index(request):
    datas = {
        
    }
    return render(request, "index.html", datas)

# blog
def blog(request):
    datas = {
        
    }
    return render(request, "blog.html", datas)

# detail
def detail(request):
    datas = {
        
    }
    return render(request, "blog-details.html", datas)

# club
def club(request):
    datas = {
        
    }
    return render(request, "club.html", datas)

# contact
def contact(request):
    datas = {
        
    }
    return render(request, "contact.html", datas)

# main
def main(request):
    datas = {
        
    }
    return render(request, "main.html", datas)

# result
def result(request):
    datas = {
        
    }
    return render(request, "result.html", datas)

# schedule
def schedule(request):
    datas = {
        
    }
    return render(request, "schedule.html", datas)
