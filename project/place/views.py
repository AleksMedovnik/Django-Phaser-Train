from django.shortcuts import render
from django.views.generic.base import TemplateView


def main(request):
    return render(request, 'place/index.html')

class Canvas1(TemplateView):
    template_name = 'place/canvas1.html'