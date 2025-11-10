from django.db import models
from django.utils import timezone
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان خبر")
    image = models.ImageField(upload_to='news_images/', verbose_name="تصویر خبر", blank=True, null=True)
    content = models.TextField(verbose_name="متن کامل خبر")
    author = models.CharField(max_length=100, verbose_name="نویسنده")
    tags = models.CharField(max_length=200, verbose_name="تگ‌ها", help_text="تگ‌ها را با کاما جدا کنید")
    published_date = models.DateField(default=timezone.now, verbose_name="تاریخ انتشار")
    is_active = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "اخبار"
        ordering = ['-published_date']

    def __str__(self):
        return self.title