from django.db import models


class Auther(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=False)
    author = models.ForeignKey(Auther, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} liked {self.post.title}"
