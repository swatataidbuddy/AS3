import streamlit as st
import pandas as pd

# Hardcoded data dictionary based on the provided data
data = {
    "SCHW - Charles Schwab": {
        "2015": ["1", "2", "3", "4"],
        "2016": ["2", "3", "4"],
        "2017": ["1", "2", "3", "4"],
        "2018": ["1", "2", "4"],
        "2019": ["1", "2", "3"],
        "2020": ["1", "2", "4"],
        "2021": ["1", "2", "3", "4"],
    },
    "CI  - Cigna Group": {
        "2015": ["2", "3", "4"],
        "2016": ["1"],
    },
    "TMUS T-Mobile US": {
        "2024": ["4"],
    },
    "TGT - Target": {
        "2023": ["2"],
        "2024": ["4"],
    },
    "HD Home Depot": {
        "2024": ["4"],
    },
    "WMT Walmart": {
        "2019": ["2", "3"],
        "2020": ["1", "2", "3"],
    },
    "EOG EOG resources": {
        "2024": ["4"],
    },
    "LIN Linde": {
        "2015": ["1", "2", "3", "4"],
        "2016": ["1", "2", "3", "4"],
        "2017": ["1", "2", "3", "4"],
        "2018": ["1", "2", "3", "4"],
    },
    "LOW Lowes Companies": {
        "2021": ["3"],
        "2023": ["2"],
        "2024": ["4"],
    },
    "BRK.B Berkshire Hathaway": {
        "2015": ["1", "2", "3", "4"],
        "2016": ["1", "2", "3", "4"],
        "2017": ["1", "2", "3", "4"],
        "2018": ["1", "2", "3", "4"],
        "2019": ["1", "2", "3", "4"],
        "2020": ["1", "2", "3", "4"],
        "2021": ["1", "2", "3", "4"],
        "2022": ["1", "2", "3", "4"],
        "2023": ["1", "2", "3", "4"],
        "2024": ["1", "2", "3", "4"],
    },
}

# Streamlit app layout
st.title("Empty Quarters by Company")

# Sidebar: select a company from the keys of our data dictionary
company = st.sidebar.selectbox("Select Company", list(data.keys()))

# Retrieve data for the selected company
company_data = data.get(company, {})

# Prepare a list of rows for our table
rows = []
for year, quarters in company_data.items():
    # Join quarter numbers with commas
    quarters_str = ", ".join(quarters)
    rows.append({"Year": year, "Empty Quarters": quarters_str})

# Create a DataFrame, sort by Year (if desired)
df = pd.DataFrame(rows).sort_values(by="Year")

# Display the company name and table
st.write(f"### Empty Quarters for **{company}**")
st.table(df)
