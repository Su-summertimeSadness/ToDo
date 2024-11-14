from time import time

from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


# Create your models here.

def get_slug(user_slug):
    new_sl = slugify(user_slug, allow_unicode=True)
    return new_sl + '-' + str(int(time()))


class Action(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    body = models.TextField(blank=True, db_index=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    dead_line = models.DateTimeField(null=True)

    tag = models.ForeignKey('Tag', related_name='actions', null=True, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('action_detail', kwargs={'slug': self.slug})

    def get_update(self):
        return reverse('action_update', kwargs={'slug': self.slug})

    def get_delete(self):
        return reverse('action_delete', kwargs={'slug': self.slug})

    # def get_done(self):
    #     self.is_done = True
    #
    #     return reverse('action_detail', kwargs={'slug': self.slug})


    # def get_not_done(self):
    #     self.is_done = False
    #     return reverse('action_detail', kwargs={'slug': self.slug})







    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = get_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def get_update(self):
        return reverse('tag_update', kwargs={'slug': self.slug})

    def get_delete(self):
        return reverse('tag_delete', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
