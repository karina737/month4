
from django.shortcuts import render, get_object_or_404
from clothes.models import ClothesModel, Brand
from django.views import generic

class AllClothesView(generic.ListView):
    template_name='clothes/clothes.html'
    context_object_name='clothes'
    
    def get_queryset(self):
        return ClothesModel.objects.all()
    
class TFClothesView(generic.ListView):
    template_name= 'clothes/tom_ford_clothes.html'
    context_object_name='clothes'
    
    def get_queryset(self):
        return ClothesModel.objects.filter(
            brands_name__name="Tom Ford"
        ).distinct()

class MMClothesView(generic.ListView):
    template_name= 'clothes/miu_miu_clothes.html'
    context_object_name='clothes'
   
    def get_queryset(self):
        return ClothesModel.objects.filter(
            brands_name__name="Miu Miu"
        ).distinct()

# def all_clothes(request):
#     if request.method == "GET":
#         clothes = ClothesModel.objects.all().order_by("-id")
#     return render(
#             request,
#             template_name='clothes/clothes.html',
#             context={
#                 'clothes': clothes
#             }
#         )

# def tom_ford_clothes_views(request):
#       if request.method == "GET":
#         clothes = ClothesModel.objects.filter(brands_name__name="Tom Ford").distinct()
#       return render(
#         request,
#         template_name='clothes/tom_ford_clothes.html',
#         context={
#             'clothes': clothes
#             }
#         )
      
      
# def miu_miu_clothes_views(request):
#       if request.method == "GET":
#         clothes = ClothesModel.objects.filter(brands_name__name="Miu Miu").distinct()
#       return render(
#         request,
#         template_name='clothes/miu_miu_clothes.html',
#         context={
#             'clothes': clothes
#             }
#         )
