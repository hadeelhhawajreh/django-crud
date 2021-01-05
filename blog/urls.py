from django.urls import path,include
from .views import HomeBlogView,BlogCreate,BlogUpdate,BlogDelete,DetailsBlogView
urlpatterns = [
    path('',HomeBlogView.as_view() ,name='home'),
    path('<int:pk>/',DetailsBlogView.as_view() ,name='details'),
    path('add/' , BlogCreate.as_view() ,name='create_blog'),
    path('<int:pk>/update/',BlogUpdate.as_view(),name='update_blog'),
    path('<int:pk>/delete/',BlogDelete.as_view(),name='delete_blog')
    ]
