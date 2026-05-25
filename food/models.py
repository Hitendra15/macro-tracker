from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.DecimalField(max_digits=8, decimal_places=2)
    protein = models.DecimalField(max_digits=8, decimal_places=2, help_text="Protein in grams")
    carbs = models.DecimalField(max_digits=8, decimal_places=2, help_text="Carbohydrates in grams")
    fats = models.DecimalField(max_digits=8, decimal_places=2, help_text="Fats in grams")
    fiber = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        help_text="Fiber in grams"
    )
    sugar = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        help_text="Sugar in grams"
    )
    image = models.ImageField(default='food/default-image.jpg',upload_to='food',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Consume(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food,on_delete=models.CASCADE)
    consumed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + "-" + str(self.food_consumed)