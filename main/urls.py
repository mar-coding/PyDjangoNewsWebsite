from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  path('', views.home, name='home'),
                  path('detail/<int:id>', views.detail, name='detail'),
                  path('cat/<int:id>', views.cat, name='cat'),
                  path('register', views.reg, name='reg'),
                  path('signin', views.signin, name='signin'),
                  path('index', views.index, name='index'),
                  path('signout', views.signout, name='signout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
