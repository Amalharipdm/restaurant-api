from django.contrib import admin
from .models import Restaurant, Rating, Bookmark

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'average_rating')
    search_fields = ('name',)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant', 'stars', 'created_at')
    

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant', 'created_at')
    search_fields = ('user__username', 'restaurant__name')
