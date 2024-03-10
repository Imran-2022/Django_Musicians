from django.shortcuts import render,redirect
from . import forms
from album.models import Album
# Create your views here.

def add_album(request):
    if request.method=='POST':
        album_form=forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage') 
    else: 
        album_form=forms.AlbumForm()
    return render(request, 'album.html',{'form':album_form})

def delete_album(request,id):
    post = Album.objects.get(pk=id)
    post.delete()
    return redirect('homepage') 