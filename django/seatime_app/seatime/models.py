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


# Title: Captain
class StaffPosition(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"


# Title: MODU, OSV, etc
class Rating(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"


class StaffRatingCombinations(models.Model):
    staff_position = models.ForeignKey(StaffPosition, related_name='positions', on_delete=models.CASCADE)
    position_rating = models.ForeignKey(Rating, related_name='ratings', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.staff_position} - {self.position_rating}"


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


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)


class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)
