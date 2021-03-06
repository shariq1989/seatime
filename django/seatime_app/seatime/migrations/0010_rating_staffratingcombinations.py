# Generated by Django 3.0.7 on 2020-07-02 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatime', '0009_auto_20200702_0314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='StaffRatingCombinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionRating', models.ManyToManyField(to='seatime.Rating')),
                ('staffPosition', models.ManyToManyField(to='seatime.StaffPosition')),
            ],
        ),
    ]
