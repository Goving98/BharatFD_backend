import pytest
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_model():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
        category="BANK"
    )
    assert faq.question == "What is Django?"
    assert faq.answer == "Django is a web framework."
    assert faq.category == "BANK"

