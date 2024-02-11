import pytest  # need to add pytest.ini and conftest.py

# Create your tests here.

app_urls = ["/", "/prototype/", "/about/"]


@pytest.mark.parametrize("app_url", app_urls)
@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_page_render(client, app_url, user):
    # this test stub
    response = client.get(app_url)
    assert response.status_code == 200
