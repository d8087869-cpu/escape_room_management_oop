from datetime import datetime

class PricingManager:
    def calculate_price(self, room, players, booking_date):
        base_price = players * room.price_per_player

        if players >= 7:
            discount = 0.15

        elif players >= 5:
            discount = 0.10

        else:
            discount = 0

        total_price = base_price * (1 - discount)

        booking_day = datetime.strptime(
            booking_date, "%Y-%m-%d"
        ).weekday()

        if booking_day in [4, 5]:
            total_price *= 1.15

        return round(total_price, 2)

    def calculate_cancellation_fee(self, booking, current_datetime):
        booking_datetime = datetime.strptime(
            f"{booking.booking_date} {booking.start_time}",
            "%Y-%m-%d %H:%M")

        time_remaining = booking_datetime - current_datetime
        hours_remaining = time_remaining.total_seconds() / 3600

        if hours_remaining > 24:
            cancellation_fee = 0

        elif hours_remaining >= 6:
            cancellation_fee = booking.total_price * 0.25

        else:
            cancellation_fee = booking.total_price * 0.50

        return round(cancellation_fee, 2)