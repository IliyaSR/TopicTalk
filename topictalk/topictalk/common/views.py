from django.core.mail import send_mail
from django.shortcuts import render, redirect

from topictalk.common.forms import SearchForm
from topictalk.post.models import Post, Like, Comment, LikeComment


# Create your views here.
def home(request):
    all_posts = Post.objects.all()

    context = {
        'all_posts': all_posts,
    }

    return render(request, template_name='common/home-page.html', context=context)


def search_view(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        if Post.objects.filter(choose_community__icontains=searched):
            return redirect(f'{searched.lower()}')
        else:
            return render(request, 'common/search.html', {'searched': searched})


def like_functionality(request, post_id):
    post = Post.objects.get(id=post_id)
    liked_object = Like.objects.filter(to_post_id=post_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_post=post)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{post_id}')


def like_functionality_about_comments(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    liked_comment = LikeComment.objects.filter(to_comment_id=comment_id).first()

    if liked_comment:
        liked_comment.delete()
    else:
        like = LikeComment(to_comment=comment)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{comment_id}')


