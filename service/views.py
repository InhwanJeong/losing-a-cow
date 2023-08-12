from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'service/index.html')

def kca_list(request):
    return render(request, 'service/kca_list.html')