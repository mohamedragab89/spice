from django.contrib import admin
from gamification.models import Method

def test_method(modeladmin, request, queryset):
    queryset.update(status='p')
test_method.short_description = "Make the method available to test on website"

class MethodAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    ordering = ['name']
    actions = [test_method]

admin.site.register(Method, MethodAdmin)
