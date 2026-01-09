from django.shortcuts import render, redirect, get_object_or_404
from basket.forms import BasketForms
from basket.models import Basket

def create_basket_view(request):
    if request.method == 'POST':
        form = BasketForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/basket_list/')
    else:
        form = BasketForms()
    return render(
        request,
        template_name='basket/create_basket.html',
        context={"form": form}
    )

def read_basket_view(request):
    if request.method == 'GET':
        basket = Basket.objects.all()
    return render(request, template_name='basket/basket_list.html',
                  context={'basket': basket})


def update_basket_view(request, id):
    product_id = get_object_or_404(Basket, id=id)
    if request.method == 'POST':
        form = BasketForms(request.POST, instance=product_id)
        if form.is_valid():
            form.save()
            return redirect('/basket_list/')
    else:
        form = BasketForms(instance=product_id)
    return render(request,
                  template_name='basket/update_basket.html',
                  context={
                      'form': form,
                      'product_id': product_id
                    }
                  )

def delete_basket_view(request, id):
    product_id = get_object_or_404(Basket, id=id)
    product_id.delete()
    return redirect('/basket_list/')