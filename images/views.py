from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Image, Comment, Like
from .forms import PostForm, ProfileUploadForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()
    print(images)
    return render(request, 'index.html', {"images":images})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()

    return render(request, 'profile.html', {"current_user": current_user, "profile": profile})


@login_required(login_url='/accounts/login/')
def post(request):

    current_user = request.user
    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)

        if form.is_valid:
            post = form.save(commit=False)
            post.name = current_user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'post.html', {"post_form": form})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'query' in request.GET and request.GET['query']:
        search_term = request.GET.get("query")
        user = Profile.search_profiles(search_term)
        images = Image.objects.all()
        message = f"{search_term}"

        content = {
            "message": message,
            "found": user,
            "images": images,
        }

        return render(request, 'search.html', content)
    else:
        message = "You haven't searched for anyone"
        return render(request, 'search.html', {"message": message})

@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user 
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                requested_profile.profile_pic = form.cleaned_data['profile_pic']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.username = form.cleaned_data['username']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(profile_pic = form.cleaned_data['profile_pic'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()


    return render(request,'upload_profile.html',{"title":title,"current_user":current_user,"form":form})

