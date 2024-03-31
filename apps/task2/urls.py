from django.urls import path
from .api_endpoints.VacancyList import VacancyList


urlpatterns = [path("vacancies/", VacancyList.as_view(), name="vacancies")]
