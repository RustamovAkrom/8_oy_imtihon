from rest_framework.generics import ListAPIView
from apps.task2.models import Vacancy
from .serializers import VacancyListSerializer


class VacancyList(ListAPIView):
    serializer_class = VacancyListSerializer

    def get_queryset(self):
        queryset = Vacancy.objects.all()

        salary = self.request.query_params.get("salary", None)
        salary_to = self.request.query_params.get("salary_to", None)
        salary_from = self.request.query_params.get("salary_from", None)
        print(salary, salary_to, salary_from)

        if not salary:
            if not salary_to:
                if not salary_from:
                    return queryset
                else:
                    return queryset.filter(salary_from__icontains = salary_from)    
            else:
                return queryset.filter(salary_to__icontains = salary_to)
        else:

            return queryset.filter(salary__icontains = salary)
          

__all__ = [
    "VacancyList",
]
