import streamlit as st
from google_places import get_top_attractions

st.set_page_config(page_title="Travel Itinerary Planner", layout="wide")

st.title("AI Travel Itinerary Planner")
st.sidebar.header("User Input")

# User Inputs
destination = st.sidebar.text_input("Destination")
duration = st.sidebar.slider("Trip Duration (days)", min_value=1, max_value=7, value=3)
num_attractions = st.sidebar.slider("Attractions Per Day", min_value=1, max_value=5, value=3)

# Generate Itinerary Button
if st.sidebar.button("Generate Itinerary"):
    if not destination:
        st.error("Please enter a destination.")
    else:
        try:
            st.subheader(f"Top Attractions in {destination}")
            attractions = get_top_attractions(destination, num_results=duration * num_attractions)
            
            # Display Itinerary
            for day in range(duration):
                st.markdown(f"### Day {day + 1}")
                for idx in range(num_attractions):
                    attraction_idx = day * num_attractions + idx
                    if attraction_idx < len(attractions):
                        attr = attractions[attraction_idx]
                        st.write(f"- **{attr['name']}** ({attr['address']}) - Rated {attr['rating']}")
        except Exception as e:
            st.error(f"Error generating itinerary: {e}")
