from django.db import models


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=20)
    citizenship = models.CharField(max_length=20)
    birth_year = models.DateField()
    work_place = models.CharField(max_length=30)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    number = models.CharField(max_length=16, unique=True)
    account_type = models.IntegerField(default=1)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.number} {self.account_type}'


class Credit(models.Model):
    sum = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sum} {self.date}"

