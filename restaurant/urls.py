from django.conf.urls import patterns, url
from django.views.generic import TemplateView, DetailView
from django.views.decorators.cache import cache_page

from .models import Restaurant


urlpatterns = patterns('restaurant.views',
    url(r'^$', cache_page(60 * 15)(TemplateView.as_view(template_name="home.haml")), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name="about.haml"), name='about'),
    url(r'^restaurants.json$', 'restaurants_json', name='json'),
    url(r'^restaurant/(?P<pk>\d+)/$', DetailView.as_view(model=Restaurant, template_name="restaurant/restaurant_detail.haml"), name='restaurant_detail'),
)
