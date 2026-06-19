import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

providers = pd.read_csv("providers_data.csv")
receivers = pd.read_csv("receivers_data.csv")
food = pd.read_csv("food_listings_data.csv")
claims = pd.read_csv("claims_data.csv")

st.sidebar.header("Filters")
provider_filter = st.sidebar.selectbox(
    "Provider Type",
    ["All"] + list(providers["Type"].unique())
)


st.title("🍽️ Local Food Wastage Management Dashboard")
st.write("Selected Provider:", provider_filter)
filtered_providers = providers

if provider_filter != "All":
    filtered_providers = providers[
        providers["Type"] == provider_filter
    ]
food_filter = st.sidebar.selectbox(
    "Food Type",
    ["All"] + list(food["Food_Type"].unique())
)
filtered_food = food

if food_filter != "All":
    filtered_food = food[
        food["Food_Type"] == food_filter
    ]

meal_filter = st.sidebar.selectbox(
    "Meal Type",
    ["All"] + list(food["Meal_Type"].unique())
)
if meal_filter != "All":
    filtered_food = filtered_food[
        filtered_food["Meal_Type"] == meal_filter
    ]
    
status_filter = st.sidebar.selectbox(
    "Claim Status",
    ["All"] + list(claims["Status"].unique())
)

filtered_claims = claims

if status_filter != "All":
    filtered_claims = claims[
        claims["Status"] == status_filter
    ]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Providers", len(filtered_providers))

with col2:
    st.metric("Receivers", len(receivers))

with col3:
    st.metric("Food Listings", len(filtered_food))

with col4:
    st.metric("Claims", len(filtered_claims))

   
st.subheader("Provider Type Distribution")

fig, ax = plt.subplots()

filtered_providers["Type"].value_counts().plot(
 kind="bar",
 ax=ax
    )

st.pyplot(fig)
st.markdown("---")


st.subheader("Receiver Type Distribution")

fig, ax = plt.subplots()

receivers["Type"].value_counts().plot(
        kind="bar",
        ax=ax
    )

st.pyplot(fig)
st.markdown("---")

st.subheader("Food Type Distribution")

fig, ax = plt.subplots()

filtered_food["Food_Type"].value_counts().plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)
st.markdown("---")

st.subheader("Meal Type Distribution")

fig, ax = plt.subplots()

filtered_food["Meal_Type"].value_counts().plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)
st.markdown("---")

st.subheader("Claim Status Distribution")

fig, ax = plt.subplots()

filtered_claims["Status"].value_counts().plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)
st.markdown("---")

st.subheader("Top 10 Cities by Food Listings")

top_cities = food["Location"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10,5))

top_cities.plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)
st.markdown("---")