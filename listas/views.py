from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from listas.models import Item, List
from listas.forms import ItemForm, ExistingListItemForm


def home_page(request):
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()

    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request,
                  'list.html',
                  {
                      'list': list_,
                      "form": form,
                      })


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})
    # try:
    #     item.full_clean()
    #     item.save()
    # except ValidationError:
    #     list_.delete()
    #     error = "You can't have an empty list item"
    #     return render(request, 'home.html', {"error": error})
    # # return redirect(f'/lists/{list_.id}/')
    # return redirect(list_)

    # return redirect(f'/lists/{list_.id}/')

