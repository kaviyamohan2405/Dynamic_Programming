import streamlit as st

# Define the Taxi class
class Taxi:
    def __init__(self, id, current_location='A'):
        self.id = id
        self.current_location = current_location
        self.earnings = 0
        self.is_available = True

    def update_location(self, new_location):
        self.current_location = new_location

    def update_earnings(self, amount):
        self.earnings += amount

    def set_availability(self, status):
        self.is_available = status

# Define the TaxiFleet class
class TaxiFleet:
    def __init__(self, num_taxis=4):
        self.taxis = [Taxi(id=i+1) for i in range(num_taxis)]

    def get_free_taxis(self):
        return [taxi for taxi in self.taxis if taxi.is_available]

    def get_taxi_by_location(self, location):
        return [taxi for taxi in self.taxis if taxi.current_location == location]

    def allocate_taxi(self, pickup_point):
        free_taxis = self.get_free_taxis()
        if not free_taxis:
            return None  # No taxis available
        taxis_at_location = self.get_taxi_by_location(pickup_point)
        if taxis_at_location:
            return min(taxis_at_location, key=lambda x: x.earnings)
        return self.find_nearest_taxi(pickup_point)

    def find_nearest_taxi(self, pickup_point):
        # Simplified for this example, needs actual implementation
        return min(self.taxis, key=lambda x: abs(ord(x.current_location) - ord(pickup_point)))

# Define the BookingRequest class
class BookingRequest:
    def __init__(self, pickup_point, drop_point):
        self.pickup_point = pickup_point
        self.drop_point = drop_point
        self.distance = self.calculate_distance()
        self.fare = self.calculate_fare()

    def calculate_distance(self):
        return abs(ord(self.drop_point) - ord(self.pickup_point)) * 15

    def calculate_fare(self):
        base_fare = 100
        additional_fare = max(0, self.distance - 5) * 10
        return base_fare + additional_fare

    def is_valid_booking(self):
        return self.distance > 0

# Initialize the Taxi Fleet
fleet = TaxiFleet()

# Streamlit Application
st.title("Call Taxi Booking Application")

# Input form for booking
pickup_point = st.selectbox("Select Pickup Point", ["A", "B", "C", "D", "E", "F"])
drop_point = st.selectbox("Select Drop Point", ["A", "B", "C", "D", "E", "F"])

if st.button("Book Taxi"):
    booking = BookingRequest(pickup_point, drop_point)
    
    if booking.is_valid_booking():
        taxi = fleet.allocate_taxi(pickup_point)
        if taxi:
            taxi.update_location(drop_point)
            taxi.update_earnings(booking.fare)
            taxi.set_availability(False)  # Taxi is now busy
            st.success(f"Booking confirmed with Taxi ID {taxi.id}. Fare: Rs.{booking.fare}")
        else:
            st.error("Booking rejected. No taxis available.")
    else:
        st.error("Invalid booking request.")

# Display the status of taxis
st.subheader("Taxi Fleet Status")
for taxi in fleet.taxis:
    status = "Available" if taxi.is_available else "Busy"
    st.write(f"Taxi ID {taxi.id}: Location {taxi.current_location}, Earnings Rs.{taxi.earnings}, Status: {status}")

# To run the app, use the following command in the terminal:
# streamlit run app.py
