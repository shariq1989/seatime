# Generated by Django 3.0.7 on 2020-07-02 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seatime', '0010_rating_staffratingcombinations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffratingcombinations',
            old_name='positionRating',
            new_name='position_rating',
        ),
        migrations.RenameField(
            model_name='staffratingcombinations',
            old_name='staffPosition',
            new_name='staff_position',
        ),
    ]