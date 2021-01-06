from django.shortcuts import render

# Create your views here.
def index(request):
    condic = {'text':'hello world', 'number': 100}
    return render(request, 'basicapp/index.html', context=condic)

def other(request):
    return render(request, 'basicapp/other.html')

def relative(request):
    return render(request,'basicapp/relative_url.html')


