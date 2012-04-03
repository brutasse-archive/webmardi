from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse

from .forms import CheeseForm
from .models import Cheese, Taste

def cheese_list(request):
    context = {
        'cheeses': Cheese.objects.all(),
    }
    return TemplateResponse(request, 'cheese_list.html', context)


def cheese_detail(request, pk):
    cheese = get_object_or_404(Cheese, pk=pk)
    user_taste = None
    if request.user.is_authenticated():
        try:
            user_taste = cheese.tastes.get(user=request.user)
        except Taste.DoesNotExist:
            pass
    return TemplateResponse(request, 'cheese_detail.html',
                            {'cheese': cheese, 'taste': user_taste})

@login_required
def like_cheese(request, pk):
    cheese = get_object_or_404(Cheese, pk=pk)
    taste, created = cheese.tastes.get_or_create(user_id=request.user.user.pk)
    taste.like = True
    taste.save()
    return redirect(reverse('cheese_detail', args=[pk]))


@login_required
def dislike_cheese(request, pk):
    cheese = get_object_or_404(Cheese, pk=pk)
    taste, created = cheese.tastes.get_or_create(user_id=request.user.user.pk)
    taste.like = False
    taste.save()
    return redirect(reverse('cheese_detail', args=[pk]))


@login_required
def add_cheese(request):
    if request.method == 'POST':
        form = CheeseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            cheese = form.save()
            return redirect(reverse('cheese_detail', args=[cheese.pk]))
    else:
        form = CheeseForm()
    return TemplateResponse(request, 'cheese_form.html', {'form': form})
