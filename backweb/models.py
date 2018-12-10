from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'my_user'


class TokenUser(models.Model):
    token = models.CharField(max_length=30)
    user = models.OneToOneField(MyUser)

    class Meta:
        db_table = 'token_user'


class Atype(models.Model):
    t_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'a_type'


class Article(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)
    content = models.TextField()
    icon = models.ImageField(upload_to='article',null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=0)
    atype = models.ForeignKey(Atype, null=True)


    class Meta:
        db_table = 'article'


