from django.db import models
from django.db import models
from django.shortcuts import reverse
from unidecode import unidecode
from django.template.defaultfilters import slugify,safe
from django.contrib.auth.models import User
from uuid import uuid4
import os
from cropduster.models import CropDusterField, Size
from ckeditor.fields import RichTextField

def upload_to(instance,filename):
    uzanti = filename.split('.')[-1]
    new_name = "%s.%s"%(str(uuid4()),uzanti)
    unique_id = instance.unique_id
    return os.path.join('blog',unique_id,new_name)

class BlogGezi(models.Model):

    title = models.CharField(max_length=100
                            ,verbose_name='Baslik Giriniz',help_text = 'Baslik bilgisi burada girilir')

    #content = models.TextField(null=True,blank=False,max_length=2500,verbose_name='İcerik')

    content = RichTextField(null=True,blank=False,max_length=10000,verbose_name='İcerik')
    
    #image = models.ImageField(default="default/ohdintropng.png",upload_to=upload_to,blank=True, verbose_name='Foto',
    #                              null=True, help_text="Kapak Fotosu Yukleyiniz")

    image = models.ImageField(blank=True)

    slug = models.SlugField(null=True, unique=True, editable=False)

    unique_id = models.CharField(max_length=100,editable=False,null=True)

    creating_date = models.DateField(auto_now_add=True,auto_now=False) # "Yayın Tarihi" auto now true olursa her dokundugunda guncelleniyor

    class Meta:   #Cogul degil istedigimiz ismi verdik
        verbose_name_plural = 'GonderilerGezi'
        ordering = ['-id']

    def __str__(self):
        return "%s" % (self.title)

    #def get_absolute_url(self):
    #    return reverse('post-detail',kwargs={'slug':self.slug})

    def get_image_filename(instance, filename):
        title = instance.post.title
        slug = slugify(title)
        return "post_images/%s-%s" % (slug, filename)  

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return '/media/default/ohdintropng.png'

    def get_unique_slug(self):
        sayi = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while BlogGezi.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "%s-%s"%(slug,sayi)

        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            new_unique_id = str(uuid4())
            self.unique_id = new_unique_id
            self.slug = self.get_unique_slug() #slugify(unidecode(title))
        else :
            blog = BlogGezi.objects.get(slug=self.slug)
            if blog.title != self.title :
                self.slug = self.get_unique_slug()
        super(BlogGezi, self).save()


    #def get_blog_comment(self):
        ##Comment classında "blog" kısmına related name comment ekledigimiz icin burada comment diyip devam ediyoruz
    #    return self.comment.all()

class BlogFilm(models.Model):

    title = models.CharField(max_length=100
                            ,verbose_name='Baslik Giriniz',help_text = 'Baslik bilgisi burada girilir')

    #content = models.TextField(null=True,blank=False,max_length=2500,verbose_name='İcerik')

    content = RichTextField(null=True,blank=False,max_length=10000,verbose_name='İcerik')

    image = models.ImageField(default="default/ohdintropng.png",upload_to=upload_to,blank=True, verbose_name='Foto',
                                  null=True, help_text="Kapak Fotosu Yukleyiniz")

    slug = models.SlugField(null=True, unique=True, editable=False)

    unique_id = models.CharField(max_length=100,editable=False,null=True)

    creating_date = models.DateField(auto_now_add=True,auto_now=False) # "Yayın Tarihi" auto now true olursa her dokundugunda guncelleniyor

    class Meta:   #Cogul degil istedigimiz ismi verdik
        verbose_name_plural = 'GonderilerFilm'
        ordering = ['-id']

    def __str__(self):
        return "%s" % (self.title)

    #def get_absolute_url(self):
    #    return reverse('post-detail',kwargs={'slug':self.slug})

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return '/media/default/ohdintropng.png'

    def get_unique_slug(self):
        sayi = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while BlogFilm.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "%s-%s"%(slug,sayi)

        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            new_unique_id = str(uuid4())
            self.unique_id = new_unique_id
            self.slug = self.get_unique_slug() #slugify(unidecode(title))
        else :
            blog = BlogFilm.objects.get(slug=self.slug)
            if blog.title != self.title :
                self.slug = self.get_unique_slug()
        super(BlogFilm, self).save()

