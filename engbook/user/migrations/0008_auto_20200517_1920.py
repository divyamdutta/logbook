# Generated by Django 3.0.5 on 2020-05-17 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200517_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='field_study',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user.FieldStudy'),
        ),
    ]
