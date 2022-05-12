from django.urls import path, include
#from apps.users.api.api import CustomUserAPIView
#from apps.users.api.api import user_api_view, user_detail_api_view


urlpatterns = [
    path('users/',include('users.urls')),
#     path('rest-auth/', include('rest_auth.urls')),
]



# # urlpatterns = [
# #     path('user/', user_api_view, name = 'user_api'),
# #     path('user/<int:pk>/', user_detail_api_view, name = 'user_detail_api_view'),
# # ]