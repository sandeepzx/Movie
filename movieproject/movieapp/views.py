from django.shortcuts import redirect, render
from . models import Movie
from .forms import MovieForm

# Create your views here.
def index(req):
    movie = Movie.objects.all()
    context = {
        'movie_list' : movie
    }
    return render (req,"index.html", context)

def detail(req,movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(req,"detail.html",{'i':movie})

def add_movie(req):
    if req.method == "POST":
        name = req.POST.get('name')
        desc = req.POST.get('desc')
        year = req.POST.get('year')
        img = req.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, img=img)
        movie.save()
        return redirect('/')
    return render(req,"add.html")

def update(req,id):
    movie = Movie.objects.get(id=id)
    form = MovieForm( req.POST or None , req.FILES, instance = movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        return render(req, "edit.html", {'form':form, 'movie':movie })
    

def delete(req,id):
    if req.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(req, 'delete.html')
