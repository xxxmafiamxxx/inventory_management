from django.db import models

# Dimension Table: Categories
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

# Dimension Table: Locations
class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.state}, {self.region}, {self.postal_code}"

# Dimension Table: Customers
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    segment = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name

# Dimension Table: Products
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name

# Fact Table: SalesFacts
class SalesFact(models.Model):
    order_id = models.CharField(primary_key=True, max_length=20)
    order_date = models.DateField()
    ship_date = models.DateField()
    ship_mode = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sales = models.FloatField()
    quantity = models.IntegerField()
    discount = models.FloatField()
    profit = models.FloatField()

    def __str__(self):
        return self.order_id