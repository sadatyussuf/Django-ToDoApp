from django.db import models

# Create your models here.
class todoModel(models.Model):
    """
    docstring
    """
    name = models.CharField(max_length=500)
    

    

    def __str__(self):
        return self.name