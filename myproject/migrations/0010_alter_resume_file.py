# Generated by Django 4.2.3 on 2023-07-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0009_alter_portfolio_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='resume'),
        ),
    ]
