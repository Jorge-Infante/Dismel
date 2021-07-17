from django.urls import path, re_path

from . import views
app_name = 'users_app'

urlpatterns = [
    
    path (
        'api/user/create/',
          views.UserCreateApiView.as_view(), 
          name='createUser'
    ),

]