from django.shortcuts import render


# Create your views here.
def post_create(request):
    return render(request, template_name='post/post-page.html')


def post_details(request):
    return render(request, template_name='post/post-details.html')


def minecraft(request):
    return render(request, template_name='post/minecraft-post.html')