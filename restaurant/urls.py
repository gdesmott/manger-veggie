from django.conf.urls import patterns, url
from django.views.generic import TemplateView, DetailView

from .models import Restaurant


urlpatterns = patterns('restaurant.views',
    url(r'^$', TemplateView.as_view(template_name="home.haml"), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name="about.haml"), name='about'),
    url(r'^restaurants.json$', 'restaurants_json', name='home'),
    url(r'^restaurant/(?P<pk>\d+)/$', DetailView.as_view(model=Restaurant, template_name="restaurant/restaurant_detail.haml"), name='home'),
)
