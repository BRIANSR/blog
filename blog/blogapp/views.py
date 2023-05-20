from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from requests import request
from .forms import postform, editform, CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

from blogapp.models import post, category, Comment


# def home(req):
#     return render(req,"index.html")

def LikeView(request, pk):

    PostL = get_object_or_404(post, id=request.POST.get('post_id'))
    liked =False
    if PostL.likes.filter(id=request.user.id).exists():
      PostL.likes.remove(request.user)
      liked=False
    else:
     PostL.likes.add(request.user)
    liked =True
    return HttpResponseRedirect(reverse('Article-details', args=[str(pk)]))


class HomeView(ListView):
    model = post
    template_name = 'index.html'
    ordering = ['-post_date']
    # ordering = ['-id']
#
# def categoryView(request,cats):
#     category_posts=post.objects.filter(category=cats)
#     return render(request, 'categories.html', {'cats': cats , 'category_posts': category_posts })

class ArticleDetailView(DetailView):
    model = post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(post,  id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        context["total_likes"] = total_likes
        context["liked"] =liked
        return context
class AddpostView(CreateView):
    model = post
    form_class = postform
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title','body')
    # when we want  specific form patterns we have to name it from previously created models.in this we selected __all__
class AddcategoryView(CreateView):
    model = category
    template_name = 'add_category.html'
    fields = '__all__'
class editpostView(UpdateView):
    model = post
    form_class = editform
    template_name = 'edit_post.html'

class deletepostView(DeleteView):
    model = post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comments.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

