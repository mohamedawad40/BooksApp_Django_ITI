
from django.urls import path
from accounts.views import  profile_view
urlpatterns = [
    path('profile/', profile_view , name='account.profile'),
    # path('register',create_user, name='account.register' )
]