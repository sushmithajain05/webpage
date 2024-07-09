from django.db import models

# Create your models here.
class Menu(models.Model):
	name = models.CharField(max_length=20, help_text="eg. pizza, pasta")

	def __str__(self):
		return self.name


class Dish(models.Model):
	TAG_CHOICES = (('hot!', 'hot!'), ('popular', 'popular'), ('special', 'special'), ('seasonal', 'seasonal'))
	
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	recipe = models.CharField(max_length=100)
	tag = models.CharField(max_length=15, blank=True, null=True, choices=TAG_CHOICES)

	class Meta:
		verbose_name_plural = "Dishes"

	def __str__(self):
		return self.name	


class Reservation(models.Model):
	name = models.CharField(max_length=100)
	people = models.PositiveSmallIntegerField()
	date = models.DateTimeField()
	message = models.CharField(max_length=500)

	def __str__(self):
		return self.name