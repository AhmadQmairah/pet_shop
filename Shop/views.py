from django.shortcuts import render,redirect
from .models import Pet
from .froms import PetForm
# Create your views here.
def animal_list(request):
	context={"pets":Pet.objects.filter(available=True)}
	return render(request,"list.html",context)

def animal_detail(request,animal_id):
	context={"pet":Pet.objects.get(id=animal_id)}
	return render(request,"detail.html",context)


def animal_create(request):
	form=PetForm()
	context={"form":form}
	if request.method=="POST":
		form=PetForm(request.POST,request.FILES)
		if(form.is_valid()):
			form.save()
			return redirect('animal_list')
	return render(request,"create.html",context)


def animal_update(request,animal_id):
	pet=Pet.objects.get(id=animal_id)
	form=PetForm(instance=pet)
	context={"form":form}
	if request.method=="POST":
		form=PetForm(request.POST,request.FILES,instance=pet)
		if(form.is_valid()):
			form.save()
			return redirect('animal_detail',animal_id=pet.id)
	return render(request,"update.html",context)

def animal_delete(request,animal_id):
	Pet.objects.get(id=animal_id).delete()
	return redirect('animal_list')