class BlogDizi(models.Model):


    title = models.CharField(max_length=100
                            ,verbose_name='Baslik Giriniz',help_text = 'Baslik bilgisi burada girilir')

    #content = models.TextField(null=True,blank=False,max_length=2500,verbose_name='İcerik')
    content = RichTextField(null=True,blank=False,max_length=10000,verbose_name='İcerik')
    image = models.ImageField(default="default/ohdintropng.png",upload_to=upload_to,blank=True, verbose_name='Foto',
                                  null=True, help_text="Kapak Fotosu Yukleyiniz")

    slug = models.SlugField(null=True, unique=True, editable=False)

    unique_id = models.CharField(max_length=100,editable=False,null=True)

    creating_date = models.DateField(auto_now_add=True,auto_now=False) # "Yayın Tarihi" auto now true olursa her dokundugunda guncelleniyor

    class Meta:   #Cogul degil istedigimiz ismi verdik
        verbose_name_plural = 'GonderilerDizi'
        ordering = ['-id']

    def __str__(self):
        return "%s" % (self.title)

    #def get_absolute_url(self):
    #    return reverse('post-detail',kwargs={'slug':self.slug})

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return '/media/default/ohdintropng.png'

    def get_unique_slug(self):
        sayi = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while BlogDizi.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "%s-%s"%(slug,sayi)

        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            new_unique_id = str(uuid4())
            self.unique_id = new_unique_id
            self.slug = self.get_unique_slug() #slugify(unidecode(title))
        else :
            blog = BlogDizi.objects.get(slug=self.slug)
            if blog.title != self.title :
                self.slug = self.get_unique_slug()
        super(BlogDizi, self).save()

class BlogHayat(models.Model):


    title = models.CharField(max_length=100
                            ,verbose_name='Baslik Giriniz',help_text = 'Baslik bilgisi burada girilir')

    #content = models.TextField(null=True,blank=False,max_length=2500,verbose_name='İcerik')
    content = RichTextField(null=True,blank=False,max_length=10000,verbose_name='İcerik')
    
    image = models.ImageField(default="default/ohdintropng.png",upload_to=upload_to,blank=True, verbose_name='Foto',
                                  null=True, help_text="Kapak Fotosu Yukleyiniz")

    slug = models.SlugField(null=True, unique=True, editable=False)

    unique_id = models.CharField(max_length=100,editable=False,null=True)

    creating_date = models.DateField(auto_now_add=True,auto_now=False) # "Yayın Tarihi" auto now true olursa her dokundugunda guncelleniyor

    class Meta:   #Cogul degil istedigimiz ismi verdik
        verbose_name_plural = 'GonderilerHayat'
        ordering = ['-id']

    def __str__(self):
        return "%s" % (self.title)

    #def get_absolute_url(self):
    #    return reverse('post-detail',kwargs={'slug':self.slug})

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return '/media/default/ohdintropng.png'

    def get_unique_slug(self):
        sayi = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while BlogHayat.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "%s-%s"%(slug,sayi)

        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            new_unique_id = str(uuid4())
            self.unique_id = new_unique_id
            self.slug = self.get_unique_slug() #slugify(unidecode(title))
        else :
            blog = BlogHayat.objects.get(slug=self.slug)
            if blog.title != self.title :
                self.slug = self.get_unique_slug()
        super(BlogHayat, self).save()





    
class ImagesBlogGezi(models.Model):
    blog = models.ForeignKey(BlogGezi)
    image = models.ImageField(upload_to="images/",blank=True,null=True)
    unique_id = models.CharField(max_length=100,editable=False,null=True)

    class Meta:   #Cogul degil istedigimiz ismi verdik
        verbose_name_plural = 'ImagesGonderilerGezi'

    def __str__(self):
        return self.blog.title + "Image"

class ImagesBlogFilm(models.Model):
    blog = models.ForeignKey(BlogFilm)
    image = models.ImageField(upload_to="images/",blank=True,null=True)
    unique_id = models.CharField(max_length=100,editable=False,null=True)

    class Meta:   #Cogul degil istedigimiz ismi verdik
        verbose_name_plural = 'ImagesGonderilerFilm'

    def __str__(self):
        return self.blog.title + "Image"

class ImagesBlogDizi(models.Model):
    blog = models.ForeignKey(BlogDizi)
    image = models.ImageField(upload_to="images/",blank=True,null=True)
    unique_id = models.CharField(max_length=100,editable=False,null=True)

    class Meta:   #Cogul degil istedigimiz ismi verdik
        verbose_name_plural = 'ImagesGonderilerDizi'

    def __str__(self):
        return self.blog.title + "Image"

class ImagesBlogHayat(models.Model):
    blog = models.ForeignKey(BlogHayat)
    image = models.ImageField(upload_to="images/",blank=True,null=True)
    unique_id = models.CharField(max_length=100,editable=False,null=True)

    class Meta:   #Cogul degil istedigimiz ismi verdik
        verbose_name_plural = 'ImagesGonderilerHayat'

    def __str__(self):
        return self.blog.title + "Image"