# Generated by Django 3.0.3 on 2020-03-01 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('rank', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('official_number', models.CharField(max_length=64)),
                ('tonnage', models.CharField(max_length=64)),
                ('propulsion', models.CharField(max_length=64)),
                ('hp', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='VoyageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='WorkdayType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart_date', models.DateField()),
                ('arrival_date', models.DateField()),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seatime.StaffPosition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vessel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seatime.Vessel')),
                ('voyage_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seatime.VoyageType')),
                ('workday_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seatime.WorkdayType')),
            ],
        ),
        migrations.CreateModel(
            name='MarinerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('citizenship_cntry', models.CharField(max_length=255)),
                ('residence_state', models.CharField(max_length=255)),
                ('mariner_ref_num', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MarinerDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mmc_doc_num', models.PositiveIntegerField()),
                ('mmc_issue_date', models.DateField()),
                ('mmc_expr_date', models.DateField()),
                ('med_ntl_expr_date', models.DateField()),
                ('med_stcw_expr_date', models.DateField()),
                ('med_pilot_expr_date', models.DateField()),
                ('twic_expr_date', models.DateField()),
                ('basic_training_expr_date', models.DateField()),
                ('advanced_fire_expr_date', models.DateField()),
                ('first_aid_cpr_expr_date', models.DateField()),
                ('passport_expr_date', models.DateField()),
                ('drug_test_compliant', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
