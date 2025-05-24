from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item

@login_required
def dash(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/dash.html', {
        'items': items,
    })


# Create your views here.

