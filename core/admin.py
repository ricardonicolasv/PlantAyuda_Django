from django.contrib import admin
from core.models import Categoria, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'stock', 'cod.producto', 'categoria']
    search_fields = ['nombre', 'cod.producto']
    list_filter = ['categoria']
    list_per_page: 10

admin.site.register(Producto)
admin.site.register(Categoria)