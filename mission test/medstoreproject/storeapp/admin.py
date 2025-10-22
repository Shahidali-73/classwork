from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'stock', 'added_at')
    search_fields = ('name', 'description', 'owner__username')
