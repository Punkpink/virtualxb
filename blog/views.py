from multiprocessing import context
from django.shortcuts import redirect, render,get_object_or_404
from  django.views.generic import View
from .forms import PostCreateForm
from .models import Post

# Create your views here.

class BlogListView(View):
    def get(self,request,*arg,**kwargs):
        posts = Post.objects.all()
        context={
            'posts':posts
        }
        return render(request, 'blog_list.html',context)

class BlogCreateView(View):
    def get(self, request, *arg,**kwargs):
        form = PostCreateForm
        context = {
            'form':form
        }
        return render(request,'blog_create.html',context)

    def post(self, request, *arg,**kwargs):
        if request.method == "POST":
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title = title, content = content)
                p.save()
                return redirect('blog:home')

        context = {

        }
        return render(request,'blog_create', context)

class BlogDetailView(View):
    def get(self,request, pk,*arg,**kwargs):
        post = get_object_or_404(Post,pk=pk)
        context = {
            'post':post
        }
        return render(request,'blog_detail.html', context)