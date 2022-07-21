from django.urls import path
from kitaplar.api import views as api_views

urlpatterns = [
    path('kitaplar/',api_views.KitapListCreateAPIView.as_view(), name='kitap_listesi'),
    path('kitaplar/<int:pk>', api_views.KitapDetailAPIView.as_view(), name= 'kitap_detail'),
    path('kitaplar/<int:kitap_pk>/yorum_yap', api_views.YorumCreateAPIView.as_view(), name='yorum_yap'),
    path('yorumlar/<int:pk>', api_views.YorumDetailAPIView.as_view(), name = 'yorumlar'),
]
