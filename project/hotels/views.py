from django.shortcuts import render
from .models import Hotel
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .mixins import LoginAndOrganisationRequiredMixin
from .forms import HotelCreateForm
from django.contrib import messages
class HotelListView(ListView):
    model = Hotel 
    context_object_name = 'hotels'
    paginate_by = 6
    ordering = ['-created_at']
    def get_queryset(self):
        queryset = super(HotelListView, self).get_queryset()
        place = self.request.GET.get('place') or None
        if place == None:
            queryset = Hotel.objects.all()
        else:
            queryset = Hotel.objects.filter_by_place(place)
        queryset = queryset 
        return queryset


class HotelDetailView(DetailView):
    model = Hotel 

    def get_context_data(self, **kwargs):
        context = super(HotelDetailView, self).get_context_data(**kwargs)
        context['related_hotels'] = Hotel.objects.related_hotels(self.get_object().place)
        return context
    

class HotelCreateView(LoginAndOrganisationRequiredMixin, CreateView):
    model = Hotel
    form_class = HotelCreateForm

    def form_valid(self, form):
        hotel = form.save(commit=False)
        hotel.place = form.cleaned_data['place']
        messages.success(self.request, 'your hotel ad has been created successfully.')
        return super(HotelCreateView, self).form_valid(form)


    def form_invalid(self, form):
        messages.error(self.request, 'An error occured.')
        return super(HotelCreateView, self).form_invalid(form)