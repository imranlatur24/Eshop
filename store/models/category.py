from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=25)  
    def __str__(self):
        return self.name #return category name in product model for easy selection 
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
