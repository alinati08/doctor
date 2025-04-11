from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class Blog(models.Model):
    title=models.CharField(_("عنوان"),max_length=50)
    description=models.CharField(_("توضیحات"),max_length=100)
    content=RichTextField(_("متن"))
    created_at=models.DateTimeField(_("زمان انتشار"),default=timezone.now)
    image=models.ImageField(_("تصویر"),upload_to="blogs/" , null=True , blank=True)
    author=models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.CASCADE)
    category=models.ForeignKey("Category",related_name="blog", verbose_name=_("دسته بندی"), on_delete=models.CASCADE, null=True)
    
    def __str__(self) :
        return self.title
    
    class  Meta:
        
        managed = True
        verbose_name = ' بلاگ'
        verbose_name_plural = 'بلاگ ها  '
    
    
class Category(models.Model):
    title=models.CharField(_("عنوان"),max_length=50)
    sluf=models.SlugField(_("عنوان لاتین"))
    published_at=models.DateField(_("تاریخ انتشار "),auto_now=False, auto_now_add=True)
    
    class  Meta:
        
        managed = True
        verbose_name = ' دسته بندی'
        verbose_name_plural = ' دسته بندی ها  '
    
    def __str__(self) :
        return self.title
    

 
 
 
 
    
class Comments(models.Model):
    blog=models.ForeignKey(("Blog"),verbose_name=_("مقاله"),related_name="comments", on_delete=models.CASCADE)
    name=models.CharField(_("نام کاربر"),max_length=50)
    email=models.EmailField(_("آدرس ایمیل "),max_length=254)
    message=models.TextField(_("متن کامنت"))
    date=models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    
    class  Meta:
        
        managed = True
        verbose_name = ' کامنت '
        verbose_name_plural = '  کامنت ها   '
    def __str__(self) :
        return self.email