from django.contrib.auth.models import User
from django.db import models


# Extended auth user with this table
class MarinerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True)
    citizenship_cntry = models.CharField(max_length=255, blank=True)
    residence_state = models.CharField(max_length=255, blank=True)


# All the document dates
class MarinerDocument(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mariner_ref_num = models.PositiveIntegerField(null=True)
    mmc_doc_num = models.PositiveIntegerField(null=True)
    mmc_issue_date = models.DateField(null=True)
    mmc_expr_date = models.DateField(null=True)
    med_ntl_expr_date = models.DateField(null=True)
    med_stcw_expr_date = models.DateField(null=True)
    med_pilot_expr_date = models.DateField(null=True)
    twic_expr_date = models.DateField(null=True)
    basic_training_expr_date = models.DateField(null=True)
    advanced_fire_expr_date = models.DateField(null=True)
    first_aid_cpr_expr_date = models.DateField(null=True)
    passport_expr_date = models.DateField(null=True)
    drug_test_compliant = models.BooleanField(default=False)


# Ship details table. To be filled by an API
class Vessel(models.Model):
    name = models.CharField(max_length=64)
    official_number = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


# 8 hour workday, 12 hr day, etc
class WorkdayType(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type}"


# Inland Waterways, Coastal, Open Ocean, etc
class VoyageType(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type}"


# Title: MODU, OSV, etc
class Designation(models.Model):
    name = models.CharField(max_length=64)


# Title: Captain
class Rank(models.Model):
    designation = models.ManyToManyField(Designation)
    name = models.CharField(max_length=64)


# Info for each voyage
class Voyage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    depart_date = models.DateField()
    arrival_date = models.DateField()
    voyage_type = models.ForeignKey(VoyageType, on_delete=models.CASCADE)
    workday_type = models.ForeignKey(WorkdayType, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user} - {self.vessel} - {self.depart_date}"


class Tag(models.Model):
    title = models.CharField(max_length=100)


class Post(models.Model):
    tag = models.ManyToManyField(Tag)
    text = models.CharField(max_length=100)
