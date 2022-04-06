from django.shortcuts import render
# my imports below
from django.views.generic import ListView
from .models import Post

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = "home.html"