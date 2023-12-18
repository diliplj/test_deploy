from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator,RegexValidator
from rest_api import api

DATAMODE_CHOICES = (('Active','Active'),('Inactive','Inactive'),('Delete','Delete'))


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

class OTP(models.Model):
    email  = models.EmailField(max_length=255, null=False)
    otp = models.CharField(max_length = 6,validators=[RegexValidator(r'^\d+$', 'Enter a valid number.')])
    is_verified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(OTP, self).save(*args, **kwargs)
        if self.email:
            self.slug = slugify(self.email)
            super(OTP, self).save()

    def __str__(self):
        return self.email+"__"+str(self.otp)
    
    class Meta:
        db_table = "OTP"
        verbose_name = "OTP"

class UserTable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=15, db_index=True)

    def save(self, *args, **kwargs):
        super(UserTable, self).save(*args, **kwargs)
        num = api.six_digit_otp(6,None)
        num = str(list(num)[0])
        self.uid = str(num)+'-%06d' % self.id
        super(UserTable, self).save(*args, **kwargs)
        return self
    
    def __str__(self):
        return '{0}'.format(self.user.email)
    


class Article(models.Model):
    uid = models.CharField(max_length=15, db_index=True)
    title = models.CharField(max_length = 50, null=False)
    headline = models.TextField(null=False)  
    body = models.TextField(null=False)
    image = models.ImageField(null=False, upload_to="")
    slug = models.SlugField(max_length=255,blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.CharField(blank=True,null=True, max_length=255)
    updated_by = models.CharField(blank=True,null=True, max_length=255)

    datamode = models.CharField(max_length=257, default='Active', choices=DATAMODE_CHOICES)

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        if self.title:
            self.slug = slugify(self.title)
            super(Article, self).save()
        num = api.six_digit_otp(6,None)
        num = str(list(num)[0])
        self.uid = str(num)+'-%06d' % self.id
        super(Article, self).save(*args, **kwargs)
        return self
    
    def __str__(self):
        return '{0}'.format(self.user.email)

    def __str__(self):
        return '{0}'.format(self.title)

    class Meta:
        db_table = "Article" 
        verbose_name = "Article" 


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    slug = models.SlugField(max_length=255,blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.CharField(blank=True,null=True, max_length=255)
    updated_by = models.CharField(blank=True,null=True, max_length=255)

    datamode = models.CharField(max_length=257, default='Active', choices=DATAMODE_CHOICES)

    def __str__(self):
        return '{0}'.format(self.article.title)

    class Meta:
        db_table = "Comment" 
        verbose_name = "Comment"    
