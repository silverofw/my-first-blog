from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_rand(request):
    return render(request, 'blog/post_rand.html')

def post_guess1(request):
    return render(request, 'blog/post_guess1.html')
def post_guess2(request):
    return render(request, 'blog/post_guess2.html')
def post_guess3(request):
    return render(request, 'blog/post_guess3.html')
def post_guess4(request):
    return render(request, 'blog/post_guess4.html')
def post_guess5(request):
    return render(request, 'blog/post_guess5.html')
def post_guess6(request):
    return render(request, 'blog/post_guess6.html')
def post_guess7(request):
    return render(request, 'blog/post_guess7.html')
def post_guess8(request):
    return render(request, 'blog/post_guess8.html')
def post_guess9(request):
    return render(request, 'blog/post_guess9.html')
def post_guess10(request):
    return render(request, 'blog/post_guess10.html')
def post_guess11(request):
    return render(request, 'blog/post_guess11.html')
def post_guess12(request):
    return render(request, 'blog/post_guess12.html')
def post_guess13(request):
    return render(request, 'blog/post_guess13.html')

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
