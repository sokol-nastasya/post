from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from user_post.models import Post
from user_post.forms import PostForm

def main(request):
	post = Post.objects.all().order_by('-date')

	paginator = Paginator(post, 5)
	page = request.GET.get('page')

	try:
		post = paginator.page(page)
	except PageNotAnInteger:
		post = paginator.page(1)
	except EmptyPage:
		post = paginator.page(paginator.num_pages)

	args = {'post':post}

	return render(request, 'user_post/main.html', args)


def show_post(request, pk):
	args = {}
	args.update(csrf(request))
	args['post'] = get_object_or_404(Post, pk=pk)
	return render(request, 'user_post/post.html', args)

def addlikes(request, post_id):
    post = get_object_or_404(Post,id = post_id)
    post.likes += 1
    post.save()
    return redirect('/posts/%s' %post_id)

def dislike(request, post_id):
	post = get_object_or_404(Post,id = post_id)
	post.dislike += 1
	post.save()
	return redirect('/posts/%s' %post_id)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('user_post:show_post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'user_post/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('user_post:show_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'user_post/post_edit.html', {'form': form})
