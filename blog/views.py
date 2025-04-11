from django.shortcuts import render 
from .models import Blog , Comments
from .forms import CommentForm
from django.core.paginator import Paginator
# Create your views here.
def blog_list(request):
    blogs= Blog.objects.all()
    paginator = Paginator(blogs, 3)  # Show 3 blog per page.
    page_number = request.GET.get("page") 
    blog_list = paginator.get_page(page_number)
    
    context={
        "blog_list":blog_list
    }
    
    return render(request,"blog/blog_list.html" ,context)

def blog_detail(request,id):
    blog= Blog.objects.get(id=id)
   
    comments=Comments.objects.all().filter(blog=blog)
    
    if request.method == "POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            new_name=form.cleaned_data['name']
            new_email=form.cleaned_data['email']
            new_message=form.cleaned_data['message']
        
            new_comment=Comments(blog=blog,name=new_name,email=new_email, message=new_message)
            new_comment.save()
    context={
        "blog":blog ,
        # "recents":recents ,
        "comments":comments ,
    }
    
    return render(request,"blog/blog_detail.html",context)