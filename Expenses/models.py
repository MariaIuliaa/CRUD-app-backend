from django.db import models


class Expense(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    category = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.name
        #return f"amount: {self.amount} category: {self.category} date: {self.date}  description: {self.description}"
