

def process_filters(request):
    brand = int(request.GET.get("car_brand_id"))
    year_from = int(request.GET.get("car_year_from"))
    year_to = int(request.GET.get("car_year_to"))
    price_from = request.GET.get("min_price_point")
    price_to = request.GET.get("max_price_point")
    filters = {}
    if brand and brand > 0:
        filters['brand'] = brand
    if year_from and year_from > 0:
        filters['fabrication__gte'] = year_from
    if year_to and year_to > 0:
        filters['fabrication__lte'] = year_to
    if price_from and price_to:
        filters['price__gte'] = price_from
        filters['price__lte'] = price_to

    return filters