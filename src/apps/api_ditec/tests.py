from django.contrib.auth import get_user_model
from django.urls import reverse

import pytest
import responses
from mixer.backend.django import mixer
from rest_framework_simplejwt.tokens import RefreshToken
from .views import get_subjects, get_filter_subjects
from django.conf import settings


@pytest.fixture
def get_or_create_token():
    user = mixer.blend(get_user_model())
    refresh = RefreshToken.for_user(user)
    return refresh.access_token


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_name_app():
    from apps.api_ditec.apps import ApiDitecConfig
    assert ApiDitecConfig.name == 'api_ditec'


@pytest.mark.django_db
@responses.activate
def test_news(api_client, get_or_create_token):
    url = settings.API_DITEC + '/noticias/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('news')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_not_found_news(api_client, get_or_create_token):
    url = settings.API_DITEC + '/noticias/_search'
    responses.add(responses.POST,
                  url,
                  status=201)

    path = reverse('news')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': 'Error not found results'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_news(api_client, get_or_create_token):
    url = settings.API_DITEC + '/noticias/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('news-search') + '?search=word'
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_news_without_word(api_client, get_or_create_token):
    url = settings.API_DITEC + '/noticias/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('news-search')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': 'It is necessary to pass search'}
    assert len(responses.calls) == 0


@pytest.mark.django_db
@responses.activate
def test_radioagency(api_client, get_or_create_token):
    url = settings.API_DITEC + '/radioagencia/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('radioagency')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_not_found_radioagency(api_client, get_or_create_token):
    url = settings.API_DITEC + '/radioagencia/_search'
    responses.add(responses.POST,
                  url,
                  status=201)

    path = reverse('radioagency')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': 'Error not found results'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_radioagency(api_client, get_or_create_token):
    url = settings.API_DITEC + '/radioagencia/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('radioagency-search') + '?search=word'
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_radioagency_without_word(api_client, get_or_create_token):
    url = settings.API_DITEC + '/radioagencia/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('radioagency-search')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': 'It is necessary to pass search'}
    assert len(responses.calls) == 0


@pytest.mark.django_db
@responses.activate
def test_tvcamara(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-tv/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('tvcamara')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_not_found_tvcamara(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-tv/_search'
    responses.add(responses.POST,
                  url,
                  status=201)

    path = reverse('tvcamara')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': 'Error not found results'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_tvcamara(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-tv/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('tvcamara-search') + '?search=word'
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_tvcamara_without_word(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-tv/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('tvcamara-search')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': 'It is necessary to pass search'}
    assert len(responses.calls) == 0


@pytest.mark.django_db
@responses.activate
def test_get_subjects(api_client, get_or_create_token):
    path = '/noticias/_search'
    responses.add(responses.POST,
                  settings.API_DITEC + path,
                  json={'response': 'json_test'}, status=201)

    response = get_subjects(path)

    assert response == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == settings.API_DITEC + \
        '/noticias/_search'


@pytest.mark.django_db
@responses.activate
def test_get_subjects_without_json(api_client, get_or_create_token):
    path = '/noticias/_search'

    responses.add(responses.POST,
                  settings.API_DITEC + path,
                  status=201)

    response = get_subjects(path)

    assert response == {'error': 'Error not found results'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == settings.API_DITEC + \
        '/noticias/_search'


@pytest.mark.django_db
@responses.activate
def test_get_filter_subjects(api_client, get_or_create_token):
    path = '/noticias/_search'
    responses.add(responses.POST,
                  settings.API_DITEC + path,
                  json={'response': 'json_test'}, status=201)

    response = get_filter_subjects('word', path)

    assert response == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == settings.API_DITEC + \
        '/noticias/_search'


@pytest.mark.django_db
@responses.activate
def test_get_filter_subjects_without_json(api_client, get_or_create_token):
    path = '/noticias/_search'

    responses.add(responses.POST,
                  settings.API_DITEC + path,
                  status=201)

    response = get_filter_subjects('word', path)

    assert response == {'error': 'Error not found results'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == settings.API_DITEC + \
        '/noticias/_search'


@pytest.mark.django_db
@responses.activate
def test_radiocamara(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-radio/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('radiocamara')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_not_found_radiocamara(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-radio/_search'
    responses.add(responses.POST,
                  url,
                  status=201)

    path = reverse('radiocamara')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': 'Error not found results'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_radiocamara(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-radio/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('radiocamara-search') + '?search=word'
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'response': 'json_test'}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.django_db
@responses.activate
def test_search_radiocamara_without_word(api_client, get_or_create_token):
    url = settings.API_DITEC + '/programas-radio/_search'
    responses.add(responses.POST,
                  url,
                  json={'response': 'json_test'}, status=201)

    path = reverse('radiocamara-search')
    api_client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(
        get_or_create_token))
    response = api_client.get(path)

    assert response.json() == {'error': 'It is necessary to pass search'}
    assert len(responses.calls) == 0