from django.urls import path
from .views import *


urlpatterns = [
	path('send_file/<filename>', send_file, name = 'send_file'),
	path('buy/', buy, name='buy'),
	path('', index, name='index'),
	path('admin/download_product/<int:id>', download, name = 'download_product'),
]