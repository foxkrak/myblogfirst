from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required()
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

@login_required()
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    # levei uma vida pra descobrir o erro que estava dando na pagina post_edit with keyword arguments '{'pk': ''}' not found. 1 pattern(s)
    # eu so precisava declarar a variavel post como declarado a baixo, para que o template pudesse usar, assim o botão delete funcionaria!
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})

@login_required()
def post_del(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    # Sou meio leigo, entao ficou esse code feio ai, mas ja ajeitei pensando um pouco mais.!
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # return render(request, 'blog/post_list.html', {'post': post, 'posts': posts})
    #
    # Esse é o codigo certo!
    return post_list(request)
    # somente isso..

# Create your views here.
