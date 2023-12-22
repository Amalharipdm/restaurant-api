from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, UserLoginView, RestaurantList, AdminRestaurantListView, AdminLoginView, RestaurantViewSet, UserViewSet, HighRatedRestaurantList, BookmarkDeleteView, BookmarkListCreateView, RestaurantListCreateView, RatingListCreateView, CreateRatingView


router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')
router.register(r'users', UserViewSet, basename='user')
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('restaurants_list/', RestaurantList.as_view(), name='restaurant-list'),
    path('high_rated_restaurants/?min_average_rating=3.5,', HighRatedRestaurantList.as_view(), name='high-rated-restaurant-list'),
    path('bookmarks/', BookmarkListCreateView.as_view(), name='bookmark-list-create'),
    path('bookmarks/<int:restaurant_id>/', BookmarkDeleteView.as_view(), name='bookmark-delete'),
    path('restaurants/', RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('ratings/', RatingListCreateView.as_view(), name='rating-list-create'),
    path('ratings/create/', CreateRatingView.as_view(), name='create-rating'),


    path('admin/restaurants/', AdminRestaurantListView.as_view(), name='admin-restaurant-list'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('api/', include(router.urls)),
]
urlpatterns += router.urls