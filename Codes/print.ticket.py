import os
from datetime import datetime
from models import Ticket

def generate_ticket_file(ticket_info: dict):
    try:
        os.makedirs("tickets", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M")

        filename = f"tickets/ticket_{ticket_info['username']}_{timestamp}.txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write("########################\n")
            file.write("       TRAIN TICKET\n")
            file.write("########################\n\n")

            file.write(f"Passenger Name : {ticket_info['full_name']}\n")
            file.write(f"Username       : {ticket_info['username']}\n\n")

            file.write(f"Train Name     : {ticket_info['train_name']}\n")
            file.write(f"Route          : {ticket_info['route']}\n\n")

            file.write(f"Tickets Count  : {ticket_info['ticket_count']}\n")
            file.write(f"Price (Each)   : {ticket_info['price_each']}\n")
            file.write(f"Total Price    : {ticket_info['total_price']}\n\n")

            file.write(f"Purchase Time  : {datetime.now()}\n\n")

            file.write("########################\n")
            file.write("   Have a safe journey!\n")
            file.write("########################\n")

        return {"status": True,"message": "Ticket generated successfully","file_path": filename}

    except PermissionError:
        return {"status": False,"message": "Permission denied while creating ticket file"}

    except KeyError as e:
        return {"status": False,"message": f"Missing ticket info field: {e}"}

    except Exception:
        return {"status": False,"message": "Unexpected error occurred while generating ticket"}

if __name__ == "__main__":
    test_ticket = Ticket(
        "Ali Ahmadi",
        "ali123",
        "Express 7",
        "Tehran -> Mashhad",
        2,
        150000
    )
    print(generate_ticket_file(test_ticket))