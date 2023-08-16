import datetime

from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.
from service.models import KCACustomerDangerousData, Inference


def index(request):
    queryset = Inference.objects.all()
    age = request.GET.get('age')
    result = dict()

    return render(
        request,
        'service/index.html',
        dict(
            all_count=len(queryset),
            today_count=len(queryset.filter(created_at__date=datetime.date.today())),
            result=result,
        ),
    )


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
            page_numbers=posts.paginator.get_elided_page_range(page)
        )
    )
