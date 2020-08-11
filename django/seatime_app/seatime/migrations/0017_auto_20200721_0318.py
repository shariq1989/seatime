# Generated by Django 3.0.7 on 2020-07-21 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seatime', '0016_post_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('designation', models.ManyToManyField(to='seatime.Designation')),
            ],
        ),
        migrations.RemoveField(
            model_name='staffposition',
            name='ratings',
        ),
        migrations.RemoveField(
            model_name='voyage',
            name='position',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='StaffPosition',
        ),
        migrations.AddField(
            model_name='voyage',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seatime.Designation'),
        ),
        migrations.AddField(
            model_name='voyage',
            name='rank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seatime.Rank'),
            preserve_default=False,
        ),
    ]
