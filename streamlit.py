import streamlit as st
import pandas as pd

# Sample Data (Replace with actual file processing logic)
data = {"Nvidia-23": {
  "Financial Reporting & Performance": [
    "Annual Report Form 10-K Notes",
    "Fiscal Year 2023 Revenue and Financial Performance",
    "Financial Statements for January 29, 2023",
    "Financial Expenses for Fiscal Years 2023, 2022, and 2021",
    "Disclosure Controls and Procedures in Periodic Report"
  ],
  "Taxation & Regulatory Compliance": [
    "Foreign Asset/Account Reporting Requirements and Exchange Controls",
    "Deferred Tax Assets and Liabilities",
    "Personal Tax Consultation",
    "Data Privacy and Processing Regulations",
    "Compliance with Section 409A of the Code",
    "Tax-Related Items and Service Recipients",
    "Compliance with Exchange Control Laws and Regulations"
  ],
  "Corporate Governance & Leadership": [
    "Internal Control over Financial Reporting",
    "Proxy Statement Information",
    "Securities Exchange Act of 1934 and SEC Filings",
    "Board Committee Discretion",
    "Executive Leadership at NVIDIA Corporation"
  ],
  "Investments & Market Risks": [
    "Risks and Considerations of Investing in Common Stock",
    "Liquidity and Cash Management",
    "Foreign Currency Forward Contracts",
    "Accounting for Gains and Losses on Investments",
    "United States Debt Securities and Financial Markets",
    "Dividend Program and Commercial Paper Program"
  ],
  "Stock Awards, Compensation & Incentives": [
    "Stock Award Agreements and Plan Terms and Conditions",
    "Stock Award Assumption and Termination in Corporate Transactions and Change in Control",
    "Termination of Continuous Service and Exercise of Awards",
    "Performance Goals and Criteria for Compensation under Section 162(m) of the Code",
    "Stock Award Grants and Agreements",
    "Restricted Stock Unit Awards and Agreements",
    "Stock Option Incentives",
    "Plan Participation and Agreement Acceptance",
    "Grant Date and Vesting of RSUs, PSUs, and Market-based PSUs Awards",
    "Share Issuance and Sale",
    "Company Affiliates and Employee Relationships"
  ],
  "Mergers, Acquisitions & Corporate Transactions": [
    "Fair Value Allocation in Acquisitions",
    "Acquisition Termination Cost in Fiscal Year 2023",
    "Termination of Arm Acquisition by NVIDIA and SoftBank due to Regulatory Challenges"
  ],
  "Product & Market Strategy": [
    "NVIDIA Computing Platforms and Software Solutions",
    "NVIDIA AI Cloud Services",
    "Product Transitions and Demand for New Products"
  ],
  "Operational & External Business Impact": [
    "Inventory Management and Provisions",
    "Long-term Operating Leases and Liabilities",
    "Time Management/Updates",
    "Impact of External Factors on Business Financial Results and Operations",
    "Revenue Recognition and Performance Obligations"
  ],
  "Corporate Presence & Brand": [
    "NVIDIA Corporation and its Subsidiaries",
    "NVIDIA Headquarters and Operations in Santa Clara, California"
  ]
},
        "Nvidia-24":{
  "Financial Reporting & Performance": [
    "2024 Fiscal Year Revenue Growth in Various Industries",
    "Annual Report Form 10-K Notes",
    "Financial Statements for January 28, 2024",
    "Financial Condition and Results of Operations",
    "Financial Expenses for Fiscal Years 2024, 2023, and 2022",
    "Disclosure Controls and Procedures"
  ],
  "Taxation & Regulatory Compliance": [
    "Income Tax Expense and Benefits",
    "USG Licensing Requirements for Exports to China and Country Groups D1, D4, and D5",
    "Data Privacy and Security Laws and Regulations",
    "Deferred Tax Assets and Valuation Allowance",
    "Business Risks and Uncertainties",
    "Risk Factors and Uncertainties in Annual Report on Form 10-K"
  ],
  "Corporate Governance & Leadership": [
    "Internal Control over Financial Reporting",
    "Securities Exchange Act Reporting Requirements",
    "Incentive Compensation Policy",
    "Proxy Statement Information",
    "Executive Leadership at NVIDIA Corporation",
    "Share Repurchase Program and Board of Directors"
  ],
  "Investments & Market Risks": [
    "Non-Marketable Equity Securities and Investments in Non-Affiliated Entities",
    "Stock repurchases and dividends for common stock",
    "Liquidity and Cash Management",
    "Foreign currency risk management with forward contracts",
    "Investment Income and Losses",
    "Commercial Paper Program"
  ],
  "Revenue & Sales Strategy": [
    "Revenue Recognition and Forecasting for Services and Software Support",
    "Compute & Networking Segment Revenue Breakdown",
    "Data Center Product Launch Strategy",
    "Revenue Recognition and Standalone Selling Price"
  ],
  "Supply Chain & Inventory Management": [
    "Product Transitions and Demand Impact",
    "Inventory Management and Provisions",
    "Operating Lease Liabilities and Assets",
    "Supply Chain Management",
    "Product Returns and Allowances"
  ],
  "AI, Technology & Business Risks": [
    "NVIDIA AI Computing Platform and Software",
    "Impact of Geopolitical Conflict on License and Development Arrangements in Israel",
    "Negative impact of export controls on AI technology and business",
    "Risks of AI and Responsible Technology Use"
  ],
  "Legal & Corporate Litigation": [
    "NVIDIA Corporation and Derivative Lawsuits",
    "Cryptocurrency Mining and Securities Lawsuits"
  ],
  "Corporate Presence & Brand": [
    "NVIDIA's Presence in Santa Clara, California"
  ]
}
}

# Streamlit App Title
st.title("Topic SuperGrouping using OpenAI")

# File Selection Dropdown
selected_file = st.selectbox("Select a File", list(data.keys()))

# Display High-Level Topics based on selected file
if selected_file:
    topics = list(data[selected_file].keys())
    selected_topic = st.selectbox("Select a High-Level Topic", topics)

    # Display all Sub-Level Topics as a Table
    if selected_topic:
        sub_topics = data[selected_file][selected_topic]

        # Split data into Label & Similarity Score
        table_data = []
        for item in sub_topics:
            label, score = item.split(":")
            table_data.append({"Topic Label": label.strip(), "Similarity Score": float(score.strip())})

        # Convert to DataFrame
        df = pd.DataFrame(table_data)

        # Display the table (without showing the index)
        st.subheader(f"Sub-Level Topics for {selected_topic}")
        st.dataframe(df.set_index("Topic Label"))  # This hides the default index and makes "Label" the index