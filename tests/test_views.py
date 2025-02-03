import pytest
from rest_framework.test import APIClient
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_api():
    client = APIClient()
    FAQ.objects.create(question="Test Q?", answer="Test A", category="FD")

    response = client.get("/api/faqs/")
    assert response.status_code == 200
    assert len(response.json()) > 0
