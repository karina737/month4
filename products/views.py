from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from products.models import Products

def products(request):
     if request.method== 'GET':
         products=Products.objects.all()
     return render(
         request,
         template_name='products_list.html',
         context={
             'products': products
         }
     )

def products_detail(request, id):
    if request.method== 'GET':
        products_id=get_object_or_404(Products, id=id)
    return render(
         request,
         template_name='products_detail.html',
         context={
             'products_id': products_id
         }
     )
        
    

def top_5_food_korea(request):
    if request.method== 'GET':
        return HttpResponse("""
Топ-5 популярных продуктов питания в Корее:
1. Кимчи
2. Пибимпаб
3. Ттокпокки
4. Кимбап
5. Булгоги
""")
        
def timestamp(request):
    if request.method== 'GET':
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"Текущее время: {now}")
       
    
    
def about_me(request):
    if request.method== 'GET':
        return HttpResponse('<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSByvCXPbeUxSKVj89NcnzcQ08_cibB5vasXg&s"><p>Меня зовут Карина, моя жизнь посвящена авиации и самолетам</p>')
    