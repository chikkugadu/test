from django.urls import path
from submit import views
from .views  import add_detail
from .views  import homepageview

urlpatterns = [
    path('',views.homepageview,name='home'),
    path('add_detail/',views.add_detail,name='add_detail')
]