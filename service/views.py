from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.
from service.models import KCACustomerDangerousData


def index(request):
    return render(request, 'service/index.html')


def kca_list(request):
    page = request.GET.get('page', 1)

    queryset = KCACustomerDangerousData.objects.all()
    paginator = Paginator(queryset, 10)

    posts = paginator.get_page(page)

    return render(
        request,
        'service/kca_list.html',
        dict(
            posts=posts,
        )
    )
