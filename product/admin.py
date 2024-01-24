from django.contrib import admin
from .import models 
# Register your models here.


class SizeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = [ 'name','slug']
class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = [ 'name','slug']

admin.site.register(models.Product)
admin.site.register(models.UserReviews)
admin.site.register(models.Purchase)
admin.site.register(models.WishList)
admin.site.register(models.Size,SizeAdmin)
admin.site.register(models.Color,ColorAdmin)