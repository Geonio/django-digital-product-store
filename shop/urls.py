from django.urls import path
from .views import *


urlpatterns = [
	path('', index, name='index'),
	path('buy/', buy, name='buy'),
	path('send_file/<filename>', send_file, name = 'send_file'),
	path('admin/download_product/<int:id>', download, name = 'download_product'),
]
