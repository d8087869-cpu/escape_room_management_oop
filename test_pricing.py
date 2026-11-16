from datetime import datetime
from models import Room, Booking
from pricing_manager import PricingManager


room = Room(
    "R001",
    "The Lab",
    "Easy",
    60,
    2,
    8,
    80,
    True
)

pricing = PricingManager()


# regular price
price = pricing.calculate_price(room, 4, "2026-11-17")
print("Regular price:", price)


# group discount
price = pricing.calculate_price(room, 5, "2026-11-17")
print("Group price:", price)


# weekend price
price = pricing.calculate_price(room, 4, "2026-11-20")
print("Weekend price:", price)


# cancelle check
booking = Booking(
    "B001",
    "David Cohen",
    "R001",
    "2026-11-20",
    "18:00",
    4,
    320.0,
    "Active",
    0.0
)

current_datetime = datetime(2026, 11, 20, 10, 0)

fee = pricing.calculate_cancellation_fee(
    booking,
    current_datetime
)

print("Cancellation fee:", fee)