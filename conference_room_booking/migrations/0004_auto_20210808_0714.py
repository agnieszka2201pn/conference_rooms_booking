# Generated by Django 3.2.6 on 2021-08-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_room_booking', '0003_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('reservation_date', 'room_id_id')},
        ),
    ]
