# -*- coding: utf-8 -*-
from io import BytesIO

from django.core.files.storage import default_storage
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from PIL import Image
from tinymce.models import HTMLField

from accounts.models import Author


class Category(models.Model):

    title = models.CharField(_("Título"), max_length=50)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Post(models.Model):

    title = models.CharField(_("Título"), max_length=100)
    overview = models.TextField(_("Detalle"), default="")
    timestamp = models.DateTimeField(_("Timestamp"), auto_now=True)

    content = HTMLField(default="<p>Noticia</p>")
    featured = models.BooleanField(_("Publicar"), default=False)
    category = models.ManyToManyField(
        Category, verbose_name=_("Categoria"), related_name="post"
    )
    author = models.ForeignKey(
        Author, verbose_name=_("Author"), on_delete=models.CASCADE
    )
    thumbnail = models.ImageField(
        _("Foto"), upload_to="thumbnail", default="thumbnail/default.jpg", blank=True
    )
    slug = models.SlugField(_("Slug"), blank=True, null=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("post_update", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("post_delete", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        if self.thumbnail:
            img = Image.open(default_storage.open(self.thumbnail.name))
            if img.mode != 'RGB':
                img = img.convert('RGB') 
            if img.height > 1080 or img.width > 1920: 
                output_size = (1920, 1080)
                img.thumbnail(output_size)
                buffer = BytesIO()
                img.save(buffer, format="JPEG")
                default_storage.save(self.thumbnail.name, buffer)


class Comment(models.Model):

    user = models.ForeignKey(Author, verbose_name=_("user_id"), on_delete=models.CASCADE, related_name="comments")
    timestamp = models.DateTimeField(_("Timestamp"), auto_now=True)
    content = models.TextField(_("Escribe aquí"))
    post = models.ForeignKey(
        Post, verbose_name=_("post_id"), on_delete=models.CASCADE, related_name="comments"
    )

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __str__(self):
        return self.user
