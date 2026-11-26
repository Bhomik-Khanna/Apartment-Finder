#  Apartment Finder

A Smart Apartment Discovery and Comparison Platform

Apartment Finder is a Streamlit-based application designed to simplify apartment discovery by helping users evaluate rental listings based on budget, location, and commute preferences.

The platform combines personalized apartment ranking, real-time commute calculations, side-by-side comparisons, and an AI-powered assistant to make rental decisions more informed and convenient.

---

 Key Features

 1. Smart Apartment Discovery
- Browse apartment listings across Gurgaon and Faridabad.
- Filter apartments based on maximum rent, bedrooms, and commute time.
- Automatically rank apartments based on user-defined preferences.
- View match scores to identify suitable rental options.

 2. Personalized Ranking System
- Calculate apartment match scores using rent and commute preferences.
- Adjust the importance of rent versus commute time.
- Dynamically reorder listings as preferences and filters change.
- Visualize rental costs and commute comparisons.

Scoring formula:

`Match Score = (Rent Score × Rent Weight) + (Commute Score × Commute Weight)`

 3. Apartment Comparison
- Compare multiple apartments side by side.
- Evaluate differences in rental prices, bedrooms, commute times, and other listing details.
- Make more informed decisions using structured comparisons.

 4. Near Me – Live Commute Analysis
- Enter a custom starting location or choose from predefined locations.
- Calculate driving commute times to available apartments.
- Retrieve geographical coordinates through OpenRouteService geocoding.
- Rank apartments based on commute convenience and affordability.
- Cache commute results to avoid unnecessary repeated API requests.

 5. AI-Powered Assistant
- Integrated Google Gemini API for conversational assistance.
- Ask natural-language questions about apartment listings.
- Receive apartment recommendations based on actual database records.
- Get explanations of match scores and application functionality.
- Add apartment listings through conversational interactions.
- Collect user feedback and ratings.

 6. Analytics Dashboard
- Explore user feedback and rating trends.
- Visualize application data through charts.
- Monitor feedback to understand user experience.

 7. Apartment Management
- Add and manage apartment listings.
- Store apartment information using SQLite.
- Prevent duplicate apartment entries.
- Automatically calculate commute information when adding listings.

8. Additional Functionality
- Customizable application themes.
- User preferences and filtering settings.
- Password-protected administration functionality.
- Persistent storage for apartment listings and feedback.

---

Tech Stack

| Category | Technologies |
|---|---|
| Frontend / UI | Streamlit |
| Programming Language | Python |
| Database | SQLite |
| Data Visualization | Matplotlib |
| AI Integration | Google Gemini API |
| Geolocation & Routing | OpenRouteService API |
| HTTP Requests | Requests |
| Environment Configuration | Python Dotenv |
| Version Control | Git & GitHub |

---

 Project Structure

```text
Apartment-Finder/
│
├── .streamlit/
│   └── config.toml
│
├── pages/
│   ├── 1_Compare.py
│   ├── 2_Manage.py
│   ├── 3_About.py
│   ├── 4_Near_Me.py
│   ├── 5_AI_Assistant.py
│   ├── 6_Analytics.py
│   ├── 7_Admin.py
│   └── 8_Settings.py
│
├── Image.png
├── Landing.py
├── app.py
├── apartment.py
├── storage.py
├── tracker.py
├── theme.py
├── distance_api.py
├── seed_data.py
├── debug.py
│
├── apartments.db
├── apartment_requests.json
├── apartments.json.migrated
│
├── .gitignore
└── README.md
```

---

 Installation & Setup

### Prerequisites

- Python 3.10 or later
- Git
- Google Gemini API key
- OpenRouteService API key

### 1. Clone the repository

```bash
git clone https://github.com/Bhomik-Khanna/Apartment-Finder.git
```

Navigate into the project directory:

```bash
cd Apartment-Finder
```

2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows:
```powershell
venv\Scripts\activate
```

macOS / Linux:**
```bash
source venv/bin/activate
```

3. Install dependencies

```bash
pip install streamlit matplotlib requests python-dotenv urllib3
```

 4. Configure environment variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
ORS_API_KEY=your_openrouteservice_api_key
```




 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

---

 Database & Data Storage

The application uses SQLite for persistent data storage.

The database manages:

- Apartment listings
- User feedback and ratings
- Apartment requests submitted through the AI assistant

The database schema is initialized automatically when the storage module creates a connection.

The project also includes a JSON-to-SQLite migration mechanism for importing existing apartment records.

---

 Supported Locations

The current apartment dataset focuses on the National Capital Region (NCR).

**Gurgaon:**
- Sector 44
- Sector 45
- Sector 46
- Sector 47
- Sector 48

**Faridabad:**
- Old Faridabad
- NIT Faridabad
- Sector 15
- Sector 21
- Badkhal
- Ballabhgarh

---

Security Notes

- API credentials are configured through environment variables.
- Sensitive configuration files are excluded using `.gitignore`.
- Administrative functionality is protected through password authentication.

---

 Future Improvements

- Integration with additional rental listing sources.
- Advanced apartment recommendation algorithms.
- Interactive map-based apartment discovery.
- Automated apartment listing updates.
- Expanded analytics and reporting.
- Improved AI-driven rental recommendations.

---



Bhomik Khanna



