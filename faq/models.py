from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import LANGUAGES
import requests
from django.conf import settings

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    category = models.CharField(max_length=10, choices=[
        ('FD', 'Fixed Deposits'),
        ('INV', 'Investments'),
        ('BANK', 'Banking'),
    ], default='FD')

    def translate_and_cache(self, text, target_language):
        if target_language == 'en' or target_language not in LANGUAGES:
            return text

        cache_key = f"faq:{self.id}:{text[:50]}:{target_language}"
        
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation

        try:
            api_key = settings.GOOGLE_TRANSLATE_API_KEY
            url = f"https://translation.googleapis.com/language/translate/v2?key={api_key}"
            response = requests.post(url, json={
                "q": text,
                "target": target_language
            })

            if response.status_code == 200:
                translation = response.json()["data"]["translations"][0]["translatedText"]
                cache.set(cache_key, translation, timeout=86400)
                return translation
            
        except Exception as e:
            print(f"Translation error: {e}")
        
        return text

    def get_translated_question(self, lang):
        return self.translate_and_cache(self.question, lang)

    def get_translated_answer(self, lang):
        return self.translate_and_cache(self.answer, lang)

    def __str__(self):
        return self.question[:100]