"""
seed_data.py

Run this file ONCE to load your real, manually-collected apartment
listings into apartments.json.

Commute time gets filled in automatically via the distance API.
After running this once, app.py loads straight from apartments.json.
"""

from apartment import Apartment
from tracker import ApartmentTracker
from distance_api import get_commute_minutes
from storage import save_to_file

ORIGIN_ADDRESS = "Sector 42 Gurgaon"

RAW_LISTINGS = [
    # ==========================================
    # Sector 45, Gurgaon
    # ==========================================
    {"name": "Unitech Greenwood City 3BHK", "address": "Sector 45, Gurgaon, Haryana", "rent": 75000, "bedrooms": 3, "notes": "Gated society, 24x7 security, semi-furnished"},
    {"name": "Royal Residency 3BHK", "address": "Sector 45, Gurgaon, Haryana", "rent": 70000, "bedrooms": 3, "notes": "Park view, semi-furnished, 7th floor"},
    {"name": "San Marino Apartments 3BHK", "address": "Sector 45, Gurgaon, Haryana", "rent": 47000, "bedrooms": 3, "notes": "Semi-furnished, modular kitchen"},
    {"name": "Ayyachi Apartment 3BHK", "address": "Sector 45, Gurgaon, Haryana", "rent": 46000, "bedrooms": 3, "notes": "Semi-furnished, 1500 sq ft"},
    {"name": "Pratap Yadav Nest 2BHK", "address": "Sector 45, Gurgaon, Haryana", "rent": 42000, "bedrooms": 2, "notes": "Fully furnished, 1400 sq ft"},
    {"name": "Budget 3BHK Sector 45", "address": "Sector 45, Gurgaon, Haryana", "rent": 50000, "bedrooms": 3, "notes": "1650 sq ft, garden view, semi-furnished"},
    {"name": "Apex Flats 1BHK", "address": "Sector 45, Gurgaon, Haryana", "rent": 18000, "bedrooms": 1, "notes": "Furnished, 500 sq ft, park view"},
    {"name": "Huda Plot 2BHK", "address": "Sector 45, Gurgaon, Haryana", "rent": 30000, "bedrooms": 2, "notes": "Independent floor"},
    {"name": "Comdor Cyber Gardens Iris 2BHK", "address": "Sector 45, Gurgaon, Haryana", "rent": 35200, "bedrooms": 2, "notes": "1300 sq ft, semi-furnished, 3 balconies, newly built"},
    {"name": "House 807 Low-Rise 2BHK", "address": "Sector 45, Gurgaon, Haryana", "rent": 35000, "bedrooms": 2, "notes": "1000 sq ft, semi-furnished, 1st floor, near Huda Metro"},
    {"name": "Uday Arden 45 2BHK", "address": "Sector 45, Gurgaon, Haryana", "rent": 46000, "bedrooms": 2, "notes": "891 sq ft, fully furnished, power backup, brand new building"},
    {"name": "Dream Home Floors 1BHK", "address": "Sector 45, Gurgaon, Haryana", "rent": 35000, "bedrooms": 1, "notes": "Furnished, near DPS school and Sector 45 main market"},
    {"name": "Doordarshan Apartments Studio", "address": "Sector 45, Gurgaon, Haryana", "rent": 22000, "bedrooms": 1, "notes": "250 sq ft studio, near Huda City Centre metro & Sector 44"},

    # ==========================================
    # Sector 46, Gurgaon
    # ==========================================
    {"name": "Sector 46 Budget 2BHK", "address": "Sector 46, Gurgaon, Haryana", "rent": 25000, "bedrooms": 2, "notes": "Near metro station"},
    {"name": "Sector 46 PG Single Room", "address": "Sector 46, Gurgaon, Haryana", "rent": 9000, "bedrooms": 1, "notes": "Shared society, meals included"},
    {"name": "Green View Apartments 2BHK", "address": "Sector 46, Gurgaon, Haryana", "rent": 35000, "bedrooms": 2, "notes": "Semi-furnished, lift available"},
    {"name": "Sector 46 Studio", "address": "Sector 46, Gurgaon, Haryana", "rent": 15000, "bedrooms": 1, "notes": "Compact studio, good for single occupant"},
    {"name": "RWA Sector 46 1BHK", "address": "Sector 46, Gurgaon, Haryana", "rent": 24000, "bedrooms": 1, "notes": "900 sq ft, near big Huda market, international school & park"},
    {"name": "Sector 46 Luxury Flat 1BHK", "address": "Sector 46, Gurgaon, Haryana", "rent": 35000, "bedrooms": 1, "notes": "600 sq ft, central AC, swimming pool access, full power backup"},
    {"name": "Huda Staff Colony 1RK", "address": "Sector 46, Gurgaon, Haryana", "rent": 22000, "bedrooms": 1, "notes": "Furnished room, split AC, inverter backup, lift available"},
    {"name": "Sector 46 Independent Villa 1BHK", "address": "Sector 46, Gurgaon, Haryana", "rent": 27000, "bedrooms": 1, "notes": "918 sq ft, 2 bathrooms, 2 balconies, peaceful locality"},

    # ==========================================
    # Sector 44, Gurgaon
    # ==========================================
    {"name": "DLF Phase Residency 2BHK", "address": "Sector 44, Gurgaon, Haryana", "rent": 38000, "bedrooms": 2, "notes": "Near DLF Cyber Hub"},
    {"name": "Sector 44 PG Twin Sharing", "address": "Sector 44, Gurgaon, Haryana", "rent": 11000, "bedrooms": 1, "notes": "Twin sharing, wifi included"},
    {"name": "Heritage Homes 3BHK", "address": "Sector 44, Gurgaon, Haryana", "rent": 62000, "bedrooms": 3, "notes": "Fully furnished, premium society"},

    # ==========================================
    # Sector 47, Gurgaon
    # ==========================================
    {"name": "Sector 47 Independent Floor 2BHK", "address": "Sector 47, Gurgaon, Haryana", "rent": 28000, "bedrooms": 2, "notes": "Independent entry, semi-furnished"},
    {"name": "Vatika Residency 3BHK", "address": "Sector 47, Gurgaon, Haryana", "rent": 55000, "bedrooms": 3, "notes": "Clubhouse, pool access"},
    {"name": "Sector 47 Budget 1BHK", "address": "Sector 47, Gurgaon, Haryana", "rent": 14000, "bedrooms": 1, "notes": "Unfurnished, ground floor"},
    {"name": "Uniworld Gardens II 2BHK", "address": "Sector 47, Gurgaon, Haryana", "rent": 38000, "bedrooms": 2, "notes": "997 sq ft, semi-furnished, 7th floor, modular kitchen"},
    {"name": "Uniworld Gardens II High-Rise 2BHK", "address": "Sector 47, Gurgaon, Haryana", "rent": 35000, "bedrooms": 2, "notes": "973 sq ft, semi-furnished, 14th floor, gym & pool access"},
    {"name": "New Gurgaon Builder Floor 2BHK", "address": "Sector 47, Gurgaon, Haryana", "rent": 47000, "bedrooms": 2, "notes": "1200 sq ft, furnished, 2 balconies"},
    {"name": "Huda EWS Flats 1BHK", "address": "Sector 47, Gurgaon, Haryana", "rent": 27000, "bedrooms": 1, "notes": "600 sq ft, park facing, peaceful neighborhood"},

    # ==========================================
    # Sector 48, Gurgaon
    # ==========================================
    {"name": "Sector 48 PG Single Room", "address": "Sector 48, Gurgaon, Haryana", "rent": 10000, "bedrooms": 1, "notes": "AC room, food included"},
    {"name": "Central Park Resorts 2BHK", "address": "Sector 48, Gurgaon, Haryana", "rent": 45000, "bedrooms": 2, "notes": "Premium amenities, gym"},
    {"name": "Sector 48 Family Flat 3BHK", "address": "Sector 48, Gurgaon, Haryana", "rent": 58000, "bedrooms": 3, "notes": "Family friendly society"},
    {"name": "Central Park The Room Studio", "address": "Sector 48, Gurgaon, Haryana", "rent": 72000, "bedrooms": 1, "notes": "835 sq ft, luxury serviced studio, fully furnished"},
    {"name": "Parsvnath Green Ville 2BHK", "address": "Sector 48, Gurgaon, Haryana", "rent": 40000, "bedrooms": 2, "notes": "1600 sq ft, 5th floor with terrace, park facing"},
    {"name": "Bestech Park View City 3BHK", "address": "Sector 48, Gurgaon, Haryana", "rent": 57000, "bedrooms": 3, "notes": "1776 sq ft, semi-furnished, servant room, modular kitchen"},
    {"name": "Vipul Greens 3BHK", "address": "Sector 48, Gurgaon, Haryana", "rent": 60000, "bedrooms": 3, "notes": "1630 sq ft, semi-furnished, servant room, near metro"},

    # ==========================================
    # Sector 43, Gurgaon
    # ==========================================
    {"name": "Millenium Bajrang Society 1BHK", "address": "Sector 43, Gurgaon, Haryana", "rent": 35000, "bedrooms": 1, "notes": "Furnished, 600 sq ft, modular kitchen, central AC"},
    {"name": "Star Floors Villa 2BHK", "address": "Sector 43, Gurgaon, Haryana", "rent": 35000, "bedrooms": 2, "notes": "Furnished, 600 sq ft, modular kitchen, near metro"},
    {"name": "Huda Flats Builder Floor 2BHK", "address": "Sector 43, Gurgaon, Haryana", "rent": 36000, "bedrooms": 2, "notes": "Furnished, 1500 sq ft, 2 balconies"},
    {"name": "Huda Flats Ground Floor 2BHK", "address": "Sector 43, Gurgaon, Haryana", "rent": 47000, "bedrooms": 2, "notes": "Furnished, 900 sq ft, modular kitchen, central AC"},

    # ==========================================
    # Sector 42, Gurgaon
    # ==========================================
    {"name": "Central Park Sector 42 1BHK", "address": "Sector 42, Gurgaon, Haryana", "rent": 38000, "bedrooms": 1, "notes": "Fully furnished, 700 sq ft, park-facing, near origin"},
    {"name": "Sector 42 Studio Apartment", "address": "Sector 42, Gurgaon, Haryana", "rent": 23000, "bedrooms": 1, "notes": "300 sq ft, semi-furnished, ceramic flooring, modular kitchen, central AC"},

    # ==========================================
    # Sector 40, Gurgaon
    # ==========================================
    {"name": "Individual Floors Sector 40 Studio", "address": "Sector 40, Gurgaon, Haryana", "rent": 24000, "bedrooms": 1, "notes": "300 sq ft, furnished studio, modular kitchen, central AC, lift"},
    {"name": "Sector 40 Park Facing 1BHK", "address": "Sector 40, Gurgaon, Haryana", "rent": 27500, "bedrooms": 1, "notes": "600 sq ft, furnished, near main road, hospital and metro"},
    {"name": "Sector 40 Card Access 1RK", "address": "Sector 40, Gurgaon, Haryana", "rent": 22000, "bedrooms": 1, "notes": "475 sq ft, smart TV, power backup, RO, electronic card access"},
    {"name": "Sector 40 Builder Floor 1BHK", "address": "Sector 40, Gurgaon, Haryana", "rent": 21700, "bedrooms": 1, "notes": "900 sq ft, ground floor, park facing, study room included"},

    # ==========================================
    # Sector 39, Gurgaon
    # ==========================================
    {"name": "Unitech Cyber Park 1RK", "address": "Sector 39, Gurgaon, Haryana", "rent": 23500, "bedrooms": 1, "notes": "850 sq ft, furnished with lift, opposite Medanta Hospital & Huda Metro"},
    {"name": "Durga Colony 1BHK", "address": "Sector 39, Gurgaon, Haryana", "rent": 32000, "bedrooms": 1, "notes": "1080 sq ft, newly built, opposite Medanta, near Sector 32 corporates"},
    {"name": "Urban Green Sector 39 1BHK", "address": "Sector 39, Gurgaon, Haryana", "rent": 33000, "bedrooms": 1, "notes": "1050 sq ft, furnished with lift, CCTV, open parking, near Cyber Park"},

    # ==========================================
    # Sector 38, Gurgaon
    # ==========================================
    {"name": "Sector 38 Huda Floor Studio", "address": "Sector 38, Gurgaon, Haryana", "rent": 28000, "bedrooms": 1, "notes": "500 sq ft, furnished brand new studio, split AC, smart TV, near Medanta"},
    {"name": "Sector 38 Villa 1BHK", "address": "Sector 38, Gurgaon, Haryana", "rent": 30000, "bedrooms": 1, "notes": "800 sq ft, semi-furnished independent villa, east facing, open parking"},
    {"name": "Sector 38 Triplex Builder Floor 1BHK", "address": "Sector 38, Gurgaon, Haryana", "rent": 24000, "bedrooms": 1, "notes": "800 sq ft, fully furnished, 2 bathrooms, 2 balconies, behind Medanta"},

    # ==========================================
    # Sector 31, Gurgaon
    # ==========================================
    {"name": "Peach Jasmine Apartments Studio", "address": "Sector 31, Gurgaon, Haryana", "rent": 25000, "bedrooms": 1, "notes": "650 sq ft, elegant modern design, furnished, quiet residential area"},
    {"name": "Sector 31 Builder Floor 1BHK", "address": "Sector 31, Gurgaon, Haryana", "rent": 23000, "bedrooms": 1, "notes": "1260 sq ft, top floor, furnished, 1 balcony, near Sector 31 market"},
    {"name": "Sector 31 Compact Studio", "address": "Sector 31, Gurgaon, Haryana", "rent": 25000, "bedrooms": 1, "notes": "160 sq ft, carpet area, furnished, 1 balcony"},

    # ==========================================
    # Sector 28, Gurgaon
    # ==========================================
    {"name": "Suncity Essel Towers Studio", "address": "Sector 28, Gurgaon, Haryana", "rent": 18000, "bedrooms": 1, "notes": "220 sq ft, furnished, near IFFCO Chowk & MG Road metro, 24x7 security"},
    {"name": "Suncity Essel Towers 2BHK", "address": "Sector 28, Gurgaon, Haryana", "rent": 60000, "bedrooms": 2, "notes": "1210 sq ft, furnished, attached balconies, parking, near MG Road metro"},
    {"name": "Suncity Essel Towers 3BHK", "address": "Sector 28, Gurgaon, Haryana", "rent": 72000, "bedrooms": 3, "notes": "1780 sq ft, furnished, servant room, 3 bathrooms, prime society"},
    {"name": "Essel Towers Ivory Court 2BHK", "address": "Sector 28, Gurgaon, Haryana", "rent": 70000, "bedrooms": 2, "notes": "1313 sq ft, 2BHK + study, fully renovated, modular kitchen, near metro"},
    {"name": "Maruti Vihar Sector 28 1RK", "address": "Sector 28, Gurgaon, Haryana", "rent": 20500, "bedrooms": 1, "notes": "400 sq ft, newly built, furnished, CCTV, near MG Road metro"},

    # ==========================================
    # Saraswati Vihar, Gurgaon
    # ==========================================
    {"name": "Saraswati Vihar Studio", "address": "Saraswati Vihar, Gurgaon, Haryana", "rent": 19000, "bedrooms": 1, "notes": "400 sq ft, furnished, modular kitchen, central AC, near MG Road metro"},
    {"name": "Housing Board Colony 1RK", "address": "Saraswati Vihar, Gurgaon, Haryana", "rent": 16000, "bedrooms": 1, "notes": "320 sq ft, furnished, RO water, lift & power backup, near metro"},
    {"name": "Saraswati Vihar Balcony Studio", "address": "Saraswati Vihar, Gurgaon, Haryana", "rent": 23000, "bedrooms": 1, "notes": "550 sq ft, northeast-corner residence, sun-drenched balcony, near MG Road"},

    # ==========================================
    # Chakkarpur, Gurgaon
    # ==========================================
    {"name": "Jan Pratinidhi Apartments 3BHK", "address": "Chakkarpur, Gurgaon, Haryana", "rent": 75000, "bedrooms": 3, "notes": "2200 sq ft, fully furnished, 4 bathrooms, servant room, near Phase 1 metro"},
    {"name": "Maruti Vihar Colony 1BHK", "address": "Chakkarpur, Gurgaon, Haryana", "rent": 15000, "bedrooms": 1, "notes": "450 sq ft, spacious and quiet, close to metro station"},

    # ==========================================
    # Sector 23 & 23A, Gurgaon
    # ==========================================
    {"name": "RWA East Pocket Builder Floor 1BHK", "address": "Sector 23, Gurgaon, Haryana", "rent": 26000, "bedrooms": 1, "notes": "1485 sq ft, newly built, furnished with AC, fridge, washing machine"},
    {"name": "Ansal Plaza Sector 23 1BHK", "address": "Sector 23, Gurgaon, Haryana", "rent": 30000, "bedrooms": 1, "notes": "630 sq ft, furnished, 2 bathrooms, 1 balcony, near Huda Market"},
    {"name": "Sector 23A Independent House 1BHK", "address": "Sector 23A, Gurgaon, Haryana", "rent": 31000, "bedrooms": 1, "notes": "500 sq ft, furnished builder floor, owner free, near Palam Triangle"},

    # ==========================================
    # Sector 22, Gurgaon
    # ==========================================
    {"name": "Ambience Creacions Luxury 2BHK", "address": "Sector 22, Gurgaon, Haryana", "rent": 67000, "bedrooms": 2, "notes": "1400 sq ft carpet, luxury high-rise, gym, pool, club house"},
    {"name": "Ambience Creacions Furnished 2BHK", "address": "Sector 22, Gurgaon, Haryana", "rent": 72000, "bedrooms": 2, "notes": "1380 sq ft carpet, fully furnished, luxury society"},

    # ==========================================
    # Sector 21, Gurgaon
    # ==========================================
    {"name": "Sector 21 Gurgaon House 1BHK", "address": "Sector 21, Gurgaon, Haryana", "rent": 27500, "bedrooms": 1, "notes": "263 sq ft, semi-furnished, 0-1 yr old, quiet residential pocket"},

    # ==========================================
    # Palam Vihar, Gurgaon
    # ==========================================
    {"name": "Ansals Palam Vihar 1BHK", "address": "Palam Vihar, Gurgaon, Haryana", "rent": 26500, "bedrooms": 1, "notes": "700 sq ft, semi-furnished top floor, modular kitchen, near Metro Hospital"},
    {"name": "Bestech Park View Residency 1BHK", "address": "Palam Vihar, Gurgaon, Haryana", "rent": 26000, "bedrooms": 1, "notes": "650 sq ft, 2 balconies, open parking, gated society with amenities"},

    # ==========================================
    # Sector 14, Gurgaon
    # ==========================================
    {"name": "Sector 14 RWA Builder Floor 1BHK", "address": "Sector 14, Gurgaon, Haryana", "rent": 26000, "bedrooms": 1, "notes": "700 sq ft, semi-furnished, modular kitchen, top floor, near Star Mall"},
    {"name": "Sector 14 Prime Studio", "address": "Sector 14, Gurgaon, Haryana", "rent": 26000, "bedrooms": 1, "notes": "1200 sq ft, fully furnished studio, central AC, near Millennium City Metro"},
    {"name": "Sector 14 Porsche Builder Floor 1BHK", "address": "Sector 14, Gurgaon, Haryana", "rent": 31000, "bedrooms": 1, "notes": "520 sq ft, fully furnished luxury builder floor, near Star Mall"},

    # ==========================================
    # Sector 15 Part 2, Gurgaon
    # ==========================================
    {"name": "Sector 15 Part 2 Builder Floor 1BHK", "address": "Sector 15 Part 2, Gurgaon, Haryana", "rent": 30000, "bedrooms": 1, "notes": "800 sq ft, furnished, gated community, near Google office"},

    # ==========================================
    # Sector 17, Gurgaon
    # ==========================================
    {"name": "IFFCO Nagar Sector 17 1BHK", "address": "Sector 17, Gurgaon, Haryana", "rent": 29000, "bedrooms": 1, "notes": "1431 sq ft, fully furnished, near IFFCO Chowk & MG Road metro"},
    {"name": "Sukhrali Sector 17 Studio", "address": "Sector 17, Gurgaon, Haryana", "rent": 29200, "bedrooms": 1, "notes": "900 sq ft, fully furnished new house, near IFFCO Chowk metro"},

    # ==========================================
    # DLF Phase 2, Gurgaon
    # ==========================================
    {"name": "Emaar MGF The Vilas 2BHK", "address": "DLF Phase 2, Gurgaon, Haryana", "rent": 95000, "bedrooms": 2, "notes": "1060 sq ft carpet, posh society, well lit"},
    {"name": "DLF Oakwood Estate 2BHK", "address": "DLF Phase 2, Gurgaon, Haryana", "rent": 65000, "bedrooms": 2, "notes": "1450 sq ft carpet, furnished, near MG Road metro"},
    {"name": "DLF Belvedere Park 2BHK", "address": "DLF Phase 2, Gurgaon, Haryana", "rent": 65000, "bedrooms": 2, "notes": "1402 sq ft carpet, furnished, near Belvedere Towers metro"},
    {"name": "DLF Phase 2 Luxury Studio", "address": "DLF Phase 2, Gurgaon, Haryana", "rent": 28000, "bedrooms": 1, "notes": "800 sq ft, ultra luxury studio, walking distance to Sikanderpur metro & Cyber City"},
    {"name": "DLF Phase 2 Gated Studio", "address": "DLF Phase 2, Gurgaon, Haryana", "rent": 25000, "bedrooms": 1, "notes": "240 sq ft, gated society next to Cyber City, 2 min to NH-8"},

    # ==========================================
    # DLF Phase 3, Gurgaon
    # ==========================================
    {"name": "DLF Phase 3 Luxury Studio", "address": "DLF Phase 3, Gurgaon, Haryana", "rent": 25000, "bedrooms": 1, "notes": "1140 sq ft, brand new luxury studio, near Cyber City & Dronacharya metro"},
    {"name": "DLF Phase 3 Boutique 1BHK", "address": "DLF Phase 3, Gurgaon, Haryana", "rent": 35000, "bedrooms": 1, "notes": "1400 sq ft, brand new luxury 1BHK, aesthetic furnishings, modular kitchen"},
    {"name": "DLF Phase 3 U-Block Studio", "address": "DLF Phase 3, Gurgaon, Haryana", "rent": 20000, "bedrooms": 1, "notes": "580 sq ft, furnished, near Rapid Metro, daily housekeeping & wifi included"},
    {"name": "DLF Phase 3 T-Block Studio", "address": "DLF Phase 3, Gurgaon, Haryana", "rent": 26000, "bedrooms": 1, "notes": "300 sq ft, luxury interiors, king size storage bed, Daikin inverter AC, RFID entry"},

    # ==========================================
    # Ambience Island, Gurgaon
    # ==========================================
    {"name": "Ambience Island Lagoon 3BHK", "address": "Ambience Island, Gurgaon, Haryana", "rent": 75000, "bedrooms": 3, "notes": "2100 sq ft, fully furnished luxury high-rise, servant room, near Ambience Mall"},

    # ==========================================
    # Old Faridabad
    # ==========================================
    {"name": "Old Faridabad 2BHK", "address": "Old Faridabad, Faridabad, Haryana", "rent": 16000, "bedrooms": 2, "notes": "Close to railway station, unfurnished"},
    {"name": "Old Faridabad PG", "address": "Old Faridabad, Faridabad, Haryana", "rent": 7000, "bedrooms": 1, "notes": "Budget PG, shared room"},
    {"name": "Old Faridabad Studio 1BHK", "address": "Old Faridabad, Faridabad, Haryana", "rent": 9500, "bedrooms": 1, "notes": "Compact, semi-furnished"},

    # ==========================================
    # NIT Faridabad
    # ==========================================
    {"name": "NIT Faridabad 2BHK", "address": "NIT Faridabad, Faridabad, Haryana", "rent": 13000, "bedrooms": 2, "notes": "Near NIT campus, student-friendly"},
    {"name": "NIT Faridabad PG Twin Sharing", "address": "NIT Faridabad, Faridabad, Haryana", "rent": 8000, "bedrooms": 1, "notes": "Popular with students"},
    {"name": "NIT Faridabad 1BHK Furnished", "address": "NIT Faridabad, Faridabad, Haryana", "rent": 12000, "bedrooms": 1, "notes": "Fully furnished, AC"},

    # ==========================================
    # Sector 15, Faridabad
    # ==========================================
    {"name": "Sector 15 Faridabad 2BHK", "address": "Sector 15 Market, Faridabad, Haryana", "rent": 17000, "bedrooms": 2, "notes": "Established residential area"},
    {"name": "Sector 15 Faridabad Studio", "address": "Sector 15 Market, Faridabad, Haryana", "rent": 9000, "bedrooms": 1, "notes": "Budget studio"},

    # ==========================================
    # Sector 21, Faridabad
    # ==========================================
    {"name": "Sector 21 Faridabad 3BHK", "address": "Sector 21C, Faridabad, Haryana", "rent": 22000, "bedrooms": 3, "notes": "Spacious, semi-furnished"},
    {"name": "Sector 21 Faridabad PG", "address": "Sector 21C, Faridabad, Haryana", "rent": 7500, "bedrooms": 1, "notes": "Shared room"},

    # ==========================================
    # Badkhal, Faridabad
    # ==========================================
    {"name": "Badkhal 2BHK", "address": "Badkhal, Faridabad, Haryana", "rent": 14500, "bedrooms": 2, "notes": "Near Badkhal lake, peaceful area"},
    {"name": "Badkhal Studio Flat", "address": "Badkhal, Faridabad, Haryana", "rent": 8500, "bedrooms": 1, "notes": "Compact, furnished"},

    # ==========================================
    # Ballabhgarh, Faridabad
    # ==========================================
    {"name": "Ballabhgarh 2BHK", "address": "Ballabhgarh, Faridabad, Haryana", "rent": 12000, "bedrooms": 2, "notes": "Budget friendly, unfurnished"},
    {"name": "Ballabhgarh PG Single", "address": "Ballabhgarh, Faridabad, Haryana", "rent": 6500, "bedrooms": 1, "notes": "Cheapest option, basic amenities"},
]


def seed():
    tracker = ApartmentTracker()

    for listing in RAW_LISTINGS:
        print(f"Looking up commute for: {listing['name']}...")
        commute = get_commute_minutes(ORIGIN_ADDRESS, listing["address"])

        apartment = Apartment(
            name=listing["name"],
            address=listing["address"],
            rent=listing["rent"],
            bedrooms=listing["bedrooms"],
            notes=listing.get("notes", ""),
            commute_minutes=commute,
        )
        tracker.add_apartment(apartment)

        if commute is not None:
            print(f"  -> commute: {commute} minutes")
        else:
            print("  -> could not get commute time (check API key/address)")

    save_to_file(tracker.apartments)
    print(f"\nSaved {len(tracker)} apartments to apartments.json")


if __name__ == "__main__":
    seed()