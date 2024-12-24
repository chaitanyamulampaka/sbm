from django.urls import path
from . import  views



from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from .views import signup
from .views import login

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
    path('otp_verify/', views.otp_verify, name='otp_verify'),
    path('home/product_viewer/<int:id>/', views.productViewer, name='productViewer'),
    path('logout/', views.logout_view, name='logout'),
    path('add_to_cart/<int:product_id>',views.addtocart,name='addtocart') ,
    path('cart/', views.viewcart, name='viewcart'),
    path('checkout/',views.AddressView,name='checkout'),
    path('get-city-state/', views.get_city_state, name='get_city_state'),
    path('delete_from_cart/<int:id>',views.delete_from_cart,name='delete_from_cart'),
    # Add any other URL patterns here
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)