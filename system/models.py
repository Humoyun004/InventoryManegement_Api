from django.db import models
from datetime import date


class Product(models.Model):
    name = models.CharField(max_length=55)
    manufacturer = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.name} applies to {self.manufacturer}"


class Part(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    units = models.IntegerField()
    date_produced = models.DateField()
    expiry_date = models.DateField()
    total = models.IntegerField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.total = self.units
            super(Part, self).save(*args, **kwargs)
        else:
            super(Part, self).save(*args, **kwargs)

    @property
    def freshness(self):
        if (date.today() - self.expiry_date).days > 0:
            return "Expired"
        elif (self.expiry_date - date.today()).days <= 3:
            return "Expiring"
        else:
            return "Fresh"

    def __str__(self):
        return f"{self.id} - {self.product} - expiry {self.expiry_date}"


class Order(models.Model):
    order_date = models.DateField()
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name="part_in_order")
    units = models.IntegerField()
    company = models.CharField(max_length=55)

    def save(self, *args, **kwargs):
        if not self.id:
            if self.units < self.part.total:
                self.part.total -= self.units
                self.part.save()
                super(Order, self).save(*args, **kwargs)
            return

    def __str__(self):
        return f"{self.order_date} - {self.units} from {self.part}"


