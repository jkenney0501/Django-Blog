from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


#home page view
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context )

#creates a post listing from ALL users, order by most recent
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #to change to order newest to oldest use the - 1st
    paginate_by = 5
    
    
#creates a user post listing with pagination, ordered by most recent
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


#dsplay post on sep page after clicking link
class PostDetailView(DetailView):
    model = Post
    
#create a post after user is logged in and from home page  
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
#create UPDATE VIEW  
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    #check to see if user is the author of the post and is allowed to update it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#delete view, user must be author an must be logged in
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    #check to see if user is the author of the post and is allowed to delete it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
#about page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'} )

#landing page
def index(request):
    return render(request, 'blog/index.html' )
