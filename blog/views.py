from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from taggit.models import Tag
from .models import Post, Comment, Visit
from .forms import CommentPostForm


# Create your views here.





def post_list(request, tag_slug=None, page_number=1):
    object_list = Post.published.all()
    tag = None
    tags = Post.tags.all()

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    per_page = 8
    paginator = Paginator(object_list, per_page)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # Если page_number не целое число, то
        # выдать первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {"posts": posts, "tags": tags}
    return render(request, "blog/blog.html", context)


# @require_POST
def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    ip_address = request.META.get("REMOTE_ADDR")
    Visit.objects.create(user=request.user, ip=ip_address, post_id=post.id)
    v = Visit.objects.filter(post_id=post.id).count()

    comments = post.comments.filter(active=True)
    return render(
        request,
        "blog/detail.html",
        {
            "post": post,
            "comments": comments,
            'view_count': v,
        },
    )


def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    comment_form = CommentPostForm(data=request.POST)
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.post = post
        if request.POST.get("parent", None):
            new_comment.parent_id = int(request.POST.get("parent"))


        new_comment.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    comment_form = CommentPostForm()
    return redirect(Post.get_absolute_url)


def to_get_comment(request, comment_id):
    selected_comment = get_object_or_404(Comment, id=comment_id)
    selected_comment.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def page_not_found_view(request, exception):
    return render(request, "server/404.html", status=404)
