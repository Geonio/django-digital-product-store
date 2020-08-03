from django.contrib import admin
from django_changelist_toolbar_admin.admin import DjangoChangelistToolbarAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.http import HttpResponse

from .models import *


class DownloadButton(admin.ModelAdmin):
    list_display = ('title', 'count', 'download_button' )
    fields = ('title', 'description', 'icon', 'price') 

    def download_button(self, obj):
        return mark_safe('<a class="button" href="{}">Загрузить</a>'.format(reverse('download_product', args = (str(obj.id)) )))

    download_button.short_description = ''
    download_button.allow_tags = True


class SettingNoDeleteNoAdd(admin.ModelAdmin):
	model = Setting
	def has_delete_permission(self, request, obj=model.id):
		return False

	def has_add_permission(self, request):
		st = Setting.objects.all()
		if st:
			return False
		else:
			return True

	def has_change_permission(self, request, obj=model.id):
		return True



admin.site.register(Setting, SettingNoDeleteNoAdd)
admin.site.register(Product, DownloadButton)
