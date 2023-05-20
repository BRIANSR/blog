from django.urls import path
from blogapp import views
from .views import HomeView, ArticleDetailView, AddpostView, editpostView, deletepostView, AddcategoryView, LikeView,AddCommentView

urlpatterns = [
    # path('home/', views.home, name="home"),
    path('home',HomeView.as_view(), name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(), name="Article-details"),
    path('add_post',AddpostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>',editpostView.as_view(), name="edit_post"),
    path('article/delete/<int:pk>',deletepostView.as_view(), name="delete_post"),
    path('add_category', AddcategoryView.as_view(), name="add_category"),
    # path('category/<str:cats>/', categoryView, name="category"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),

]
