from django.urls import path
from .views import  (IndexView ,
                     AboutView,
                       ContactView,
                       FeaturesView,
                        JoinRoomView,
                        CreateRoomView,)


app_name = 'myapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('meeting/', CreateRoomView.as_view(), name='meeting'),
    path('join/', JoinRoomView.as_view(), name='join'),
    path('features/', FeaturesView.as_view(), name='features'),
]
