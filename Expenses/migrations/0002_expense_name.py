# Generated by Django 4.2.7 on 2023-12-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expenses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='name',
            field=models.CharField(default='default expense name', max_length=255),
        ),
    ]
