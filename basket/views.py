from django.shortcuts import render, redirect, get_object_or_404
from basket.forms import BasketForms
from basket.models import Basket
from django.views import generic

class CreateBascetView(generic.CreateView):
    template_name = 'basket/create_basket.html'
    form_class = BasketForms
    success_url = '/basket_list/'


    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBascetView, self).form_valid(form=form)
    
class ReadBasketView(generic.ListView):
    template_name = 'basket/basket_list.html'
    
    def get_queryset(self):
        return Basket.objects.all().order_by('-id')


class UpdateBasketView(generic.UpdateView):
    template_name = 'basket/update_basket.html'
    form_class = BasketForms
    success_url = '/basket_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBasketView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(Basket, id=todo_id)

class DeleteBasketView(generic.DeleteView):
    template_name = 'basket/confirm_delete.html'
    success_url = '/basket_list/'


    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(Basket, id=todo_id)


# def create_basket_view(request):
#     if request.method == 'POST':
#         form = BasketForms(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/basket_list/')
#     else:
#         form = BasketForms()
#     return render(
#         request,
#         template_name='basket/create_basket.html',
#         context={"form": form}
#     )

# def read_basket_view(request):
#     if request.method == 'GET':
#         basket = Basket.objects.all()
#     return render(request, template_name='basket/basket_list.html',
#                   context={'basket': basket})


# def update_basket_view(request, id):
#     product_id = get_object_or_404(Basket, id=id)
#     if request.method == 'POST':
#         form = BasketForms(request.POST, instance=product_id)
#         if form.is_valid():
#             form.save()
#             return redirect('/basket_list/')
#     else:
#         form = BasketForms(instance=product_id)
#     return render(request,
#                   template_name='basket/update_basket.html',
#                   context={
#                       'form': form,
#                       'product_id': product_id
#                     }
#                   )

# def delete_basket_view(request, id):
#     product_id = get_object_or_404(Basket, id=id)
#     product_id.delete()
#     return redirect('/basket_list/')