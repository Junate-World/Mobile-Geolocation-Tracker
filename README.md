# Mobile Geolocation Tracker

A simple Tkinter application that tracks the location of a phone number and displays it on a map using the OpenCage Geocode API and Folium.

## Features

- Enter a phone number to get the location and carrier information.
- Displays the location on a map saved as an HTML file.
- Opens the generated map in a web browser.

## Requirements

- Python 3.x
- Tkinter
- phonenumbers
- folium
- opencage-geocoder

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Junate-World/Mobile-Geolocation-Tracker.git
   cd Mobile-Geolocation-Tracker

Install the required packages:

bash

pip install phonenumbers folium opencage-geocoder

Obtain an API key from OpenCage Data and save it in a file named api.txt in the project directory.

Place your images (search.png and search_icon.png) in the project directory.

Run the application:

bash

python tracker.py
Enter a phone number in the input field and click the search button.

The application will display the country and SIM information and generate a map showing the location of the phone number. The map will open automatically in your web browser.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
OpenCage Data for providing the geocoding API.
Folium for easy map visualization.
phonenumbers for phone number parsing and validation.#   M o b i l e - G e o l o c a t i o n - T r a c k e r  
 