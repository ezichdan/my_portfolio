# Generated by Django 4.2.3 on 2023-07-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0007_alter_portfolio_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='proj_img1',
            field=models.ImageField(blank=True, null=True, upload_to='projects/proj_img1'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='proj_img2',
            field=models.ImageField(blank=True, null=True, upload_to='projects/proj_img2'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='proj_img3',
            field=models.ImageField(blank=True, null=True, upload_to='projects/proj_img3'),
        ),
    ]
