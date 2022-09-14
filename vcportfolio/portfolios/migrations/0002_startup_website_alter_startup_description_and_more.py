# Generated by Django 4.1.1 on 2022-09-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='website',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='industry',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
