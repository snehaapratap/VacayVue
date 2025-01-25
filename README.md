# **VacayVue**

## **Overview**
The AI Travel Itinerary Planner is a user-friendly web app powered by **Google Places API** and built with **Streamlit**. It generates a personalized, day-by-day travel itinerary based on user preferences, such as destination, trip duration, and number of attractions per day.

## **Features**
- **Dynamic Travel Itineraries**: Generates a detailed plan with top attractions for any destination.
- **Google Places Integration**: Fetches highly-rated attractions, including their names, addresses, and ratings.
- **Customizable Inputs**: Users can define trip duration and the number of attractions per day.
- **Streamlit-Powered Interface**: An interactive and intuitive web application.

---

## **How to Run Locally**

### **1. Clone the Repository**
```bash
git clone https://github.com/snehaapratap/VacayVue.git
cd VacayVue
```

### **2. Set Up Environment**
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Replace `your_google_api_key_here` in `google_places.py` with your Google API key.

### **3. Run the Application**
```bash
streamlit run app.py
```

- The application will be available at `http://localhost:8501`.

---

## **File Structure**
```
travel_itinerary/
│
├── app.py                # Main Streamlit application
├── google_places.py      # Handles Google Places API integration
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

---

## **How It Works**
1. **User Input**:
   - Provide a destination.
   - Set the trip duration (1-7 days).
   - Select the number of attractions per day (1-5).

2. **Processing**:
   - Fetches attractions using **Google Places API**.
   - Creates a personalized itinerary, dividing attractions across days.

3. **Output**:
   - Displays a day-by-day itinerary with attraction details.

---

## **Example**
**Inputs**:
- Destination: Paris
- Trip Duration: 3 days
- Attractions Per Day: 2

**Output**:
```
Day 1:
- Eiffel Tower (Champ de Mars, 5 Avenue Anatole France, Paris) - Rated 4.7
- Louvre Museum (Rue de Rivoli, Paris) - Rated 4.6

Day 2:
- Notre-Dame Cathedral (6 Parvis Notre-Dame - Pl. Jean-Paul II, Paris) - Rated 4.7
- Sacré-Cœur Basilica (35 Rue du Chevalier de la Barre, Paris) - Rated 4.6

Day 3:
- Musée d'Orsay (1 Rue de la Légion d'Honneur, Paris) - Rated 4.6
- Arc de Triomphe (Place Charles de Gaulle, Paris) - Rated 4.7
```

---

## **Customization**
- Modify the **number of attractions per day** or refine the itinerary logic in `app.py`.
- Add more Google API features (e.g., hotel or restaurant recommendations).

---

## **Technologies Used**
- **Python**: Backend scripting and API integration.
- **Streamlit**: Frontend web application framework.
- **Google Places API**: Fetching travel-related data.

