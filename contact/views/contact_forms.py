from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from contact.models import Contact
from django.db.models import Q
from django.http import Http404

def create(request):
    context = {}

    return render(
        request,
        'contact/create.html',
        context
    )