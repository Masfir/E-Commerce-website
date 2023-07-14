from .models import *

def menu(request):
    # menu_item = Category.objects.all()
    menu_item = Category.objects.filter(sub_category=None)
    return dict(menu_item = menu_item)