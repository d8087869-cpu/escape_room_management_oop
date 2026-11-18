from datetime import datetime, timedelta
from models import Booking

class BookingManager:
    def __init__(self, rooms, bookings, pricing_manager):
        self.rooms = rooms
        self.bookings = bookings
        self.pricing_manager = pricing_manager

    def get_room(self, room_id):
        for room in self.rooms:
            if room.room_id == room_id:
                return room
        return None

    def validate_booking_time(self, booking_date, start_time, duration):
        try:
            start_datetime = datetime.strptime(
                f"{booking_date} {start_time}",
                "%Y-%m-%d %H:%M")

        except ValueError:
            return False, "Invalid date or time format."

        if start_datetime < datetime.now():
            return False, "Cannot create a booking in the past."

        opening_time = start_datetime.replace(
            hour=10, minute=0, second=0)

        closing_time = start_datetime.replace(
            hour=22, minute=0, second=0)

        end_datetime = start_datetime + timedelta(minutes=duration)

        if start_datetime < opening_time:
            return False, "The complex opens at 10:00."

        if end_datetime > closing_time:
            return False, "The game must finish by 22:00."

        return True, "Valid booking time."

    def check_availability(
        self, room_id, booking_date, start_time,
        exclude_booking_id=None):
        room = self.get_room(room_id)

        if room is None:
            return False

        new_start = datetime.strptime(
            f"{booking_date} {start_time}",
            "%Y-%m-%d %H:%M")

        new_end = new_start + timedelta(
            minutes=room.duration + 15)

        for booking in self.bookings:

            if booking.booking_id == exclude_booking_id:
                continue

            if booking.room_id != room_id:
                continue

            if booking.booking_date != booking_date:
                continue

            if booking.status != "Active":
                continue

            existing_start = datetime.strptime(
                f"{booking.booking_date} {booking.start_time}",
                "%Y-%m-%d %H:%M")

            existing_end = existing_start + timedelta(
                minutes=room.duration + 15)

            if new_start < existing_end and new_end > existing_start:
                return False
        return True

    def get_next_booking_id(self):
        max_id = 0

        for booking in self.bookings:
            number = int(booking.booking_id[1:])

            if number > max_id:
                max_id = number

        return f"B{max_id + 1:03d}"

    def create_booking(
        self, customer_name, room_id,
        booking_date, start_time, players):
        customer_name = customer_name.strip()
        room_id = room_id.strip().upper()

        if not customer_name:
            return False, "Customer name cannot be empty."

        room = self.get_room(room_id)

        if room is None:
            return False, "Room not found."

        if not room.is_active:
            return False, "This room is currently inactive."

        if not room.is_valid_players(players):
            return False, "Number of players is not allowed for this room."

        is_valid, message = self.validate_booking_time(
            booking_date, start_time, room.duration)

        if not is_valid:
            return False, message

        if not self.check_availability(
            room_id, booking_date, start_time):
            return False, "Room is already booked at this time."

        total_price = self.pricing_manager.calculate_price(
            room, players, booking_date)

        booking_id = self.get_next_booking_id()

        new_booking = Booking(
            booking_id,
            customer_name,
            room_id,
            booking_date,
            start_time,
            players,
            total_price,
            "Active",
            0.0)

        self.bookings.append(new_booking)

        return True, f"Booking created successfully! ID: {booking_id}"