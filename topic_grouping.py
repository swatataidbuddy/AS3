import streamlit as st
import pandas as pd

# Sample Data (Replace with actual file processing logic)
data = {"Nvidia-23": 
  {"Financial Reporting & Performance": [
    {
      "topic_label": "Annual Report Form 10-K Notes",
      "topic_summary": "Provides detailed information about the company's financial statements in Part IV, Item 15, including investments in non-affiliated entities, equity incentive plans, and other financial discussions necessary for a comprehensive understanding of financial health."
    },
    {
      "topic_label": "Fiscal Year 2023 Revenue and Financial Performance",
      "topic_summary": "Covers revenue fluctuations by segment in FY2023, such as Gaming, Automotive, and Data Center, plus income tax benefits, share repurchases, and professional visualization revenue changes."
    },
    {
      "topic_label": "Financial Statements for January 29, 2023",
      "topic_summary": "Summarizes the consolidated financial statements, foreign currency forward contracts, and fair value of RSUs/PSUs vested over three years. Reflects the company’s financial position, operations, and cash flows in accordance with US GAAP."
    },
    {
      "topic_label": "Internal Control over Financial Reporting",
      "topic_summary": "Explains management’s responsibility for effective internal controls, testing procedures for fraud risks, and quarterly assessments. No material changes were identified as of January 29, 2023."
    },
    {
      "topic_label": "Financial Expenses for Fiscal Years 2023, 2022, and 2021",
      "topic_summary": "Shows trends in intrinsic value of options exercised, inventory provisions, depreciation, amortization, and operating lease expenses. Highlights the overall increase in company expenses over multiple years."
    },
    {
      "topic_label": "Long-term Operating Leases and Liabilities",
      "topic_summary": "Covers how operating lease assets and liabilities are recognized, discounted using the incremental borrowing rate, and disclosed in the consolidated balance sheet. Includes details about remaining lease terms and related obligations."
    }
  ],
  "Investments & Corporate Finance": [
    {
      "topic_label": "Liquidity and Cash Management",
      "topic_summary": "Focuses on the company’s cash, equivalents, and marketable securities, including their availability for use in the U.S. without additional taxes. Plans for capital expenditures in FY2024 are also discussed."
    },
    {
      "topic_label": "Foreign Currency Forward Contracts",
      "topic_summary": "Describes the company’s strategy for minimizing foreign exchange rate fluctuations on operating expenses and monetary assets. Includes notional contract values and maturity dates."
    },
    {
      "topic_label": "Accounting for Gains and Losses on Investments",
      "topic_summary": "Explains how debt and marketable securities are measured at fair value, unrealized gains/losses recognized in accumulated other comprehensive income, and realized gains/losses recorded in other income (expense)."
    },
    {
      "topic_label": "United States debt securities and financial markets",
      "topic_summary": "Highlights the company’s investments in various U.S. and foreign government securities, its manufacturing outside the United States, and the global taxation environment impacting NVIDIA’s business."
    },
    {
      "topic_label": "Dividend Program and Commercial Paper Program",
      "topic_summary": "Covers the company’s share repurchase history, quarterly cash dividends, and the commercial paper program used to support general corporate purposes."
    }
  ],
  "Business & Investment Risks": [
    {
      "topic_label": "Risks and Considerations of Investing in Common Stock",
      "topic_summary": "Emphasizes insider trading restrictions, market abuse laws, and potential financial risks for shareholders in various jurisdictions. Encourages awareness of local regulations and further research."
    },
    {
      "topic_label": "Impact of external factors on business financial results and operations",
      "topic_summary": "Discusses threats such as the COVID-19 pandemic, climate change, cryptocurrency, consumer laws, and political instability, all of which can negatively affect the company’s financial condition and reputation."
    }
  ],
  "Mergers, Acquisitions & Corporate Transactions": [
    {
      "topic_label": "Fair Value Allocation in Acquisitions",
      "topic_summary": "Details how intangible assets, IPR&D, and goodwill are valued and recognized. Any excess purchase price is allocated to goodwill, with developed technology valued using the Multi-Period Excess Earnings Method."
    },
    {
      "topic_label": "Acquisition Termination Cost in Fiscal Year 2023",
      "topic_summary": "Discusses the $1.35 billion charge related to the terminated Arm transaction, including higher operating expenses, restructuring costs, and impacts on operating activities."
    },
    {
      "topic_label": "Termination of Arm Acquisition by NVIDIA and SoftBank due to Regulatory Challenges",
      "topic_summary": "Explains the regulatory hurdles that prevented the completion of the Arm acquisition, resulting in significant costs and highlighting the importance of government approvals in M&A."
    }
  ],
  "Corporate Presence & Leadership": [
    {
      "topic_label": "NVIDIA Corporation and its Subsidiaries",
      "topic_summary": "Outlines the global network of NVIDIA entities, including subsidiaries and international holdings. Mentions continuity of previous equity incentive plans and references to NVIDIA Corporation worldwide."
    },
    {
      "topic_label": "Executive Leadership at NVIDIA Corporation",
      "topic_summary": "Profiles key executives—Debora Shoquist, Colette Kress, Ajay Puri, Timothy Teter, and Jen-Hsun Huang—covering their roles, prior experience, and contributions to the company."
    },
    {
      "topic_label": "NVIDIA Headquarters and Operations in Santa Clara, California",
      "topic_summary": "Describes the company’s base of operations in Santa Clara and potential challenges like power shutoffs and extreme weather. Highlights NVIDIA’s incorporation history and reliance on California jurisdiction."
    }
  ],
  "Taxation & Regulatory Compliance": [
    {
      "topic_label": "Foreign Asset/Account Reporting Requirements and Exchange Controls.",
      "topic_summary": "Addresses the need for compliance with local tax, exchange control, and reporting obligations in various countries. Non-compliance can lead to penalties and asset impairment charges."
    },
    {
      "topic_label": "Deferred Tax Assets and Liabilities",
      "topic_summary": "Explains recognition of deferred tax assets, valuation allowances, and factors reducing the company’s effective tax rate, including FDII deductions and research tax credits."
    },
    {
      "topic_label": "Personal Tax Consultation",
      "topic_summary": "Advises participants to consult legal and tax professionals regarding local reporting requirements. Emphasizes complexity for residents in countries like Italy and Spain."
    },
    {
      "topic_label": "Data Privacy and Processing Regulations",
      "topic_summary": "Discusses strict data localization laws, cross-border transfer restrictions, and the high costs of ensuring compliance with evolving privacy regulations in various jurisdictions."
    },
    {
      "topic_label": "Compliance with Exchange Control Laws and Regulations",
      "topic_summary": "Lists multiple countries where participants must follow exchange control laws, cautioning about penalties for non-compliance and emphasizing the need for legal guidance."
    }
  ],
  "Stock Awards, Compensation & Incentives": [
    {
      "topic_label": "Stock Award Agreements and Plan Terms and Conditions",
      "topic_summary": "Explains how restricted stock awards, SARs, and stock units follow the Plan’s terms. Agreements vary by participant and incorporate Plan guidelines."
    },
    {
      "topic_label": "Stock Award Assumption and Termination in Corporate Transactions and Change in Control",
      "topic_summary": "Describes conditions under which vesting may accelerate in a Change in Control if awards aren’t assumed by the surviving corporation."
    },
    {
      "topic_label": "Termination of Continuous Service and Exercise of Awards",
      "topic_summary": "Details vesting rules for stock options or SARs upon termination (death, disability, cause, etc.) and forfeiture conditions for restricted stock."
    },
    {
      "topic_label": "Performance Goals and Criteria for Compensation under Section 162(m) of the Code",
      "topic_summary": "Outlines how Performance Goals are set, measured, and certified. The Board or Committee adjusts results for stock-based compensation and determines goal attainment before payment."
    },
    {
      "topic_label": "Stock Award Grants and Agreements",
      "topic_summary": "Covers grants of performance stock awards, restricted stock units, and other stock awards. Addresses vesting acceleration, substitution in corporate transactions, and plan limits."
    },
    {
      "topic_label": "Restricted Stock Unit Awards and Agreements",
      "topic_summary": "Defines RSU award terms, referencing Plan documents and requiring compliance with grant notices, local law, transfer limitations, and tax responsibilities."
    },
    {
      "topic_label": "Stock Option Incentives",
      "topic_summary": "Specifies option exercise prices, designations (Incentive vs. Nonstatutory), transferability under certain circumstances, and termination conditions upon death or failure to exercise."
    },
    {
      "topic_label": "Plan Participation and Agreement Acceptance",
      "topic_summary": "Highlights participants’ acknowledgment of Plan and Agreement terms, voluntary nature of awards, and immediate cessation upon end of service (except death)."
    },
    {
      "topic_label": "Compliance with Section 409A of the Code",
      "topic_summary": "Establishes requirements for deferred compensation, including six-month delays for specified employees and compliance with the Code in plan documents and corporate transactions."
    },
    {
      "topic_label": "Tax-Related Items and Service Recipients",
      "topic_summary": "Holds participants liable for all tax obligations from their plan awards, allowing the company to withhold or require direct payment of taxes."
    },
    {
      "topic_label": "Time Management/Updates",
      "topic_summary": "Notes that vesting/exercise can be accelerated for death/disability or corporate transactions, plan changes may occur, and inaccurate demand estimates can lead to mismatches."
    },
    {
      "topic_label": "Grant Date and Vesting of RSUs, PSUs, and Market-based PSUs Awards",
      "topic_summary": "Specifies how RSUs, PSUs, and market-based PSUs vest over four years or three years, with 25% upfront for some awards and Monte Carlo simulations for market-based PSUs."
    },
    {
      "topic_label": "Share Issuance and Sale",
      "topic_summary": "Explains that shares withheld for tax obligations won’t return to the plan pool. The company or broker may sell shares on behalf of participants."
    },
    {
      "topic_label": "Company Affiliates and Employee Relationships",
      "topic_summary": "Describes conditions for employee termination in a merger if ownership thresholds aren’t met. Discusses substitution or assumption of stock awards and no guaranteed continued employment."
    },
    {
      "topic_label": "Board Committee Discretion",
      "topic_summary": "Grants the Board authority over plan administration, including limitations on transferability of options, discretionary RSU grants, and acceptance of various payment forms."
    }
  ],
  "Product, Market & Operational Strategy": [
    {
      "topic_label": "Cloud Service Providers and Stock Plan Administration Services",
      "topic_summary": "Highlights a 41% increase in data center revenue driven by hyperscale and cloud service providers. Multi-year AI cloud service agreements contributed to growth."
    },
    {
      "topic_label": "NVIDIA Computing Platforms and Software Solutions",
      "topic_summary": "Showcases accelerated computing platforms used in data centers, autonomous vehicles, metaverse, gaming, and more. Highlights AI, robotics, and advanced GPU architectures."
    },
    {
      "topic_label": "Inventory Management and Provisions",
      "topic_summary": "Covers significant judgment in calculating provisions for excess or obsolete inventory and purchase obligations, with $2.17 billion in total inventory charges."
    },
    {
      "topic_label": "NVIDIA AI Cloud Services",
      "topic_summary": "Focuses on enterprise AI offerings like DGX Cloud, pretrained models, and AI Enterprise solutions. Addresses competition, responsible AI usage, and market share."
    },
    {
      "topic_label": "Product Transitions and Demand for New Products",
      "topic_summary": "Explains complexities of shipping new versus legacy products, potential revenue volatility, qualification times, channel inventory reductions, and gray market competition."
    },
    {
      "topic_label": "Revenue Recognition and Performance Obligations",
      "topic_summary": "Describes how revenue is generated from product sales, software licensing, cloud services, and development arrangements, with allowances for returns and extended warranties."
    }
  ],
  "Corporate Governance & Filings": [
    {
      "topic_label": "Proxy Statement Information",
      "topic_summary": "Addresses board governance, director independence, equity plans, and audit committee info found in the 2023 Proxy Statement, including related-party transactions and executive compensation."
    },
    {
      "topic_label": "Securities Exchange Act of 1934 and SEC Filings",
      "topic_summary": "Includes details on annual/quarterly reports, amendments, and allegations of securities law violations. Highlights compliance requirements under the Exchange Act and certification procedures."
    },
    {
      "topic_label": "Disclosure Controls and Procedures in Periodic Report",
      "topic_summary": "Outlines management’s responsibility for ensuring material information is properly disclosed, the efficacy of controls, and potential challenges with ESG reporting and stakeholder expectations."
    }
  ]
  }
,
        "Nvidia-24":{
  "Financial Reporting & Performance": [
    {
      "topic_label": "2024 Fiscal Year Revenue Growth in Various Industries ",
      "topic_summary": "In fiscal year 2024, NVIDIA saw revenue growth in Automotive, Professional Visualization, Data Center, and Gaming. Gross margin improved significantly, and the overall financial condition for FY24 vs. FY23 will be discussed in further detail."
    },
    {
      "topic_label": "Annual Report Form 10-K Notes ",
      "topic_summary": "The Annual Report on Form 10-K discusses the company's investments, accounting policies, equity incentive plans, and other financial matters. Notes in the Consolidated Financial Statements provide additional insights into the company's strategies and financial position."
    },
    {
      "topic_label": "Financial Statements for January 28, 2024 ",
      "topic_summary": "Covers three years of financial data, including marketable and non-marketable equity securities, accumulated amortization of leasehold improvements, RSU/PSU fair values at vesting, and overall compliance with U.S. accounting principles."
    },
    {
      "topic_label": "Financial Condition and Results of Operations ",
      "topic_summary": "Points to sections of the financial report (Item 1A vs. Item 1C) that should be read together for a comprehensive understanding of the company’s financial health, future operations, and growth potential."
    },
    {
      "topic_label": "Financial Expenses for Fiscal Years 2024, 2023, and 2022 ",
      "topic_summary": "Highlights expenses such as contribution costs, depreciation, amortization, operating leases, and cash dividends over three fiscal years. Also notes the overall effect on gross margin and capital investments."
    }
  ],
  "Taxation & Regulatory Compliance": [
    {
      "topic_label": "Income Tax Expense and Benefits",
      "topic_summary": "Details the changes in income tax expense, unrecognized tax benefits, and associated interest/penalties. Explains how tax liabilities may adjust based on new assessments and the overall tax rate differences between FY23 and FY24."
    },
    {
      "topic_label": "USG Licensing Requirements for Exports to China and Country Groups D1, D4, and D5 ",
      "topic_summary": "Describes expanded licensing restrictions on high-performance chips like A100 and H100 for certain countries and entities. Aims to protect national security interests by limiting exports of sensitive AI technology."
    },
    {
      "topic_label": "Securities Exchange Act Reporting Requirements ",
      "topic_summary": "Explains management’s certifications on internal control over financial reporting in Exchange Act periodic reports and clarifies that such certifications are not filed for liability under Section 18 of the Exchange Act."
    },
    {
      "topic_label": "Data Privacy and Security Laws and Regulations ",
      "topic_summary": "Discusses stricter personal data transfer and residency laws, both in the U.S. and globally. Non-compliance can lead to enforcement actions, litigation, and high costs for data localization."
    },
    {
      "topic_label": "Deferred Tax Assets and Valuation Allowance ",
      "topic_summary": "Covers the company’s valuation allowances on deferred tax assets, including capital loss carryforwards. Adjustments depend on projections of future taxable income and the likelihood of realizing these tax benefits."
    }
  ],
  "Corporate Governance & Leadership": [
    {
      "topic_label": "Internal Control over Financial Reporting",
      "topic_summary": "Reports no significant changes in Q4 FY24 that would affect the company's internal control effectiveness. Concludes that internal controls were effective under the COSO framework, with management responsible for ongoing evaluations."
    },
    {
      "topic_label": "Proxy Statement Information ",
      "topic_summary": "Outlines upcoming disclosures on board governance, director independence, equity compensation, and executive compensation in the 2024 Proxy Statement. Incorporates by reference key governance and financial reporting policies."
    },
    {
      "topic_label": "Executive Leadership at NVIDIA Corporation ",
      "topic_summary": "Profiles senior leaders—Debora Shoquist, Colette Kress, Ajay Puri, Timothy Teter—and CEO Jen-Hsun Huang, describing each executive’s role and background. Highlights the corporate structure for cybersecurity and compliance."
    },
    {
      "topic_label": "Share Repurchase Program and Board of Directors",
      "topic_summary": "Discusses Jen-Hsun Huang’s role as founder/CEO, the Board’s decision to increase share repurchases by $25 billion, and governance oversight on compensation, information security, and strategic capital returns."
    },
    {
      "topic_label": "Disclosure Controls and Procedures ",
      "topic_summary": "Emphasizes the company's commitment to transparency, shareholder expectations, and management’s responsibility for accurate financial reporting. Notes that these controls, while effective, may not prevent all errors or fraud."
    }
  ],
  "Investments & Corporate Finance": [
    {
      "topic_label": "Liquidity and Cash Management ",
      "topic_summary": "Focuses on cash flows from operating, investing, and financing activities; classifies debt securities as available-for-sale, and discusses the company’s use of cash for capital investments in the coming fiscal year."
    },
    {
      "topic_label": "Foreign currency risk management with forward contracts ",
      "topic_summary": "Describes how foreign-currency forward contracts offset monetary assets and liabilities denominated in non-U.S. currencies. Gains/losses are recognized in other income and mitigate currency exchange risks."
    },
    {
      "topic_label": "Investment Income and Losses ",
      "topic_summary": "Explains how gains and losses on investments are recorded, including foreign currency remeasurement and realized/unrealized gains on marketable securities. Net impact was not significant in the reported periods."
    },
    {
      "topic_label": "Commercial Paper Program",
      "topic_summary": "Details a $575 million commercial paper program established for general corporate purposes. Notes that no commercial paper was outstanding by FY24-end and references broader corporate financing activities."
    }
  ],
  "Stock Awards, Compensation & Incentives": [
    {
      "topic_label": "Incentive Compensation Policy ",
      "topic_summary": "Covers the recoverability of incentive compensation if based on adjusted financials or stock price. The Committee can use different recovery methods, and covered officers are not entitled to indemnification."
    },
    {
      "topic_label": "Stock-based compensation and equity incentive plans ",
      "topic_summary": "Describes RSUs, PSUs, market-based PSUs, and ESPP. Addresses fair value measurements, vesting schedules, and plan share availability. Market-based PSUs use Monte Carlo simulations to determine fair value."
    }
  ],
  "Revenue & Sales Strategy": [
    {
      "topic_label": "Revenue Recognition and Forecasting for Services and Software Support",
      "topic_summary": "Explains recognition of support and extended warranty revenue over the service period, deferred revenue balances, and risks of reliance on a limited number of partners and distributors."
    },
    {
      "topic_label": "Compute & Networking Segment Revenue Breakdown",
      "topic_summary": "Highlights segment revenue growth, including major customers responsible for large portions of total revenue. Notes increased demand in the U.S. and additions to product warranty liabilities in fiscal years 2024 and 2023."
    },
    {
      "topic_label": "Data Center Product Launch Strategy ",
      "topic_summary": "Focuses on the surge in Data Center revenue (up 217%) and NVIDIA’s full-stack innovation approach, including architecture transitions. Future product launches aim to meet rising AI market needs."
    },
    {
      "topic_label": "Revenue Recognition and Standalone Selling Price ",
      "topic_summary": "Describes how standalone selling price is determined via market data. Contracts with multiple performance obligations are accounted for separately, ensuring accurate allocation and revenue recognition."
    }
  ],
  "Supply Chain & Inventory Management": [
    {
      "topic_label": "Inventory Management and Provisions ",
      "topic_summary": "Highlights complexity in estimating future demand and developing provisions for excess or obsolete inventories. Noted as a critical audit matter with $2.2 billion total inventory/purchase obligation provisions."
    },
    {
      "topic_label": "Operating Lease Liabilities and Assets ",
      "topic_summary": "Explains how lease assets, obligations, and related deferred tax liabilities are recognized based on the present value of lease payments. Shows potential risks in securing supply/capacity if demand changes."
    },
    {
      "topic_label": "Supply Chain Management ",
      "topic_summary": "Addresses challenges with long manufacturing lead times, advanced deposits to secure capacity, and complexities due to shorter product development cycles, new lines of business, and supply constraints."
    },
    {
      "topic_label": "Product Returns and Allowances ",
      "topic_summary": "Focuses on anticipated product return rates, extended useful lives of equipment, and the impact of product transitions on demand/supply mix. Sales return allowances are adjusted based on historical data."
    }
  ],
  "AI, Technology & Business Risks": [
    {
      "topic_label": "Product Transitions and Demand Impact ",
      "topic_summary": "Covers complexities in rolling out new products alongside legacy ones, licensing restrictions for restricted products to China, and potential revenue volatility if licenses are not secured."
    },
    {
      "topic_label": "NVIDIA AI Computing Platform and Software ",
      "topic_summary": "Describes offerings in Data Center, AI enterprise software, autonomous driving, and advanced GPU architectures. Highlights the new DGX Cloud training-as-a-service and expansions into generative AI solutions."
    },
    {
      "topic_label": "Business Risks and Uncertainties ",
      "topic_summary": "Discusses global political instability, critical accounting estimates, insurance coverage, and unknown factors that could negatively affect the company’s reputation, finances, or operations."
    },
    {
      "topic_label": "Impact of Geopolitical Conflict on License and Development Arrangements in Israel ",
      "topic_summary": "Notes potential disruptions to product development due to prolonged employee absences. While not significant yet, extended conflict could impact operations, revenue, and technology license arrangements."
    },
    {
      "topic_label": "Negative impact of export controls on AI technology and business ",
      "topic_summary": "Warns of further restrictions targeting AI-related semiconductors, possibly limiting the export of technology and components, creating competitive disadvantages, and reducing demand in key markets."
    },
    {
      "topic_label": "Risks of AI and Responsible Technology Use )",
      "topic_summary": "Highlights stakeholder concerns over corporate sustainability and responsible AI. Failure to address these could slow AI adoption or lead to reputational, financial, or operational harm."
    },
    {
      "topic_label": "\"Risk Factors and Uncertainties in Annual Report on Form 10-K\" ",
      "topic_summary": "Advises investors to review the Risk Factors section for fluctuating operating results, sustainability issues, regulatory changes, and uncertainties around future share repurchases and market conditions."
    }
  ],
  "Legal & Corporate Litigation": [
    {
      "topic_label": "NVIDIA Corporation and Derivative Lawsuits ",
      "topic_summary": "Discusses a derivative action stayed pending resolution of related securities litigation, involving claims about corporate documents, stock certificates, and agreements or plans of merger."
    },
    {
      "topic_label": "Cryptocurrency Mining and Securities Lawsuits",
      "topic_summary": "Notes ongoing legal actions related to alleged misstatements on the impact of cryptocurrency mining on GPU demand. References potential insider trading and securities law violations, as well as broader market volatility."
    }
  ],
  "Corporate Presence & Brand": [
    {
      "topic_label": "NVIDIA's Presence in Santa Clara, California",
      "topic_summary": "Describes NVIDIA's founding, headquarters, and regional challenges (e.g., wildfires in Northern California). Highlights the company’s broad product and market scope, with AI, automotive, and graphics at the core."
    }
  ]
}
}
'''
# Streamlit App Title
st.title("📊 Topics Super-Grouping using OpenAI")

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
'''

st.title("📊 Topics Super-Grouping (Label and Summary) using OpenAI")

# File Selection Dropdown
selected_file = st.selectbox("Select a File", list(data.keys()))

# Display High-Level Topics (Clusters) based on selected file
if selected_file:
    topics = list(data[selected_file].keys())
    selected_topic = st.selectbox("Select a Cluster", topics)

    # Display all Sub-Level Topics in a scrollable table
    if selected_topic:
        sub_topics = data[selected_file][selected_topic]

        st.subheader(f"Sub-Level Topics for {selected_topic}:")

        # Convert the list of dicts (each with topic_label & topic_summary) into a DataFrame
        table_data = []
        for sub in sub_topics:
            table_data.append({
                "Topic Label": sub["topic_label"], 
                "Topic Summary": sub["topic_summary"]
            })

        df = pd.DataFrame(table_data)

        # Display the DataFrame in a scrollable area
        # Adjust width/height as desired
        st.dataframe(df, width=1000, height=600)