from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class FacilityAdmin(admin.ModelAdmin):
    list_display= ['name','is_active']
    list_editable = ['is_active']
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Route)
admin.site.register(StartPoint)
admin.site.register(EndPoint)
admin.site.register(Schedule)
admin.site.register(Trip)
admin.site.register(Price)
admin.site.register(Vehicle)
admin.site.register(Facility,FacilityAdmin)
admin.site.register(Category,CategoryAdmin)



