from django.contrib.auth.models import User
from django.db import models


class MarinerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    citizenship_cntry = models.CharField(max_length=255)
    residence_state = models.CharField(max_length=255)
    mariner_ref_num = models.PositiveIntegerField()


class MarinerDocument(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mmc_doc_num = models.PositiveIntegerField()
    mmc_issue_date = models.DateField()
    mmc_expr_date = models.DateField()
    med_ntl_expr_date = models.DateField()
    med_stcw_expr_date = models.DateField()
    med_pilot_expr_date = models.DateField()
    twic_expr_date = models.DateField()
    basic_training_expr_date = models.DateField()
    advanced_fire_expr_date = models.DateField()
    first_aid_cpr_expr_date = models.DateField()
    passport_expr_date = models.DateField()
    drug_test_compliant = models.DateField()


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
