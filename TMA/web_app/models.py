from django.db import models


class Item(models.Model):
    item_group = models.CharField(max_length=255)
    unit_of_measurement = models.CharField(max_length=20,
                                           choices=[('Meter', 'Meter'), ('Kilogram', 'Kilogram'), ('Liter', 'Liter'),
                                                    ('Piece', 'Piece')])
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price_without_vat = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    storage_location = models.CharField(max_length=255, blank=True)
    contact_person = models.TextField(blank=True)
    photo = models.ImageField(upload_to='web_app/photos/', blank=True)
    item_id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'web_app_item'
