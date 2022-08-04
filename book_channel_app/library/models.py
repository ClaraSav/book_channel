from django.db import models
from colorfield.fields import ColorField
from django.utils.translation import gettext_lazy as _


class Languaje(models.Model):

    name = models.CharField(verbose_name=_("Languaje"), max_length=100)

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):

    name = models.CharField(verbose_name=_("Category"), max_length=100)
    parent_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    color = ColorField(default="#00FF00")

    def __str__(self):
        name = self.name
        parent = self.parent_id
        while parent:
            name = parent.name + '/' + name
            parent = parent.parent_id
        return name

    class Meta:
        verbose_name_plural = "categories"


class Book(models.Model):

    title = models.CharField(verbose_name=_("Book"), max_length=200, blank=False)
    isbn = models.CharField(verbose_name=_("ISBN"), max_length=200, unique=True)
    publish_date = models.DateField(verbose_name=_("Publish Date"), blank=True, null=True)
    category_ids = models.ManyToManyField(Category, verbose_name=_("Categories"), blank=True)
    editorial = models.CharField(verbose_name=_("Editorial"), max_length=100, blank=True, null=True)
    languaje_id = models.ForeignKey(Languaje, verbose_name=_("Languaje"), on_delete=models.RESTRICT, blank=False)
    number_pages = models.IntegerField(verbose_name=_("Pages"), blank=True, null=True)
    description = models.TextField(verbose_name=_("Description"))
    front_page = models.ImageField(default='library/img/libro_portada.png')
    author_id = models.ForeignKey(Author, verbose_name=_("Author"), on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.title}'


class Platform(models.Model):

    name = models.CharField(verbose_name=_('Name'), max_length=50)
    platform_ico = models.ImageField(default='library/img/avatar.png')

    def __str__(self):
        return f'{self.name}'


class Link(models.Model):

    FORMAT_FILES = [
        ('pdf', 'PDF'),
        ('epub', 'EPUB'),
        ('cbr', 'CBR'),
        ('ebook', 'eBook'),
    ]

    url = models.URLField(verbose_name=_("URL"))
    book_id = models.ForeignKey(Book, blank=False, on_delete=models.CASCADE)
    platform_id = models.ForeignKey(Platform, blank=False, null=True, verbose_name=_("Platform"), on_delete=models.RESTRICT)
    format = models.CharField(max_length=20, choices=FORMAT_FILES, default='pdf')

    def __str__(self):
        return f'{self.url}'


