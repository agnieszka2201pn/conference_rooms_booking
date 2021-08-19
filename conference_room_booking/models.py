from django.db import models


class Conference_Room(models.Model):
    room_name = models.CharField(max_length=255, unique=True)
    room_size = models.IntegerField()
    beamer_available = models.BooleanField(null=True)

class Reservation(models.Model):
    reservation_date = models.DateField(null=True)
    room_id = models.ForeignKey(Conference_Room, on_delete=models.CASCADE)
    comment = models.TextField(null=True)

    class Meta:
        unique_together = ('reservation_date', 'room_id_id')
    