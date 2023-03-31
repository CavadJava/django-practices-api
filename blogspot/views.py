from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView  # new
from .models import PostForm


# Create your views here.
def index(request):
    return HttpResponse('Hello World')


class BlogListView(ListView):
    model = PostForm
    template_name = 'home.html'
    context_object_name = 'all_posts_list'


class BlogDetailView(DetailView):
    model = PostForm
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = PostForm
    fields = '__all__'
    template_name = 'post_new.html'
    # fields = ['title', 'author', 'body']
