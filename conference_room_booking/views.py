from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from conference_room_booking.models import Conference_Room, Reservation

class MainView(View):
    def get(self, request):
        return render(request,'main_form.html')

class AddRoom(View):
    def get(self,request):
        return render(request, 'add_room.html')

    def post(self,request):
        new_room_name = request.POST.get('room_name')
        new_room_size = int(request.POST.get('room_size'))
        beamer = request.POST.get('beamer') == 'on'

        check_room = Conference_Room.objects.filter(room_name=new_room_name)
        if check_room:
            return HttpResponse ("this room already exists")
        else:
            if new_room_name and new_room_size > 0:
                Conference_Room.objects.create(room_name=new_room_name, room_size=new_room_size, beamer_available=beamer)
                return render(request, 'main_form.html')
            else:
                return HttpResponse ("Provide correct data")

class ShowRooms(View):
    def get(self, request):
        list_of_rooms = Conference_Room.objects.all()
        return render(request, 'list_of_rooms.html', {'list_of_rooms':list_of_rooms})

class DeleteRoom(View):
    def get(self, request, room_id):
        Conference_Room.objects.filter(id=room_id).delete()
        return render(request, 'main_form.html')

class ModifyRoom(View):
    def get(self,request, room_id):
        room = Conference_Room.objects.get(id=room_id)
        return render(request, 'modify_room.html', {'room': room})

    def post(self,request, room_id):
        new_room_name = request.POST.get('room_name')
        new_room_size = int(request.POST.get('room_size'))
        beamer = request.POST.get('beamer') == 'on'

        if new_room_name and new_room_size > 0:
            Conference_Room.objects.filter(id=room_id).update(room_name=new_room_name, room_size=new_room_size,
                                           beamer_available=beamer)
            return render(request, 'main_form.html')
        else:
            return HttpResponse("Provide correct data")


class ReserveRoom(View):
    def get(self, request, room_id):
        reservations = Reservation.objects.filter(room_id=room_id)
        room = Conference_Room.objects.get(pk=room_id)
        return render(request, 'reservation_form.html', {'reservations':reservations, 'room':room})

    def post(self, request, room_id):
        reservation_date = request.POST.get('reservation_date')
        comment = request.POST.get('comment')

        if Reservation.objects.filter(room_id=room_id, reservation_date=reservation_date):
            return HttpResponse('Such reservation already exists. Please choose a different room or date')
        else:
            Reservation.objects.create(reservation_date=reservation_date, comment=comment, room_id=Conference_Room.objects.get(id=room_id))
            return render(request,'main_form.html')

class ConferenceRoomDetails(View):
    def get(self, request, room_id):
        chosen_room = Conference_Room.objects.get(id=room_id)
        reservations_to_display = chosen_room.reservation_set.all()
        return render(request, 'room_details.html', {'room':chosen_room, 'reservations':reservations_to_display })