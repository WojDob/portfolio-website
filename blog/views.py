from django.shortcuts import render, get_object_or_404

from .models import Category, Post

def post_list_view(request, category_name=None):
    if category_name:
        queryset = Post.objects.filter(category__name=category_name)
    else:
        queryset = Post.objects.all()
    context = {
        'object_list': queryset.filter(public=True).order_by('-date_publish'),
        'category_list': Category.objects.all(),
        'category_name': category_name,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail_view(request, post_id):
    context = {
        'object': get_object_or_404(Post, id=post_id),
        'category_list': Category.objects.all(),
        'category_name': None,
    }
    return render(request, 'blog/post_detail.html', context)
