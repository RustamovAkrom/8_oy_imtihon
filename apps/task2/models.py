from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    salary_from = models.DecimalField(max_digits=10, decimal_places=2)
    salary_to = models.DecimalField(max_digits=10, decimal_places=2)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"-{self.title}-"
