from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('restaurant.views',
    url(r'^$', TemplateView.as_view(template_name="home.haml"), name='home'),
    url(r'^restaurants.json$', 'restaurants_json', name='home'),
)
