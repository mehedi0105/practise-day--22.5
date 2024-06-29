
from django.urls import path
# from .views import UserRegistrationView, UserLoginView, UserLogoutView,UserBankAccountUpdateView
from .views import UserRegistrationView, UserLoginView, user_logout,UserBankAccountUpdateView, pass_change
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
    path('logout/', user_logout, name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' ),
    path('pass_change/', pass_change, name='pass_change'),
]