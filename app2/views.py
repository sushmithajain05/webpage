from django.shortcuts import render,redirect
from . models import Menu
from . forms import ReservationForm

# Create your views here.
def index(request):
	active_menu = Menu.objects.get(id=1)
	other_menus = Menu.objects.exclude(id=1)

	# process reservation
	if request.method == 'POST':
		form = ReservationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = ReservationForm()
	
	context = {
		'active_menu': active_menu,
		'other_menus': other_menus,
		'form': form
	}
	return render(request, 'index.html', {'menu':menu})
