from django.db import models
from django.utils.text import slugify
from django.contrib.auth.hashers import check_password, make_password
from django.utils.crypto import salted_hmac


class Category(models.Model):
    cat_name = models.CharField(max_length=55,verbose_name="Categorylar")
    slug = models.SlugField(max_length=100,unique=True,db_index=True,verbose_name="Url slug")
    is_menu =  models.BooleanField(default=True,verbose_name="Menuda korish")


    class Meta:

        verbose_name = "categorya"

    def __str__(self):
        return self.cat_name

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.cat_name) 
        super() .save(*args,**kwargs)

    def get_menu(self):
        return "Menuda korinadi"  if self.is_menu else "Menuda korinmaydi"


class New(models.Model):
    title =  models.CharField(max_length=255,verbose_name="Saralavha")
    short_desc =  models.CharField(max_length=500,verbose_name="qisqacha")
    description = models.TextField(verbose_name="Toliq malumoti")

    image = models.ImageField(upload_to="news/",blank=True,null=True,)

    tags= models.CharField(max_length=255, unique=True,blank=True,null=True,  verbose_name="url tags")


    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,)

    views =  models.PositiveBigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True,verbose_name="yartilgan vaqti")

    class Meta:
        verbose_name = "new"
        verbose_name_plural = "News"
        ordering =  ['-created_at']

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return self.image.url



class NewImage(models.Model):
    article =  models.ForeignKey(New,on_delete=models.CASCADE,related_name="images")
    img =  models.ImageField(upload_to="news/")


class Comment(models.Model):
    user =  models.CharField(max_length=55)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    new =  models.ForeignKey(New,on_delete=models.CASCADE,verbose_name="yanglik")


    parent = models.ForeignKey("comment",  on_delete=models.CASCADE,null=True,blank=True)

    is_sub =  models.BooleanField(default=False)

    class Meta:
        verbose_name =  "comment"
        verbose_name_plural =  "comments"

    def save(self,*args,**kwargs):
        if self.parent:
            self.is_sub = True
        return super(Comment,self).save(*args,**kwargs)

class Contact(models.Model):
    user =  models.CharField(max_length=55)
    phone = models.CharField(max_length=30,verbose_name="telefon")
    message = models.TextField()
    is_contacted = models.BooleanField(default=False)
    is_trash =  models.BooleanField(default=False)

    class Meta:
        verbose_name = "Conatact_info"
        verbose_name_plural = "Conatact_infolar"

    def __str__(self):
        return f"{self.user} | {self.message}"

class  Subscribe(models.Model):
    email =  models.EmailField(unique=True)
    is_active =  models.BooleanField(default=True)
    created_at  =  models.DateTimeField(auto_now_add=True,verbose_name="vaqt ")

    class Meta:
        verbose_name =  "Subscribe"
        verbose_name_plural = "Subscribes"

    def __str__(self):
        return self.email




class User(models.Model):
    ROLE_CHOICES = [
        ("user", "Oddiy user"),
        ("admin", "Admin"),
        ("seller", "Sotuvchi"),
    ]

    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="user",
    )
    phone_number = models.CharField(max_length=20, unique=True)
    second_number = models.CharField(max_length=20)
    email = models.CharField(max_length=70, null=True, blank=True)
    location = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=128)
    password_conf = models.CharField(max_length=8)
    last_login = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    # Website accounts are separate from Django's existing admin accounts.
    is_active = True
    is_staff = False
    is_superuser = False
    is_authenticated = True
    is_anonymous = False

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.password_conf = ""

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def get_session_auth_hash(self):
        return salted_hmac("core.User.session", self.password, algorithm="sha256").hexdigest()

    def get_session_auth_fallback_hash(self):
        from django.conf import settings

        for secret in settings.SECRET_KEY_FALLBACKS:
            yield salted_hmac(
                "core.User.session", self.password, secret=secret, algorithm="sha256"
            ).hexdigest()







