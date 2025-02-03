from django.shortcuts import render
from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):    
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


def home(request):
    lang = request.GET.get('lang', 'en')  # Get the language from the query parameter
    faqs = FAQ.objects.all()
    for faq in faqs:
        faq.question = faq.get_translated_question(lang)
        faq.answer = faq.get_translated_answer(lang)
    return render(request, 'home.html', {'faqs': faqs, 'lang': lang})