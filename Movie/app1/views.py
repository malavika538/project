from django.shortcuts import render,redirect
from app1.models import Movie
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# def home(request):
#     m = Movie.objects.all()
#     context = {'movie': m}
#     return render(request, 'home.html', context)
class HomeView(ListView):
    model=Movie
    context_object_name="movie"
    template_name="home.html"

    def get_queryset(self):
        queryset=super().get_queryset().filter(name__startswith='k')
        return queryset
    # def get_context_data(self,object_list=None, **kwargs):
    #     context=super().get_context_data()
    #     context['name']="Malu"
    #     context['age']=23
    #     return context
    extra_context={'name':'Malu','age':23}

# def detail(request,movie_id):
#     movie=Movie.objects.get(id=movie_id)
#     return render(request,'detail.html',{'movie':movie})

class MovieDetail(DetailView):
    model=Movie
    context_object_name="movie"
    template_name="detail.html"


# def addmovie(request):
#     if(request.method=="POST"):
#         t =request.POST['t']
#         d = request.POST['d']
#         l = request.POST['l']
#         y = request.POST['y']
#         i = request.FILES['i']
#         m=Movie.objects.create(title=t,description=d,language=l,year=y,image=i)
#         m.save()
#         return redirect('home')
#     return render(request,'addmovie.html')

from movieapp.forms import MovieForm

# def add_movie(request):
#     # if(request.method=="POST"):
#     #      form=MovieForm(request.POST)
#       #     if form.is_valid():
#       #          form.save()
#        #         return redirect("app1:index")
#
#
#     form=MovieForm()
#     context={'form':form}
#     return render(request,'add1.html',context)
#
# class AddMovie(CreateView):
#     model=Movie
#     form_class=MovieForm
#     template_name="add1.html"
#     success_url=reverse_lazy('app1:index')
#
# class MovieUpdate(UpdateView):
#     model=Movie
#     form_class=MovieForm
#     template_name = "edit.html"
#     success_url = reverse_lazy('app1:index')
#


class MovieDelete(DeleteView):
    template_name='delete.html'
    model=Movie
    sucess_url=reverse_lazy('app1:index')







def view(request,p):
    m=Movie.objects.get(id=p)
    context={'movie':m}
    return render(request,'view.html',context)
def delete(request,p):
    k=Movie.objects.get(id=p)
    k.delete()
    return redirect("home")
def edit(request,p):
    m=Movie.objects.get(id=p)
    if(request.method == "POST"):
        m.title = request.POST["t"]
        m.description = request.POST["d"]
        m.language = request.POST["l"]
        m.year = request.POST["y"]
        if(request.FILES.get('i') == None):
            m.save()
        else:
            m.image=request.FILES.get("i")

        m.save()
        return redirect('view',p)

    context={'movie':m}
    return render(request,'edit.html',context)