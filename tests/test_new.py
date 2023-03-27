import pytest
from django.urls import reverse
import sys

pytestmark = pytest.mark.django_db
@pytest.mark.urls('demo_app.urls')
def test_demo(client, settings, capsys):
    settings.DEBUG = True
    url = reverse("test_endpoint")
    response = client.get(url)
    captured = capsys.readouterr()
    sys.stdout.write(captured.out)
    assert "Total queries: 1" in captured.out
    assert response.status_code == 200