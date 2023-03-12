from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=20)
    citizenship = models.CharField(max_length=20)
    birth_year = models.DateField()
    work_place = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Account(models.Model):
    number = models.CharField(max_length=16)
    account_type = models.IntegerField()
    client = models.ForeignKey("Client", on_delete=models.CASCADE, related_name="accounts")

    def __str__(self):
        return self.number


class Credit(models.Model):
    sum = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    account = models.ForeignKey("Account", on_delete=models.CASCADE, related_name="credits")
