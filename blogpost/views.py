from django.views import generic
from .models import BlogModel
from django.urls import reverse_lazy

# Create your views here.
class BlogList(generic.ListView):
    template_name = 'list.html'
    model = BlogModel

class BlogDetail(generic.DetailView):
    template_name = 'detail.html'
    model = BlogModel

class BlogCreate(generic.CreateView):
    template_name = 'create.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')

class BlogDelete(generic.DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')

class BlogUpdate(generic.UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')
