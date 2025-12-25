from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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
    