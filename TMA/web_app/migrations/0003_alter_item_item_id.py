# Generated by Django 5.0.4 on 2024-04-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_remove_item_id_item_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]