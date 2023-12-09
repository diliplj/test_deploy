from django.db import models
from django.template.defaultfilters import slugify


class Register(models.Model):
    username = models.CharField(max_length=150)
    email  = models.EmailField(max_length=255,unique=True, null=False)
    password = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        super(Register, self).save(*args, **kwargs)
        if self.username:
            self.slug = slugify(self.username)
            super(Register, self).save()

    def __str__(self):
        return self.email