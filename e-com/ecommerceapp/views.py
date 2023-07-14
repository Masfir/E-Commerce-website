from django.shortcuts import render
from .models import Contact,Category,Product,ProductRelatedImage
from django.contrib import messages
# from math import ceil
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 2)  # Show 2 product_list per page.
    page_number = request.GET.get("page")
    product_view = paginator.get_page(page_number)
        
    # allProds = []
    # catprods = Product.objects.values('category','id')
    # #print(catprods)
    # cats = {item['category'] for item in catprods}
    # for cat in cats:
    #     prod = Product.objects.filter(category=cat)
    #     n = len(prod)
    #     nSlides = n//4 + ceil((n/4)-(n//4))
    #     allProds.append([prod, range(1,nSlides),nSlides]) 
               
    context = {
        'product_view' : product_view
    }
    return render(request,"index.html",context)

def product_details(request,id):
    product_detail = Product.objects.get(id=id)
    product_related_image = ProductRelatedImage.objects.filter(related_img = product_detail)
    context = {
        'product_detail': product_detail,
        'product_related_image': product_related_image
    }
    return render(request,"product.html",context)

def category_wise_product(request,id):
    category_obj = Category.objects.get(id=id)
    cat_filter_product = Product.objects.filter(category=category_obj)
    
    context = {
    'product_view' : cat_filter_product 
    }
    return render(request,"index.html",context)

def product_search(request):
    get_search_item=request.GET.get('search_item')
    search_product_view=Product.objects.filter(product_name__icontains = get_search_item)
    context = {
        'search_product_view' : search_product_view
    }
    return render(request,"search_product.html",context)

def product_price_search(request):
    get_min_price=request.GET.get('min_price')
    get_max_price=request.GET.get('max_price')
    search_product_view=Product.objects.filter(price__range = (get_min_price,get_max_price))
    context = {
        'search_product_view' : search_product_view
    }
    return render(request,"search_product.html",context)
    
    
    
def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_email = request.POST.get('email')
        get_description = request.POST.get('desc')
        get_phonenumber = request.POST.get('phonenumber')        
        myuser = Contact(name = get_name, email = get_email, desc= get_description, phonenumber = get_phonenumber)
        myuser.save()
        messages.info(request, "We will reply you soon....")
    return render(request,"contact.html")


