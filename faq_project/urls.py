from django.contrib import admin
from django.urls import path
from faq.views import FAQListView, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page for FAQs
    path('api/faqs/', FAQListView.as_view(), name="faq-list"),
]
