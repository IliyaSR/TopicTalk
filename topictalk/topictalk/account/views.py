from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, template_name='account/sign-in.html')


def register(request):
    return render(request, template_name='account/sign-up.html')


def details_profile(request, pk):
    return render(request, template_name='account/profile.html')


def edit_profile(request, pk):
    return render(request, template_name='account/edit-profile.html')


def delete_profile(request, pk):
    return render(request, template_name='account/delete-profile.html')
