from django.db import models

class Contact(models.Model):
  firstname = models.CharField(max_length=500)
  lastname = models.CharField(max_length=500)
  email = models.EmailField(null=True)
  contactNumber = models.IntegerField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
