# Generated by Django 4.0.4 on 2023-11-07 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_rename_category_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
    ]