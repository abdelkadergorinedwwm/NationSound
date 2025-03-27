from django.contrib import admin
from django.urls import path
from monsite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.accueil, name='accueil'),  
    path('billetterie/', views.billetterie, name='billetterie'),  
    path('contact/', views.contact, name='contact'),  
    path('faq/', views.faq, name='faq'),  
    path('partenaires/', views.partenaires, name='partenaires'),  
    path('programmation/', views.programmation, name='programmation'),

      ]
    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
