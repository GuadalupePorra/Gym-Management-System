from django.http import JsonResponse

def your_view_function(request):
    return JsonResponse({'message': 'Hello, this is the API response!'})
