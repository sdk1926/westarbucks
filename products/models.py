from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'
    
    def __str__(self):
        return self.name

class Category(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    sodium_mg =models.DecimalField(max_digits=6, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'nutritions'

class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'allergys'

    def __str__(self):
        return self.name 

class Product(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)    
    description = models.TextField()
    nutrition = models.OneToOneField(Nutrition, on_delete=models.PROTECT, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    allergy = models.ManyToManyField(Allergy,
                                     through='Allergyproduct',
                                     related_name='products')

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.korean_name

class Image(models.Model):
    products = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    image_url = models.CharField(max_length=2000)

    class Meta:
        db_table = 'images'

   


class Allergyproduct(models.Model):
    allergy = models.ForeignKey(Allergy, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)  

    class Meta:
        db_table = 'allergyproducts'


