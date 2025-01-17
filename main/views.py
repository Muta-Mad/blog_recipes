from django.shortcuts import get_object_or_404, render, redirect
from .forms import RecipeForm
from .models import Recipe


def recipe_create(request, pk=None):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main:list')
      
    else:
        form = RecipeForm()
    context = {'form': form}
    return render(request, 'main/recipes_create.html', context)


def recipes_list(request):
    recipe = Recipe.objects.all()
    context = {'recipe': recipe}
    return render(request, 'main/recipes_list.html', context)


def recipes_detail(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    context = {'recipe': recipe}
    return render(request, 'main/recipes_detail.html', context)