# Generated by Django 3.0.8 on 2020-08-02 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200801_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='Product',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
