from django.shortcuts import redirect, render
from django.views.generic.edit import FormMixin
from .form import CarBookForm
from .filters import CarFilters
from django_filters.views import FilterView




# Create your views here.
from django.views.generic import ListView ,DetailView,CreateView
from .models import Car

class CarList(FilterView):
 model=Car
 paginate_by=2
 filterset_class=CarFilters
 template_name='car/car_list.html'
class CarDetail(FormMixin,DetailView):
  model=Car
  form_class=CarBookForm


  def get_context_data(self, **kwargs):  ##related category#get_context_data
    context =super().get_context_data(**kwargs)
    context["related"] =Car.objects.filter(category=self.get_object().category)[:2]
    return context

  def post(self,request,*args,**kwargs):
    form=self.get_form()
    if form.is_valid():
      myform=form.save(commit=False)
      myform.Car=self.get_object()
      myform.user=request.user
      myform.save()

      return redirect('/')


class AddListing(CreateView):
  pass

