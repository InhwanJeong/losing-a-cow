import uuid

from django.db import models


class User(models.Model):
    class Meta:
        verbose_name = '사용자'

    id = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4,
    )


class Inference(models.Model):
    class Meta:
        verbose_name = '추론기능 이용자'

    user = models.ForeignKey(
        to='User',
        verbose_name='사용자',
        on_delete=models.SET_NULL,
        null=True,
    )

    age = models.IntegerField(
        verbose_name='입력 연령',
    )

    created_at = models.DateTimeField(
        verbose_name='생성시각',
        auto_now_add=True,
    )


class KCACustomerDangerousData(models.Model):
    class Meta:
        verbose_name = '한국소비자원 소비자 위해 데이터'

    filing_date = models.DateField(
        verbose_name='접수일',
    )

    age = models.IntegerField(
        verbose_name='연령',
    )

    injury_caused = models.CharField(
        verbose_name='위해 원인',
        max_length=50,
    )

    injury_item = models.CharField(
        verbose_name='위해 품목',
        max_length=50,
    )

    affected_area = models.CharField(
        verbose_name='위해 부위(환부)',
        max_length=50,
    )

    affected_place = models.CharField(
        verbose_name='위해 받은 장소',
        max_length=50,
    )

    created_at = models.DateTimeField(
        verbose_name='생성시각',
        auto_now_add=True,
    )

    removed_at = models.DateTimeField(
        verbose_name='삭제시각',
        null=True,
    )
