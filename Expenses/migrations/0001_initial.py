# Generated by Django 4.2.7 on 2023-12-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('category', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]
