import datetime

from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Count

from service.models import KCACustomerDangerousData, Inference


def index(request):
    queryset = Inference.objects.all()
    age = request.GET.get('age')

    try:
        inferences = _get_inference_result(int(age))
    except BaseException:
        return render(request, 'service/index.html', dict(
            all_count=len(queryset),
            today_count=len(queryset.filter(created_at__date=datetime.date.today())),
            ),
        )

    return render(
        request,
        'service/index.html',
        dict(
            all_count=len(queryset),
            today_count=len(queryset.filter(created_at__date=datetime.date.today())),
            inferences=inferences,
            age=age,
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


def _get_inference_result(age: int):
    queryset = KCACustomerDangerousData.objects.exclude(
        affected_area='해당없음',
    )
    if age <= 5:
        queryset = queryset.filter(age__lt=age)
    else:
        queryset = queryset.filter(
            age__gte=age - 5,
            age__lt=age + 5,
        )

    result = dict()
    columns = ['injury_caused', 'injury_item', 'affected_area', 'affected_place']
    for column in columns:
        result[column] = list(
            queryset.values(column).annotate(
                count=Count(column)
            ).order_by(
                '-count'
            )[:5]
        )

    return result
