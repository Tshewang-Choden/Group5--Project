# Generated by Django 4.0 on 2022-01-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userfname', models.CharField(max_length=20)),
                ('usersname', models.CharField(max_length=20)),
                ('useremailid', models.CharField(max_length=20, unique=True)),
                ('message', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'UserDetails',
                'verbose_name_plural': 'UserDetailss',
            },
        ),
    ]
