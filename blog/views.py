from django.shortcuts import get_object_or_404, redirect, render 
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

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    comments = Comments.objects.filter(blog=blog)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blog = blog  # اتصال کامنت به بلاگ
            new_comment.save()
            return redirect('blog_detail', id=blog.id)  # ری‌دایرکت بعد از ثبت موفق

    context = {
        'blog': blog,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/blog_detail.html', context)
    
    return render(request,"blog/blog_detail.html",context)