from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('add_recipe', views.AddRecipe.as_view(), name='add_recipe'),
    path('the_recipes', views.TheRecipes.as_view(), name='the_recipes'),  
]
