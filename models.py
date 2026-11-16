class Room:
    def __init__(self, room_id, name, difficulty, duration,
                 min_players, max_players, price_per_player, is_active):

        self.room_id = room_id
        self.name = name
        self.difficulty = difficulty
        self.duration = duration
        self.min_players = min_players
        self.max_players = max_players
        self.price_per_player = price_per_player
        self.is_active = is_active

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def is_valid_players(self, players):
        return self.min_players <= players <= self.max_players

    def to_dict(self):
        return {
            "room_id": self.room_id,
            "name": self.name,
            "difficulty": self.difficulty,
            "duration": self.duration,
            "min_players": self.min_players,
            "max_players": self.max_players,
            "price_per_player": self.price_per_player,
            "is_active": self.is_active
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["room_id"],
            data["name"],
            data["difficulty"],
            data["duration"],
            data["min_players"],
            data["max_players"],
            data["price_per_player"],
            data["is_active"])
        
        
        
class Booking:
    def __init__(self, booking_id, customer_name, room_id,
                 booking_date, start_time, players, total_price,
                 status, cancellation_fee):

        self.booking_id = booking_id
        self.customer_name = customer_name
        self.room_id = room_id
        self.booking_date = booking_date
        self.start_time = start_time
        self.players = players
        self.total_price = total_price
        self.status = status
        self.cancellation_fee = cancellation_fee

    def cancel(self, fee):
        self.status = "Cancelled"
        self.cancellation_fee = fee

    def update_details(self, booking_date, start_time, players, total_price):
        self.booking_date = booking_date
        self.start_time = start_time
        self.players = players
        self.total_price = total_price

    def to_dict(self):
        return {
            "booking_id": self.booking_id,
            "customer_name": self.customer_name,
            "room_id": self.room_id,
            "booking_date": self.booking_date,
            "start_time": self.start_time,
            "players": self.players,
            "total_price": self.total_price,
            "status": self.status,
            "cancellation_fee": self.cancellation_fee}

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["booking_id"],
            data["customer_name"],
            data["room_id"],
            data["booking_date"],
            data["start_time"],
            data["players"],
            data["total_price"],
            data["status"],
            data["cancellation_fee"])