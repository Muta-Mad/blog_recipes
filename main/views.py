from django.shortcuts import get_object_or_404, render, redirect
from .forms import RecipeForm
from .models import Recipe

# Create your views here.
def recipe(request, pk=None):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main:list')
        
    else:
        form = RecipeForm()
    context = {'form': form}
    return render(request, 'recipes.html', context)

def recipes_list(request):
    recipe = Recipe.objects.all()
    context = {'recipe': recipe}
    return render(request, 'recipes_list.html', context)

def recipes_detail(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    context = {'recipe': recipe} # Изменили ключ на `recipe`
    return render(request, 'recipes_detail.html', context)