# Generated by Django 3.0.7 on 2020-06-30 02:04

from django.db import migrations


def load_data(apps, schema_editor):
    VoyageType = apps.get_model('seatime', 'VoyageType')
    inland_waterways = VoyageType(type='Inland Waterways')
    inland_waterways.save()
    coastal = VoyageType(type='Coastal')
    coastal.save()
    open_ocean = VoyageType(type='Open Ocean')
    open_ocean.save()
    near_ocean = VoyageType(type='Near Coastal')
    near_ocean.save()
    other = VoyageType(type='Other/Unknown')
    other.save()

    WorkdayType = apps.get_model('seatime', 'WorkdayType')
    eight = WorkdayType(type='8 Hour Workday (Straight Time)')
    eight.save()
    twelve = WorkdayType(type='12 Hour Workday (Time and One Half)')
    twelve.save()

    StaffPosition = apps.get_model('seatime', 'StaffPosition')
    chief_eng = StaffPosition(title='Chief Engineer')
    chief_eng.save()
    chief_eng_modu = StaffPosition(title='Chief Engineer MODU')
    chief_eng_modu.save()
    chief_eng_ufiv = StaffPosition(title='Chief Engineer UFIV')
    chief_eng_ufiv.save()
    chief_eng_osv = StaffPosition(title='Chief Engineer OSV')
    chief_eng_osv.save()
    first_eng = StaffPosition(title='First Engineer')
    first_eng.save()
    second_eng = StaffPosition(title='Second Engineer')
    second_eng.save()
    thirdeng = StaffPosition(title='Third Engineer')
    thirdeng.save()
    qmed = StaffPosition(title='QMED')
    qmed.save()
    student = StaffPosition(title='Student or Apprentice')
    student.save()

    captain = StaffPosition(title='Master')
    captain.save()
    chiefmate = StaffPosition(title='Chief Mate')
    chiefmate.save()
    secondmate = StaffPosition(title='Second Mate')
    secondmate.save()
    thirdmate = StaffPosition(title='Third Mate')
    thirdmate.save()
    ableseaman = StaffPosition(title='Able Seaman')
    ableseaman.save()
    ordinaryseaman = StaffPosition(title='Ordinary Seaman')
    ordinaryseaman.save()
    tankerman = StaffPosition(title='Tankerman')
    tankerman.save()

    Vessel = apps.get_model('seatime', 'Vessel')
    aplChina = Vessel(name='APL China', official_number='9074389')
    aplChina.save()


class Migration(migrations.Migration):
    dependencies = [
        ('seatime', '0006_auto_20200418_1414'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]