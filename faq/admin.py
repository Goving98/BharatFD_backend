from django.contrib import admin
from .models import FAQ
from django import forms
from ckeditor.widgets import CKEditorWidget

class FAQAdminForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = FAQ
        fields = '__all__'

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm
    list_display = ('question', 'category', 'get_short_answer')
    list_filter = ('category',)
    search_fields = ('question', 'answer')
    
    fieldsets = (
        ('FAQ Content', {
            'fields': ('question', 'answer', 'category')
        }),
    )

    def get_short_answer(self, obj):
        from django.utils.html import strip_tags
        clean_answer = strip_tags(obj.answer)
        return clean_answer[:100] + ('...' if len(clean_answer) > 100 else '')
    get_short_answer.short_description = 'Answer Preview'