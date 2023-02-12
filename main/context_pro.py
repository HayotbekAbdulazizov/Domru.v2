from .models import *

def view_all(request):

    print("========")
    print("IP 1: ", request.META.get("REMOTE_ADDR"))
    print("IP 2", request.META.get("HTTP_X_FORWARDED_FOR"))
    print("User Agent", request.META.get("HTTP_USER_AGENT"))
    print("========")

    context = {
        'all_posts_count':Post.objects.all().count(),
        'with_contacts':Post.objects.filter(contacts=True).count(),
        # 'ipaddr': request.META.get('REMOTE_ADDR'),
        # 'ipaddr2':request.META.get('HTTP_X_FORWARDED_FOR'),
        # 'useragent':request.META.get('HTTP_USER_AGENT')
    }
    return context