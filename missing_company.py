import streamlit as st
import json
import pandas as pd

# Load JSON data
json_file_path = "data.json"  # Update this path
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

# Streamlit app
st.title("Company Quarters Data")

# Select a company
company_list = list(data.keys())
selected_company = st.selectbox("Select a Company", company_list)

# Display table for selected company
if selected_company:
    st.subheader(f"Missing Quarters for {selected_company}")
    
    # Prepare data for display
    company_data = data[selected_company]
    table_data = [(year, ", ".join(quarters)) for year, quarters in company_data.items()]
    df = pd.DataFrame(table_data, columns=["Year", "Quarters"])
    
    # Display as dataframe
    st.table(df)
