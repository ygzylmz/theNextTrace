from django.contrib import admin

from .models import BlogGezi,BlogFilm,BlogDizi,BlogHayat,ImagesBlogGezi,ImagesBlogDizi,ImagesBlogFilm,ImagesBlogHayat

#admin.site.register(BlogGezi)
#admin.site.register(BlogDizi)
#admin.site.register(BlogFilm)
#admin.site.register(ImagesBlogGezi)

class ImagesBlogGeziAdmin(admin.StackedInline):
    model = ImagesBlogGezi

@admin.register(BlogGezi)
class BlogGeziAdmin(admin.ModelAdmin):
    inlines = [ImagesBlogGeziAdmin]

    class Meta:
        model = BlogGezi

@admin.register(ImagesBlogGezi)
class ImagesBlogGeziAdmin(admin.ModelAdmin):
    pass








class ImagesBlogDiziAdmin(admin.StackedInline):
    model = ImagesBlogDizi

@admin.register(BlogDizi)
class BlogDiziAdmin(admin.ModelAdmin):
    inlines = [ImagesBlogDiziAdmin]

    class Meta:
        model = BlogDizi

@admin.register(ImagesBlogDizi)
class ImagesBlogDiziAdmin(admin.ModelAdmin):
    pass






class ImagesBlogFilmAdmin(admin.StackedInline):
    model = ImagesBlogFilm

@admin.register(BlogFilm)
class BlogFilmAdmin(admin.ModelAdmin):
    inlines = [ImagesBlogFilmAdmin]

    class Meta:
        model = BlogFilm

@admin.register(ImagesBlogFilm)
class ImagesBlogFilmAdmin(admin.ModelAdmin):
    pass









class ImagesBlogHayatAdmin(admin.StackedInline):
    model = ImagesBlogHayat

@admin.register(BlogHayat)
class BlogHayatAdmin(admin.ModelAdmin):
    inlines = [ImagesBlogHayatAdmin]

    class Meta:
        model = BlogHayat

@admin.register(ImagesBlogHayat)
class ImagesBlogHayatAdmin(admin.ModelAdmin):
    pass
