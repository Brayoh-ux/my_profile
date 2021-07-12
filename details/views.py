from django.shortcuts import render, redirect
from .models import Profile, Pictures
from .forms import ProfileForm, LetterForm, PicturesForm

def home(request):
    profile = Profile.objects.all()
    pictures = Pictures.objects.all()

    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            print('valid')

    else:
        form = LetterForm()

    return render(request, 'home.html', {'profile': profile, 'letter': form, 'pictures':pictures})

def upload(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        pictures = PicturesForm(request.POST, request.FILES)

        if (form.is_valid(), pictures.is_valid()):
            article = form.save(commit=False)
            article.save()

            form = pictures.save(commit=False)
            form.save()

        return redirect('home')

    else:
        form = ProfileForm()
        pictures = PicturesForm()
        
    return render(request, 'upload.html', {'form': form, 'pictures': pictures})

def more(request):
    pictures = Pictures.objects.all()

    return render(request, 'more.html', {'pictures': pictures})