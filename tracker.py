from tkinter import *
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser
import os

root = Tk()
root.title("Phone Number Tracker")
root.geometry("385x594+300+200")
root.resizable(False, False)
root.configure(bg='#96BFFF')

# OpenCage API key (replace with your actual API key)
key = open('api.txt', 'r').read().strip()

def track():
    enter_nb = entry.get()
    print(f"Entered number: {enter_nb}")  # Debugging: Show the entered number
    try:
        # Parse the entered phone number
        number = phonenumbers.parse(enter_nb)
        print(f"Parsed number: {number}")  # Debugging: Show the parsed number

        # Get the location of the phone number
        location = geocoder.description_for_number(number, "en")
        print(f"Location: {location}")  # Debugging: Show the location description
        country.config(text=location)

        # Get the carrier (SIM) information
        service = carrier.name_for_number(number, "en")
        print(f"Carrier: {service}")  # Debugging: Show carrier information
        sim.config(text=service)

        # Use OpenCage API to get the latitude and longitude for the location
        geocoder_api = OpenCageGeocode(key)
        results = geocoder_api.geocode(location)

        if results and len(results) > 0:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            print(f"Latitude: {lat}, Longitude: {lng}")  # Debugging: Show lat/lng

            # Create a Folium map centered on the latitude and longitude
            mymap = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=location).add_to(mymap)

            # Save the map as an HTML file and open it in a browser
            mymap.save("mylocation.html")
            print("Map generated successfully as mylocation.html")
        else:
            print("Location not found.")
            country.config(text="Location not found.")
            sim.config(text="")

    except phonenumbers.NumberParseException:
        country.config(text="Invalid number")
        sim.config(text="")
    except Exception as e:
        print(f"An error occurred: {e}")
        country.config(text="Error occurred")
        sim.config(text="")

def open_map():
    # Open the saved map in the default web browser if it exists
    if os.path.exists("mylocation.html"):
        webbrowser.open("mylocation.html")
    else:
        print("mylocation.html does not exist. Please track a number first.")

# GUI elements
logo = PhotoImage(file="search.png")
Label(root, image=logo, bg='#96BFFF').place(x=135, y=40)

heading = Label(root, text="Phone No. Tracker", font="arial 20 bold", bg='#96BFFF', fg="#39281E")
heading.place(x=90, y=190)

entry = StringVar()
entry_nb = Entry(root, width=17, font="arial 20", textvariable=entry, justify="center", bd=0, bg='#2C3541', fg="white")
entry_nb.place(x=54, y=250)

search_button = PhotoImage(file="search_icon.png")
btn = Button(root, image=search_button, bg='#96BFFF', bd=0, cursor="hand2", command=track, activebackground='#ED8051')
btn.place(x=155, y=308)

country = Label(root, text="Country", font="arial 14 bold", bg='#96BFFF', fg="black")
country.place(x=55, y=370)

sim = Label(root, text="SIM", font="arial 14 bold", bg='#96BFFF', fg="#39281E")
sim.place(x=255, y=370)

open_map_btn = Button(root, text="Location", width=10, cursor="hand2", font="arial 14 bold", bg='#96BFFF', fg="#39281E", command=open_map, activebackground='#ED8051')
open_map_btn.place(x=125, y=430)

root.mainloop()
