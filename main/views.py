from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe

# Create your views here.
def recipe(request, pk=None):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main:recipes_list')
        
    else:
        form = RecipeForm()
    context = {'form': form}
    return render(request, 'recipes.html', context)

def recipes_list(request):
    recipe = Recipe.objects.all()
    context = {'recipe': recipe}
    return render(request, 'recipes_list.html', context)