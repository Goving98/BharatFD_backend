from rest_framework import serializers
from .models import FAQ
from django.core.cache import cache

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'category', 'created_at']

    def to_representation(self, instance):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'en') if request else 'en'
        
        # Try to get cached representation
        cache_key = f"faq_serializer:{instance.id}:{lang}"
        cached_data = cache.get(cache_key)
        
        if cached_data:
            return cached_data
            
        representation = super().to_representation(instance)
        representation['question'] = instance.get_translated_question(lang)
        representation['answer'] = instance.get_translated_answer(lang)
        
        # Cache the representation
        cache.set(cache_key, representation, timeout=3600)  # Cache for 1 hour
        
        return representation