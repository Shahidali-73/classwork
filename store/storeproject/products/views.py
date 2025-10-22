from django.http import JsonResponse

def product_list(request):
    products = [
        {"name": "Laptop", "price": 75000, "category": "Electronics"},
        {"name": "Chair", "price": 2500, "category": "Furniture"},
        {"name": "Shoes", "price": 1500, "category": "Fashion"},
        {"name": "Book", "price": 500, "category": "Stationery"},
    ]
    return JsonResponse(products, safe=False)
