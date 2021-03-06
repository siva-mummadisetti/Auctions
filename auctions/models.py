from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser): # AbstractUser is not an abstract class, it has fields implemented for username, password ....
    watchlist = models.ManyToManyField("Listing", blank = True, related_name = "watch")
    def __str__(self):
        return f"{self.username}"

class Listing(models.Model):
    ad_title = models.TextField()
    description = models.TextField()
    img_url = models.TextField()
    category = models.TextField()
    price = models.IntegerField()
    time = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "listing")
    flag = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.ad_title}"

class Bid(models.Model):
    quote = models.IntegerField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE, related_name = "bid")
    def __str__(self):
        return f"{self.quote}"

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE, related_name = "comment")
    time = models.TextField()
    def __str__(self):
        return f"{self.text}"