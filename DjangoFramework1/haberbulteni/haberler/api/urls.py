from django.urls import path
from haberler.api import views as api_views


urlpatterns = [
    path('yazarlar/',api_views.GazeteciListCreateAPIView.as_view(), name = 'yazar_listesi'),
    path('makaleler/',api_views.MakaleListCreateAPIView.as_view(), name = 'makale_listesi'),
    path('makaleler/<int:pk>',api_views.MakaleDetailAPIView.as_view(), name = 'makale_detail'),
]



# # FUNCTION BASED VIEWS
# urlpatterns = [
#     path('makaleler/',api_views.makale_list_create_api_view, name = 'makale_listesi' ),
#     path('makaleler/<int:pk>',api_views.makale_detail_api_view, name = 'makale_detail' ),
# ]