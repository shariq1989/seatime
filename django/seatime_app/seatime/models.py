from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Vessel(models.Model):
    name = models.CharField(max_length=64)
    official_number = models.CharField(max_length=64)
    tonnage = models.CharField(max_length=64)
    propulsion = models.CharField(max_length=64)
    hp = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class WorkdayType(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type}"


class VoyageType(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type}"


class StaffPosition(models.Model):
    department = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    rank = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.department} - {self.title}"


class Voyage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    depart_date = models.DateField()
    arrival_date = models.DateField()
    voyage_type = models.ForeignKey(VoyageType, on_delete=models.CASCADE)
    workday_type = models.ForeignKey(WorkdayType, on_delete=models.CASCADE)
    position = models.ForeignKey(StaffPosition, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.vessel} - {self.depart_date}"
