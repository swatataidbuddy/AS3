import streamlit as st
import pandas as pd

# Sample Data (Replace with actual file processing logic)
data = {"Nvidia-23":{'Financial risk management strategies.': ['Stock Option Incentives:1.0', 'Fair Value Allocation in Acquisitions:0.43541885631845023', 'Foreign Currency Forward Contracts:0.36056490553218556', 'Board Committee Discretion:0.2845613793283679', 'Personal Tax Consultation:0.23157992105378455'], 'Financial transparency and accountability.': ['Proxy Statement Information:0.9999999999999998', 'Internal Control over Financial Reporting:0.3776726142961324'], 'Innovation and leadership in technology.': ['NVIDIA AI Cloud Services:0.9999999999999998', 'Executive Leadership at NVIDIA Corporation:0.44773023529918055'], 'Corporate Compliance and Financial Operations.': ['Termination of Continuous Service and Exercise of Awards:1.0', 'Grant Date and Vesting of RSUs, PSUs, and Market-based PSUs Awards:0.9930869060370133', 'Termination of Arm Acquisition by NVIDIA and SoftBank due to Regulatory Challenges:0.9896779985677504', 'Financial Expenses for Fiscal Years 2023, 2022, and 2021:0.9889947038975124', 'Tax-Related Items and Service Recipients:0.9889935349853358', 'Time Management/Updates:0.9875379610952603', 'Securities Exchange Act of 1934 and SEC Filings:0.9873789922005198', 'Performance Goals and Criteria for Compensation under Section 162(m) of the Code:0.983704174345578', 'Financial Statements for January 29, 2023:0.9832240916226129', 'Compliance with Section 409A of the Code:0.9810913111772372', 'Foreign Asset/Account Reporting Requirements and Exchange Controls.:0.9789323301348665', 'Stock Award Agreements and Plan Terms and Conditions:0.9785221081839022', 'Risks and Considerations of Investing in Common Stock:0.9708959836042594', 'Fiscal Year 2023 Revenue and Financial Performance:0.970048057821523', 'Stock Award Assumption and Termination in Corporate Transactions and Change in Control:0.9667402832149417', 'Impact of external factors on business financial results and operations:0.9660871836696122', 'Inventory Management and Provisions:0.959483960482598', 'Share Issuance and Sale:0.9564935255518122', 'Annual Report Form 10-K Notes:0.949575343739756', 'Stock Award Grants and Agreements:0.9444976260175819', 'Liquidity and Cash Management:0.9416851689078772', 'Plan Participation and Agreement Acceptance:0.9415448331711869', 'Restricted Stock Unit Awards and Agreements:0.9401270424860986', 'Revenue Recognition and Performance Obligations:0.9394397553753506', 'Company Affiliates and Employee Relationships:0.9384919729191852', 'NVIDIA Corporation and its Subsidiaries:0.9337628045862147', 'Long-term Operating Leases and Liabilities:0.9326009275703486', 'Dividend Program and Commercial Paper Program:0.9229136559619275', 'Acquisition Termination Cost in Fiscal Year 2023:0.922809059049083', 'Disclosure Controls and Procedures in Periodic Report:0.9189253678093303', 'Product Transitions and Demand for New Products:0.9162659268446761', 'Deferred Tax Assets and Liabilities:0.9157059601599394', 'Accounting for Gains and Losses on Investments:0.9103946815018888', 'Data Privacy and Processing Regulations:0.9100370474069908', 'Compliance with Exchange Control Laws and Regulations:0.9036786452917567', 'United States debt securities and financial markets:0.8967019042471309', 'Cloud Service Providers and Stock Plan Administration Services:0.8811339478656828', 'NVIDIA Computing Platforms and Software Solutions:0.8645373445561515', 'NVIDIA Headquarters and Operations in Santa Clara, California:0.8432446068985877']},
        "Nvidia-24":{'Financial risk management & compliance.': ['Foreign currency risk management with forward contracts:1.0', 'Securities Exchange Act Reporting Requirements:0.5249893815550648', 'Internal Control over Financial Reporting:0.49840430251893064', 'Incentive Compensation Policy:0.45772712513880065', 'Supply Chain Management:0.40561538370417005', 'Executive Leadership at NVIDIA Corporation:0.3597276624606056', 'Proxy Statement Information:0.3035972675781571'], 'Financial Performance and Compliance Overview': ['Financial Statements for January 28, 2024:0.9999999999999998', 'Financial Expenses for Fiscal Years 2024, 2023, and 2022:0.9907021458137475', 'Financial Condition and Results of Operations:0.9856583613307066', 'USG Licensing Requirements for Exports to China and Country Groups D1, D4, and D5:0.9807703185730557', 'Cryptocurrency Mining and Securities Lawsuits:0.9794077801439253', 'Stock-based compensation and equity incentive plans:0.9748897897041633', 'Risks of AI and Responsible Technology Use:0.9747119596119604', 'Share Repurchase Program and Board of Directors:0.9693788911788694', '"Risk Factors and Uncertainties in Annual Report on Form 10-K":0.966021415329841', 'Negative impact of export controls on AI technology and business:0.9656526754266322', 'Data Privacy and Security Laws and Regulations:0.9646903195465533', 'Revenue Recognition and Forecasting for Services and Software Support:0.9638995307176745', 'Impact of Geopolitical Conflict on License and Development Arrangements in Israel:0.9577885917824205', 'Disclosure Controls and Procedures:0.9550734259334017', 'Product Returns and Allowances:0.9544724281892503', 'Annual Report Form 10-K Notes:0.9535498449255628', 'Business Risks and Uncertainties:0.9523971060681795', 'Inventory Management and Provisions:0.9518008920062513', 'Liquidity and Cash Management:0.9488395798535997', 'Investment Income and Losses:0.9472473152629792', 'Product Transitions and Demand Impact:0.9387035646836082', 'Operating Lease Liabilities and Assets:0.9217782872077017', 'NVIDIA Corporation and Derivative Lawsuits:0.9209421096851432', 'Income Tax Expense and Benefits:0.9179041625342143', "NVIDIA's Presence in Santa Clara, California:0.9122434975806571", 'Revenue Recognition and Standalone Selling Price:0.9049041003130072', 'Compute & Networking Segment Revenue Breakdown:0.8992234898738185', 'Deferred Tax Assets and Valuation Allowance:0.8828545653966817', 'Non-Marketable Equity Securities and Investments in Non-Affiliated Entities:0.8818398264617592', 'NVIDIA AI Computing Platform and Software:0.8775031482995777', '2024 Fiscal Year Revenue Growth in Various Industries:0.8733848151366992', 'Stock repurchases and dividends for common stock:0.8188852841818424'], 'Business growth and financial planning.': ['Data Center Product Launch Strategy:0.9999999999999999', 'Commercial Paper Program:0.3881922275636319']}
        }

# Streamlit App Title
st.title("📊 Interactive Dashboard")

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