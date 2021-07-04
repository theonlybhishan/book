from django.db import models
from django.db.models.base import Model

# Create your models here.


class StartPoint(models.Model):
    start_point_name= models.CharField(max_length=500)
    pickup_Points = models.CharField(max_length=100)

    def __str__(self):
        return self.start_point_name

class EndPoint(models.Model):
    end_point_name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.end_point_name

class Schedule(models.Model):
    start_time= models.TimeField()
    end_time = models.TimeField()
    duration = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.start_time}-{self.end_time}'
class Route(models.Model):
    route_name = models.CharField(max_length=200)
    start_point = models.ForeignKey(StartPoint, on_delete=models.CASCADE)
    end_point = models.ForeignKey(EndPoint, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.route_name

class Trip(models.Model):
    title = models.TextField(max_length=300)
    route = models.ForeignKey(Route ,on_delete=models.CASCADE)
    Schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title


class Price(models.Model):
    route_name = models.ForeignKey(Route, on_delete=models.CASCADE)
    price = models.IntegerField()
    children_price = models.IntegerField(blank=True)
    special_price = models.IntegerField(blank=True)
    group_price_per_person = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.route_name}-{self.price}'

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    Registrarion_number = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    engine_no = models.CharField(max_length=100)
    model_no = models.CharField(max_length=100)
    chasis_no = models.CharField(max_length=100)
    owner = models.CharField(max_length= 100)
    owner_phone_no = models.CharField(max_length=20)
    brand_name = models.CharField(max_length=100)
    is_active= models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}-{self.Categories}'


class Facility(models.Model):
    name= models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name