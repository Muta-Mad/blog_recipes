from django.shortcuts import get_object_or_404, render, redirect
from .forms import RecipeForm
from .models import Recipe
from django.views.generic import (
    DeleteView, UpdateView
)
from django.urls import reverse_lazy

def recipe_create(request, pk=None):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
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


def recipes_detail(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    context = {'recipe': recipe}
    return render(request, 'main/recipes_detail.html', context)


class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('main:list')
    template_name = 'main/recipe_delete.html'