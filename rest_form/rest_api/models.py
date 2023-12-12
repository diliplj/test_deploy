from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User, AbstractUser


class Register(models.Model):
    username = models.CharField(max_length=150,unique=True,null=False)
    email  = models.EmailField(max_length=255,unique=True, null=False)
    password = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        super(Register, self).save(*args, **kwargs)
        if self.username:
            self.slug = slugify(self.username)
            super(Register, self).save()

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = "Register"
        verbose_name = "Register"


class Role(models.Model):
    role = models.CharField(max_length=255, null=False, default="user")
    email = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Role, self).save(*args, **kwargs)
        if self.role:
            self.slug = slugify(self.role)
            super(Role, self).save()
    
    def __str__(self):
        return '{0} - {1}'.format(self.email, self.role)
    
    class Meta:
        db_table = "Role"
        verbose_name = "Role"
