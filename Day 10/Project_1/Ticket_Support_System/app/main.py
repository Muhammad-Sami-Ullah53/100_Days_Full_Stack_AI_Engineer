# from app.models import Ticket


# ticket = Ticket(
#     ticket_id=101,
#     customer="Ali",
#     email="ali@example.com",
#     message="My payment failed"
# )

# print(ticket)

from app.storage import load_tickets


tickets = load_tickets("data/tickets.json")

print(tickets)