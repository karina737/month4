
from django.shortcuts import render
from clothes.models import ClothesModel, Brand

def all_clothes(request):
    if request.method == "GET":
        clothes = ClothesModel.objects.all().order_by("-id")
    return render(
            request,
            template_name='clothes/clothes.html',
            context={
                'clothes': clothes
            }
        )

def tom_ford_clothes_views(request):
      if request.method == "GET":
        clothes = ClothesModel.objects.filter(brands_name__name="Tom Ford").distinct()
      return render(
        request,
        template_name='clothes/tom_ford_clothes.html',
        context={
            'clothes': clothes
            }
        )
      
      
def miu_miu_clothes_views(request):
      if request.method == "GET":
        clothes = ClothesModel.objects.filter(brands_name__name="Miu Miu").distinct()
      return render(
        request,
        template_name='clothes/miu_miu_clothes.html',
        context={
            'clothes': clothes
            }
        )
