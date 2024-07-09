from django.contrib import admin
from . models import Menu, Dish, Reservation
# Register your models here.
class ReservationModel(admin.ModelAdmin):
	list_display = ('name', 'people', 'date', 'message')


class DishInline(admin.TabularInline):
	model = Dish
	extra = 0

class MenuAdmin(admin.ModelAdmin):
	inlines = [DishInline,]

admin.site.register(Menu, MenuAdmin)
admin.site.register(Reservation, ReservationModel)

