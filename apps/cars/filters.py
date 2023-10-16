from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.serializers import ValidationError
from apps.cars.models import CarModel

def car_filtered_queryset(query:QueryDict)->QuerySet:
    qs = CarModel.objects.all()

    for k,v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case 'price_gte':
                qs = qs.filter(price__gte=v)
            case 'price_lte':
                qs = qs.filter(price__lte=v)
            case 'seats_gt':
                qs = qs.filter(seats__gt=v)
            case 'seats_lt':
                qs = qs.filter(seats__lt=v)
            case 'seats_gte':
                qs = qs.filter(seats__gte=v)
            case 'seats_lte':
                qs = qs.filter(seats__lte=v)
            case 'engine_volume':
                qs = qs.filter(engine_volume__exact=v)
            case 'body_type_start':
                qs = qs.filter(body_type__startswith=v)
            case 'body_type_end':
                qs = qs.filter(body_type__endswith=v)
            case 'body_type':
                qs = qs.filter(body_type__contains=v)
            case 'brand_start':
                qs = qs.filter(brand__startswith=v)
            case 'brand_end':
                qs = qs.filter(brand__endswith=v)
            case 'brand':
                qs = qs.filter(brand__contains=v)
            case 'order_by_brand':
                qs = qs.order_by('brand')
            case '-order_by_brand':
                qs = qs.order_by('-brand')
            case 'order_by_price':
                qs = qs.order_by('price')
            case '-order_by_price':
                qs = qs.order_by('-price')
            case 'order_by_body_type':
                qs = qs.order_by('body_type')
            case '-order_by_body_type':
                qs = qs.order_by('-body_type')
            case 'order_by_engine_volume':
                qs = qs.order_by('engine_volume')
            case '-order_by_engine_volume':
                qs = qs.order_by('-engine_volume')
            case 'order_by_seats':
                qs = qs.order_by('seats')
            case '-order_by_seats':
                qs = qs.order_by('-seats')
            case _:
                raise ValidationError({'not allowed'})
    return qs