import streamlit as st
import pandas as pd

# Sample Data (Replace with actual file processing logic)
data = {
    "pfizer-2021": {
        "Strategic Partnerships in Pharmaceutical Leadership": ['Pharmaceutical Collaborations', 'Executive Leadership Roles'],
        "Financial Risk Management and Reporting": ['Common Stock Transactions', 'Foreign Exchange Risk Management', 'Internal Control Over Financial Reporting', 'Additional Information Notes'],
        "Pharma patent litigation and payments":['Patent infringement actions against generic companies', 'District Court Litigation', 'Deferred Payment Deadline for Pfizer Inc.'],
        "Financial operations and regulations overview.":['Restructuring and Acquisition-Related Costs', 'Financial Results of Upjohn Business and Mylan-Japan Collaboration as Discontinued Operations', 'Business spin-off and combination of Upjohn and Mylan to form Viatris', '409A and Section 162(m) of the Internal Revenue Code', 'Sarbanes-Oxley Act of 2002 and Section 906 Certification', 'Euroclear and Clearstream Accounts Operations', 'Expense Allocation and Reporting in 2019', 'Impact of COVID-19 Pandemic on Business Operations and Financial Condition', 'Share-based payment expenses and other financial items', 'Financial Information for December 31, 2020', 'Amendment to Separation and Distribution Agreement', 'Financial Performance of Pfizer Inc. in 2020', 'Government Regulation and Price Constraints in Form 10-K', 'Proposed Regulations for Section 162(m) of the Code', 'Reclassification adjustments and net gains/losses in financial statements', 'Risks and Challenges in Clinical Regulatory Approval for COVID-19 Vaccines and Treatments', '"Item 1A and Additional Information in a Business Report"', 'Financing Activities and Changes in Short-Term and Long-Term Borrowings', 'Redemption of Notes', 'Incorporation of Pfizer Supplemental Savings Plan in Annual and Quarterly Reports', 'Product Revenues and Alliances', 'Supplemental Indentures for Bank of New York Mellon and JPMorgan Chase Bank', 'Intellectual Property Rights and Litigation', 'Uncertain Tax Positions and Assets', 'Valuation of Projected Cash Flows', 'Pension Plans in the U.S. and Worldwide', 'Grandfathered Compensation and Awards', 'Fair Value Measurement and Reporting', 'Performance Incentive Awards and Termination', 'Pharmaceutical Competition and Government Regulations', 'Legal Business Contingencies and Result Estimates', 'Income deductions and adjustments', 'Disclosure Controls and Procedures Evaluation', 'Equity Investments and Securities Valuation', 'Deferred Compensation Plan Benefits and Eligibility', 'SEC Filings for Various Forms and Dates', 'SEC Request for Omitted Schedules and Exhibits', 'Indemnification of Liabilities in Pfizer Transactions', 'Noncurrent Assets and Impairment Testing', 'Impact of new guidance on consolidated financial statements', 'Healthcare Joint Venture Formation and Impact on Company Finances']

    },
    "pfize-2018": {
        "Financial operations and industry regulations":['Cash Acquisitions in Pharmaceutical Industry', 'Development Funding for Clinical Research', 'Emerging Markets in Europe', 'Changes in Viagra Revenue Reporting', 'Income Taxes on Continuing Operations', 'Consolidated Financial Statements Notes', 'Internal Control Over Financial Reporting']
,
        "Employee Retirement and Death Benefits": ['Retirement Plans', 'Pension Plans', 'Retirement benefits for senior executives', 'Retirement Benefits for Pfizer Employees', 'Death Benefits for Married Participants'],
        "Financial contract implementation options": ['Share Repurchase Agreements', 'Supplemental Indentures between banks', 'Lump Sum Payment Options'],
        "Financial Reporting and Compliance Requirements":['Certification and Payment Requirements under Sarbanes-Oxley Act of 2002', 'Comparison of Worldwide Revenues in 2017 and 2016 for Xeljanz, Celebrex, Lipitor, Norvasc, and Sutent', 'Cost-Reduction/Productivity Initiatives', 'Collaboration between Merck KGaA and Bavencio for cancer treatment', 'Acquisition Costs for Hospira and Other Companies', "Pfizer's Business Segments and Leadership Changes", 'Income/DeductionsNet Adjustments', 'Sale of Hospira Infusion Systems Net Assets to ICU Medical, Inc.', 'Intellectual Property Rights and Collaboration/Licensing Rights', 'Complex series of judgments and uncertainties in future events and financial reporting.', 'Financial Results and Operations of Acquired Businesses', 'Board of Directors and Committee Decision-Making', 'Vesting and Settlement of Retirement Benefits', 'Note-taking and referencing', 'Financial Report for Fiscal Year Ended December 31, 2017', 'NonGrandfathered Benefit Payment Options', 'Material Impact of Standard Adoption on Compensation Expense and Financial Statements', 'Negative impact of foreign exchange on international revenues in 2017', 'Additional Information and Notes', 'Accounting Policies and Standards', 'Financial performance and expenses', 'Retirement Benefits and Plans', '2017 Financial Report Topics', 'Business Expenses and Sales Costs', 'Financial Instruments and Long-Term Debt', 'Incorporated References in Annual Reports and Forms', 'Executive Leadership Roles and Transitions', 'Identifiable Intangible Assets and Goodwill', 'Equity Method Investments and Collaborative Development', "Strategic Alternatives for Pfizer's Consumer Healthcare Business", 'Fair Value Measurement and Impairment Testing', 'Financial Condition, Liquidity and Capital Resources', 'Risks Associated with Estimates and Assumptions in Financial Statements', 'Tax Reform and Deferred Tax Liabilities', 'Stock Repurchase and Stock Options', 'Assessing impact of new guidance on consolidated financial statements', 'Competition in the Generic and Biosimilar Market for Legacy Products', 'Multi-District Litigation in the U.S. District Court for the District of New Jersey']

    }   
}

# Streamlit App Title
st.title("📊 Interactive Dashboard")

# File Selection Dropdown
selected_file = st.selectbox("Select a File", list(data.keys()))

# Display High-Level Topics based on selected file
if selected_file:
    topics = list(data[selected_file].keys())
    selected_topic = st.selectbox("Select a High-Level Topic", topics)

    # Display all Sub-Level Topics as a menu
    if selected_topic:
        sub_topics = data[selected_file][selected_topic]

        st.subheader(f"Sub-Level Topics for {selected_topic}:")
        
        # Display each sub-topic as a clickable button
        for sub in sub_topics:
            if st.button(sub):
                st.success(f"✅ You selected: {sub}")