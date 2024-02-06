import pytest  # need to add pytest.ini and conftest.py


# Create your tests here.
@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_page_render(client, page):
    # this test stub
    response = client.get("/prototype/")
    assert response.status_code == 200
