# Generated by Django 3.0.3 on 2020-02-16 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_delete_auth_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(max_length=500)),
            ],
        ),
    ]
