from models import Room, Booking


# create room
room = Room(
    "R001", "The Lab", "Easy",
    60, 2, 8, 80, True
)

print(room.name)
print(room.is_valid_players(5))

room.deactivate()
print(room.is_active)


# convert room to dictionary
room_data = room.to_dict()
print(room_data)

# create room from dictionary
new_room = Room.from_dict(room_data)
print(new_room.name)


# create booking
booking = Booking(
    "B001", "David Cohen", "R001",
    "2026-11-20", "10:00", 4,
    320.0, "Active", 0.0
)

booking.cancel(80.0)

print(booking.status)
print(booking.cancellation_fee)


# convert booking to dictionary
booking_data = booking.to_dict()
print(booking_data)

# create booking from dictionary
new_booking = Booking.from_dict(booking_data)
print(new_booking.customer_name)