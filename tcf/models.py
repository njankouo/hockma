from django.db import models

# Create your models here.

class Personnel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"


class Test(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_days = models.IntegerField()
    features = models.TextField()

    def __str__(self):
        return self.name

class PackagePersonnel(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    assigned_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.personnel} - {self.package}"

class module(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 