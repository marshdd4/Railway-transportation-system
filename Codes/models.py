class Ticket:
    def __init__(
        self,
        full_name: str,
        username: str,
        train_name: str,
        route: str,
        ticket_count: int,
        price_each: int
    ):
        self.full_name = full_name
        self.username = username
        self.train_name = train_name
        self.route = route
        self.ticket_count = ticket_count
        self.price_each = price_each
        self.total_price = ticket_count * price_each
