from django.urls import path

from .views import login_page, logout_page, signup_vendor,signup_garage
from .views import  profile, bus_profile, edit_profile, update_profile, edit_bus_profile

urlpatterns = [
    path('login/', login_page, name='login'),
    path('signup-vendor/', signup_vendor, name = 'signup-vendor'),
    path('signup-garage/', signup_garage, name = 'signup-garage'),
    path('logout/', logout_page, name='logout'),
    path('edit_profile/<str:username>', edit_profile, name= 'edit_profile'),
    path('edit_bus_profile/<str:username>', edit_bus_profile, name='edit_bus_profile'),
    path('update_profile/<int:id>', update_profile, name = "update_profile"),
    path('profile/<str:username>', profile, name= 'profile'),
    # path('inventory/' inventory)
    # path('profile/<int:id>', edit_profile, name='profile_edit'),
    # path('update-profile/<int:id>', update_profile, name='profile'),
    path('bus_profile/<str:username>', bus_profile, name = "bus_profile"),
   
]