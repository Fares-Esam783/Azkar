from django.shortcuts import render, get_object_or_404
from .models import Dhikr, Category
from django.shortcuts import redirect
from .forms import DhikrForm

def all_dhikr(request):

    query = request.GET.get("q")   

    if query:
        dhikr_list = Dhikr.objects.filter(text__icontains=query)
    else:
        dhikr_list = Dhikr.objects.all()

    return render(request, "all_dhikr.html", {
        "dhikr": dhikr_list,
        "query": query
    })


def category_list(request):
  categories = Category.objects.all()
  return render(request, "category_list.html", {"categories": categories})


def dhikr_by_category(request, cat_id):
  category = get_object_or_404(Category, id=cat_id)
  dhikr_list = Dhikr.objects.filter(category=category)
  return render(request, "dhikr_by_category.html", 
                {"category": category, "dhikr": dhikr_list})

def dhikr_detail(request, dhikr_id):

    item = Dhikr.objects.get(id=dhikr_id)

    next_item = Dhikr.objects.filter(id__gt=item.id).order_by("id").first()

    prev_item = Dhikr.objects.filter(id__lt=item.id).order_by("-id").first()

    return render(request, "dhikr_detail.html", {
        "item": item,
        "next": next_item,
        "prev": prev_item
    })



def add_dhikr(request):

    if request.method == "POST":
        form = DhikrForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("all_dhikr")

    else:
        form = DhikrForm()

    return render(request, "add_dhikr.html", {"form": form})

def edit_dhikr(request, dhikr_id):
    
    dhikr = Dhikr.objects.get(id=dhikr_id)

    if request.method == "POST":
        form = DhikrForm(request.POST, instance=dhikr)

        if form.is_valid():
            form.save()
            return redirect("dhikr_detail", dhikr_id)

    else:
        form = DhikrForm(instance=dhikr)

    return render(request, "edit_dhikr.html", {"form": form})

def delete_dhikr(request, dhikr_id):

    dhikr = Dhikr.objects.get(id=dhikr_id)

    dhikr.delete()

    return redirect("all_dhikr")
