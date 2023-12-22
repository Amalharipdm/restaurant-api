from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def calculate_average_rating(self):
        ratings = Rating.objects.filter(restaurant=self)
        if ratings.exists():
            total_ratings = sum(rating.stars for rating in ratings)
            self.average_rating = total_ratings / len(ratings)
        else:
            self.average_rating = 0.00
        self.save()


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    stars = models.DecimalField(max_digits=3, decimal_places=2),
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'restaurant')

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'restaurant')