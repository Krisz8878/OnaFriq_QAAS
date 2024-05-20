import requests

# Base URL for the Restful-Booker API
base_url = "https://restful-booker.herokuapp.com"

def create_auth_token():
    auth_url = f"{base_url}/auth"
    auth_payload = {
        "username": "admin",
        "password": "password123"
    }
    auth_response = requests.post(auth_url, json=auth_payload)
    if auth_response.status_code == 200:
        token = auth_response.json()["token"]
        return token
    else:
        return None

# a) Create a booking
create_booking_url = f"{base_url}/booking"
create_booking_payload = {
    "firstname": "Christian",
    "lastname": "Utsu",
    "totalprice": 1000,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2024-05-14",
        "checkout": "2024-05-16"
    },
    "additionalneeds": "Blanket"
}

create_booking_response = requests.post(create_booking_url, json=create_booking_payload)

if create_booking_response.status_code == 200:
    booking_id = create_booking_response.json()["bookingid"]
    print(f"Booking created successfully. Booking ID: {booking_id}")

    # b) Get the booking created above
    get_booking_url = f"{base_url}/booking/{booking_id}"
    get_booking_response = requests.get(get_booking_url)

    if get_booking_response.status_code == 200:
        booking_details = get_booking_response.json()
        print("Booking Details:")
        print(booking_details)
    else:
        print("Failed to retrieve booking details.")

    # Get authentication token
    auth_token = create_auth_token()
    if auth_token:
        # c) Update the booking (change checkout date and additional needs)
        update_booking_url = f"{base_url}/booking/{booking_id}"
        update_booking_payload = {
            "firstname": "Christian",
            "lastname": "Utsu",
            "totalprice": 1000,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-05-14",
                "checkout": "2024-05-20"  # Updated checkout date
            },
            "additionalneeds": "Blankets, Towels"  # Updated additional needs
        }

        update_booking_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={auth_token}"
        }

        update_booking_response = requests.put(update_booking_url, headers=update_booking_headers, json=update_booking_payload)

        if update_booking_response.status_code == 200:
            print("Booking updated successfully.")
            print("Updated Booking Details:")
            print(update_booking_payload)
        else:
            print("Failed to update booking.")
    else:
        print("Failed to get authentication token.")

else:
    print("Failed to create booking.")