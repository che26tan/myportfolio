from django.shortcuts import render
from blog.models import Blog, BlogStat
from thought.models import Thought, ThoughtStat

# Create your views here.
def home(request):
    # blog = Blog.objects.order_by('blogstat._like')[10]
    # thought = Thought.objects.order_by('blogstat._like')[10]
    blog = Blog.objects.all()
    thought = Thought.objects.all()
    context={'blogs':blog, 'thoughts': thought}
    return render(request, 'home.html', context=context)