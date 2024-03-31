from rest_framework.serializers import ModelSerializer
from apps.task2.models import Vacancy


class VacancyListSerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ("title", "description", "salary", "salary_from", "salary_to")
