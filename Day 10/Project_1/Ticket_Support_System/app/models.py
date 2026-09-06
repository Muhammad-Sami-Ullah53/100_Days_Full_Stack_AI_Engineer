from dataclasses import dataclass


@dataclass
class Ticket:
    ticket_id: int
    customer: str
    email: str
    message: str