from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# On user creation, generate a token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Extended auth user with this table
class MarinerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    citizenship_cntry = models.CharField(max_length=255)
    residence_state = models.CharField(max_length=255)
    mariner_ref_num = models.PositiveIntegerField()


# All the document dates
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
    drug_test_compliant = models.BooleanField(default=False)


# Ship details table. To be filled by an API
class Vessel(models.Model):
    name = models.CharField(max_length=64)
    official_number = models.CharField(max_length=64)
    tonnage = models.CharField(max_length=64)
    propulsion = models.CharField(max_length=64)
    hp = models.CharField(max_length=64)

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


# Dept: Engine, Deck
# Title: Captain
# Rank: 1
class StaffPosition(models.Model):
    department = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    rank = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.department} - {self.title}"


# Info for each voyage
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
