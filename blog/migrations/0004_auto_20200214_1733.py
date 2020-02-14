# Generated by Django 3.0.3 on 2020-02-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200214_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tipo',
        ),
        migrations.AddField(
            model_name='post',
            name='tipos',
            field=models.CharField(choices=[('AT', 'Atualizações'), ('PR', 'Projetos')], default=None, max_length=2),
        ),
    ]