from django.contrib import admin
from .models import Car, Category

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("make", 'model', 'year', 'get_total_price', 'is_sold')
    # list_display_links = ("make", 'model', 'year', 'created_at')
    # list_filter = ("make", 'model', 'year', 'created_at')
    search_fields = ("make", 'model', 'year', 'created_at')
    # list_per_page = 2
    list_editable = ('model', 'year')
    # readonly_fields = ('model',)
    actions = ['sold_out']

    @admin.action(description="Sold out")
    def sold_out(self, request, queryset):
        queryset.update(is_sold=True)

    @admin.display(description="Total Price")
    def get_total_price(self, obj):
        return obj.price * obj.quantity

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = "Our Administration"