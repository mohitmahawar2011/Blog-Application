from django.urls import path
from .views import get_blog,home,register_attempt,login_attempt,show_all_blog,create_blog,\
    update_blog,delete_blog,logout_attempt,about_page

urlpatterns = [
    path('get-blog/<id>/',get_blog,name='get_blog'),
    path('',home,name='home'),
    path('show-all-blog/',show_all_blog,name = 'show_all_blog'),
    path('create-blog/',create_blog,name= 'create_blog'),
    path('update-blog/<id>/',update_blog,name = 'update_blog'),
    path('delete-blog/<id>/',delete_blog,name='delete_blog'),
    path('login/',login_attempt,name = 'login'),
    path('register/',register_attempt,name= 'register'),
    path('logout/',logout_attempt,name='logout'),
    path('about/',about_page,name='about_page'),

    ]