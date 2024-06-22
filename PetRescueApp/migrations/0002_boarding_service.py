# Generated by Django 4.1.7 on 2023-03-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetRescueApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='boarding_service',
            fields=[
                ('b_service_id', models.AutoField(primary_key=True, serialize=False)),
                ('pet_type', models.CharField(max_length=50)),
                ('cost', models.IntegerField(default=0)),
                ('Ac_login_id', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tbl_boarding_service',
            },
        ),
    ]
