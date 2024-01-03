from django.shortcuts import render, redirect

from topictalk.post.models import Post, Like


# Create your views here.
def home(request):
    all_posts = Post.objects.all()

    context = {
        'all_posts': all_posts
    }

    return render(request, template_name='common/home-page.html', context=context)


def like_functionality(request, post_id):
    post = Post.objects.get(id=post_id)
    liked_object = Like.objects.filter(to_post_id=post_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_post=post)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{post_id}')
