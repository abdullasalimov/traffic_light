from django.db import models


class Department(models.Model):
    DEPARTMENT_LEVEL = (
        ("1", "Первый уровень"),
        ("2", "Второй уровень"),
        ("3", "Третий уровень"),
        ("4", "Четвертый уровень"),
        ("5", "Пятый уровень"),
    )
    
    name = models.CharField(max_length=155)
    level = models.CharField(max_length=1, choices=DEPARTMENT_LEVEL, blank=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    fullname = models.CharField(max_length=255)
    job_title = models.CharField(max_length=155)
    employment_date = models.DateField(auto_now_add=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.PROTECT,)

    def __str__(self):
        return self.fullname