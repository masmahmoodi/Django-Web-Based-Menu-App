from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.
 

def index(request):
    items = Item.objects.all()
    
    context = {
        "items":items
    }
    
    return render(request,"food/index.html",context)


class Index(ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = "items"

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context ={
        "item":item
    }
    
    return render(request,"food/detail.html",context)


    
class Detail(DetailView):
    model = Item
    template_name = "food/detail.html"
    context_object_name ="item"    
    
    
    
    
# def create_item(request):
#     form = ItemForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.user_name = request.user
#             item.save()
#             return redirect('food:index')
#     else:
#         form = ItemForm()

#     return render(request, "food/forms.html", {'form': form})    
   
# def create_item(request):
#     form = ItemForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#     return render(request,"food/forms.html",{'form':form})


class CreateItem(CreateView):
    model = Item
    fields =['item_name','item_desc','item_price','itme_image']
    template_name = "food/forms.html"
    def form_valid(self,form): 
        form.instance.user_name = self.request.user
        return super().form_valid(form)


    

def edit_item(request,item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None , instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,"food/forms.html", {"form":form})


def delete_item(request,item_id):
    item = Item.objects.get(id=item_id)
    if request.method == "POST":
        item.delete()
        return redirect("food:index")
    return render(request,"food/delete_item.html",{'item':item})