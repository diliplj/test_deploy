from django.contrib import admin
from rest_api.models import *
from django.apps import apps

# admin.site.register(OTP)
# admin.site.register(Role)
# admin.site.register(UserTable)
# admin.site.register(Article)

class DynamicColumnAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super(DynamicColumnAdmin, self).__init__(*args, **kwargs)
        field_list = [i.name for i in self.model._meta.fields]
        self.list_select_related = ()
        self.search_fields = (field_list)
        self.list_display = field_list
        self.list_display_links = field_list

my_app = apps.get_app_config('rest_api')

for model in list(my_app.get_models()):
    admin.site.register(model, DynamicColumnAdmin)
