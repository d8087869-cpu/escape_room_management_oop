import json
from models import Room, Booking


class DataManager:
    def __init__(self, rooms_file, bookings_file):
        self.rooms_file = rooms_file
        self.bookings_file = bookings_file

    def load_rooms(self):
        with open(self.rooms_file, "r", encoding="utf-8") as file:
            rooms_data = json.load(file)
        rooms = []
        for room_data in rooms_data:
            room = Room.from_dict(room_data)
            rooms.append(room)
        return rooms


    def load_bookings(self):
        with open(self.bookings_file, "r", encoding="utf-8") as file:
            bookings_data = json.load(file)
        bookings = []
        for booking_data in bookings_data:
            booking = Booking.from_dict(booking_data)
            bookings.append(booking)
        return bookings


    def save_rooms(self, rooms):
        rooms_data = []
        for room in rooms:
            rooms_data.append(room.to_dict())
        with open(self.rooms_file, "w", encoding="utf-8") as file:
            json.dump(rooms_data, file, indent=4, ensure_ascii=False)


    def save_bookings(self, bookings):
        bookings_data = []
        for booking in bookings:
            bookings_data.append(booking.to_dict())
        with open(self.bookings_file, "w", encoding="utf-8") as file:
            json.dump(bookings_data, file, indent=4, ensure_ascii=False)