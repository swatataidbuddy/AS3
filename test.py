import streamlit as st
import pandas as pd
import json

# Sample JSON data
sample_json = {
  "Investment Risks and Regulations": [
    {
      "topic_id": "Topic_0",
      "topic_label": "Risks and Considerations of Investing in Common Stock",
      "topic_summary": "The acquisition, sale, or disposal of shares of Common Stock may be subject to insider trading restrictions and market abuse laws in various jurisdictions, including the United States and the shareholder's country. The shares of Common Stock are traded on the Nasdaq exchange under the ticker symbol NVDA. German residents must report the acquisition of shares exceeding a certain value to their local tax office. Investing in shares of Common Stock carries financial risk, and shareholders should be aware of the potential consequences of their participation in the Plan. It is recommended to seek additional information beyond this summary to stay informed about the implications of owning shares of Common Stock."
    },
    {
      "topic_id": "Topic_3",
      "topic_label": "Foreign Asset/Account Reporting Requirements and Exchange Controls.",
      "topic_summary": "Residents of various countries may have specific reporting requirements and exchange controls that could impact their ability to acquire or hold shares of Common Stock under a plan or cash received from participating in the plan. For example, Danish residents must report any accounts holding shares of Common Stock or cash held outside of Denmark to the Danish Tax Administration. Similarly, Palestine residents may face tax, exchange control, or reporting requirements when acquiring, holding, or transferring shares of Common Stock or cash from the plan. In some cases, if the carrying amount of an asset exceeds its estimated future cash flows, an impairment charge may be recognized. Additionally, if proceeds are paid in U.S. dollars, individuals may need to set up a U.S. dollar bank account in China to receive the funds. Overall, it is important to be aware of and comply with any foreign asset/account reporting requirements and exchange controls that may apply."
    },
    {
      "topic_id": "Topic_14",
      "topic_label": "Personal Tax Consultation",
      "topic_summary": "It is important to consult with your personal legal and tax advisors to ensure compliance with local laws and reporting obligations. This will help you understand the applicable requirements and determine the necessary steps to take in order to comply with tax regulations. Consulting with your advisors will also provide you with additional information and details regarding the specific tax laws that may apply to you. For Italian and Spanish residents, it is especially important to seek advice from tax and legal advisors to ensure compliance with personal reporting obligations. Overall, consulting with your personal advisors is crucial in navigating the complex world of tax laws and regulations."
    },
    {
      "topic_id": "Topic_21",
      "topic_label": "Compliance with Section 409A of the Code",
      "topic_summary": "In order to comply with Section 409A of the Code, certain conditions must be met for an event to be considered a Corporate Transaction. This includes a change in ownership or effective control of the Company, or a change in ownership of a substantial portion of the Company's assets. If a Participant holding an Award that constitutes deferred compensation under Section 409A is a specified employee, no distribution or payment can be made until six months after separation from service, unless it complies with Section 409A. The Plan and Award Agreements will be interpreted to be exempt from or in compliance with Section 409A. Deferrals by Participants will also be made in accordance with Section 409A. The Award is intended to comply with U.S. Treasury Regulation Section 1.409A-1(b)(4) to avoid being treated as deferred compensation. Compliance with Section 409A is crucial in determining the occurrence of a Change in Control."
    },
    {
      "topic_id": "Topic_35",
      "topic_label": "Compliance with Exchange Control Laws and Regulations",
      "topic_summary": "It is important for you to adhere to the exchange control laws in various countries, including Czech Republic, Ukraine, India, the United States, South Africa, Taiwan, and Thailand. Failure to comply with these laws may result in fines or penalties. It is your responsibility to ensure that you are following the regulations in each country where you are receiving awards or conducting financial transactions. Consulting with a legal advisor is recommended to understand the specific requirements in each location. The Company and Service Recipient will not be held liable for any consequences resulting from non-compliance with exchange control laws. Compliance with tax laws, securities laws, and other regulations is also necessary to receive your award."
    }
  ],
  "Financial Performance and Reporting": [
    {
      "topic_id": "Topic_1",
      "topic_label": "Annual Report Form 10-K Notes",
      "topic_summary": "The Annual Report on Form 10-K provides detailed information about the financial statements of a company. Notes to the Consolidated Financial Statements in Part IV, Item 15 of the report offer additional details on specific aspects of the company's financial performance. Notes 1, 8, 11, 12, 14, and 17 provide further information on various topics such as investments in non-affiliated entities, equity incentive plans, and other financial discussions. These notes are essential for investors and stakeholders to gain a comprehensive understanding of the company's financial health and performance. It is recommended to refer to these notes for a more in-depth analysis of the company's financial statements."
    },
    {
      "topic_id": "Topic_2",
      "topic_label": "Fiscal Year 2023 Revenue and Financial Performance",
      "topic_summary": "In fiscal year 2023, gaming revenue decreased by 27% to $9.07 billion, while automotive revenue grew by 60% to $903 million. Data Center revenue saw a significant increase of 41% to $15.01 billion. Income tax as a percentage of income before income tax was a benefit of 4.5% in fiscal year 2023, compared to an expense of 1.9% in fiscal year 2022. CMP contributed minimally in fiscal year 2023, in contrast to $550 million in fiscal year 2022. Cash used in financing activities increased in fiscal year 2023 due to share repurchases and no debt issuance proceeds. Professional Visualization revenue for fiscal year 2023 was $1.54 billion, down 27% from fiscal year 2022. The financial condition and results of operations for fiscal year 2023 will be discussed in the first half of fiscal year 2024."
    },
    {
      "topic_id": "Topic_6",
      "topic_label": "Financial Statements for January 29, 2023",
      "topic_summary": "The table provided shows the notional value of foreign currency forward contracts outstanding as of January 29, 2023, and January 30, 2022. The consolidated financial statements for the Company as of these dates are deemed to fairly represent its financial position, operations, and cash flows for the three years leading up to January 29, 2023, in accordance with US accounting principles. The fair value of the contracts was not significant on these dates. Additionally, the statements include information on shareholders' equity, cash flows, valuation accounts, cash equivalents, marketable securities, income, and comprehensive income for the years ending January 29, 2023, January 30, 2022, and January 31, 2021. The total fair value of RSUs and PSUs vested during these years was $4.27 billion, $5.56 billion, and $2.67 billion, respectively."
    },
    {
      "topic_id": "Topic_7",
      "topic_label": "Deferred Tax Assets and Liabilities",
      "topic_summary": "Our policy is to include interest and penalties related to unrecognized tax benefits as a component of income tax expense. We also recognize deferred tax assets as income tax benefits when their realization becomes more likely than not. Our effective tax rate for fiscal years 2022 and 2023 was lower than the U.S. federal statutory rate of 21% due to various tax benefits, including the FDII deduction, stock-based compensation, and research tax credits. We also record a valuation allowance to reduce deferred tax assets by the amount of tax benefits not expected to be realized. Our future effective tax rate may be affected by changes in business, statutory rates, earnings mix, tax incentives, and other factors. Additionally, we recognize federal, state, and foreign deferred tax assets or liabilities for future tax effects related to temporary differences and carryforwards."
    },
    {
      "topic_id": "Topic_12",
      "topic_label": "Internal Control over Financial Reporting",
      "topic_summary": "The company will continue to assess any changes that may impact its internal control over financial reporting each quarter. This includes evaluating any fraud involving management or employees with significant roles in financial reporting. In the second quarter of fiscal year 2023, the company updated its internal control over financial reporting as part of the consolidated financial reporting phase. The audit of internal control included understanding, assessing risks, and testing effectiveness. Management is responsible for maintaining effective internal control and assessing its effectiveness. The company's internal control over financial reporting was deemed effective as of January 29, 2023. Any changes in internal control that could materially affect financial reporting are disclosed in the company's reports. As of January 29, 2023, there have been no material changes in the company's internal control over financial reporting."
    },
    {
      "topic_id": "Topic_22",
      "topic_label": "Financial Expenses for Fiscal Years 2023, 2022, and 2021",
      "topic_summary": "In fiscal years 2023, 2022, and 2021, the company saw an increase in the total intrinsic value of options exercised, with amounts of $642 million, $741 million, and $521 million, respectively. Inventory provisions also increased significantly from $354 million in 2022 to $2.17 billion in 2023. Depreciation expenses rose from $486 million in 2021 to $844 million in 2023. Amortization expenses associated with intangible assets fluctuated over the years. Cash dividends paid to shareholders remained relatively stable. Operating lease expenses and property acquisitions also increased over the years. Sales of previously written-off inventory increased from $111 million in 2022 to $137 million in 2023. Contribution expenses also increased significantly from $120 million in 2021 to $227 million in 2023."
    },
    {
      "topic_id": "Topic_23",
      "topic_label": "Liquidity and Cash Management",
      "topic_summary": "As of January 29, 2023, the company had $13.30 billion in cash, cash equivalents, and marketable securities, a decrease of $7.91 billion from the previous fiscal year. The primary sources of liquidity are cash, marketable securities, and cash generated from operations. The company classifies cash equivalents and marketable securities related to debt securities as available-for-sale. Except for $1.38 billion held outside the U.S., the majority of cash and securities are available for use in the U.S. without additional taxes. Interest income is earned on these assets. In fiscal year 2024, the company plans to use existing funds to invest approximately $1.10 billion to $1.30 billion in property and equipment."
    },
    {
      "topic_id": "Topic_28",
      "topic_label": "Acquisition Termination Cost in Fiscal Year 2023",
      "topic_summary": "In fiscal year 2023, a $1.35 billion acquisition termination cost related to the Arm transaction was recorded in operating expenses, reflecting the write-off of the prepayment provided at signing. This charge contributed to a 50% increase in operating expenses compared to the previous year. Other expenses included stock-based compensation, depreciation, amortization, losses on investments, deferred income taxes, and other non-recurring charges. Cash provided by operating activities decreased due to lower net income adjusted for non-cash items and higher tax payments, partially offset by changes in working capital. The expenses also encompassed corporate infrastructure, restructuring costs, legal settlement costs, and contributions deemed to be enterprise in nature by management. Reconciling items in the \"All Other\" category included various costs and expenses related to acquisitions, restructuring, and legal matters."
    },
    {
      "topic_id": "Topic_39",
      "topic_label": "Disclosure Controls and Procedures in Periodic Report",
      "topic_summary": "As of January 29, 2023, the management of the company, including the Chief Executive Officer and Chief Financial Officer, has determined that the disclosure controls and procedures were effective in providing reasonable assurance. The financial statements and information in the report accurately represent the financial condition, results of operations, and cash flows of the company. The report also includes information on the market for the company's common equity, financial statements, and disclosures about market risk. The management is responsible for establishing and maintaining disclosure controls and procedures to ensure that material information is known to them. While the controls may not prevent all errors or fraud, the management believes they are effective in providing reasonable assurance. The report also addresses the company's ESG practices and the potential challenges in meeting evolving stakeholder expectations."
    },
    {
      "topic_id": "Topic_46",
      "topic_label": "Revenue Recognition and Performance Obligations",
      "topic_summary": "The company generates revenue from contracted license and development arrangements, as well as support for hardware and software. A significant portion of their revenue comes from a few key customers, and losing these customers could have a negative impact on their revenue. For products with a right of return, they establish a sales return allowance based on historical return rates. Revenue is recognized net of allowances for returns, customer programs, and taxes collected. Support and extended warranty revenue are recognized over the service period. Research and development expenses, sales, general, and administrative expenses, and acquisition termination costs are all expressed as a percentage of revenue. Revenue is derived from product sales, software licensing, and cloud services. The revenue from licenses and development services is recognized as a single performance obligation over the period in which the development services are performed."
    },
    {
      "topic_id": "Topic_45",
      "topic_label": "Impact of external factors on business financial results and operations",
      "topic_summary": "The COVID-19 pandemic, climate change, cryptocurrency, and consumer laws are all factors that could negatively impact the financial condition and results of operations of a business. Losses not covered by insurance could also harm the business financially. Political instability and changes in government could further harm the business, financial condition, and results of operations. Additionally, there may be additional risks, trends, and uncertainties that are not currently known or believed to be immaterial that could also harm the business, financial condition, results of operations, or reputation. It is important to carefully consider all of these factors when evaluating the financial statements and other financial information of the business."
    }
  ],
  "Stock Awards and Compensation": [
    {
      "topic_id": "Topic_4",
      "topic_label": "Stock Award Agreements and Plan Terms and Conditions",
      "topic_summary": "Each type of stock award agreement, whether it be a restricted stock award, stock appreciation right, or stock unit award, will be subject to the terms and conditions outlined in the Plan. The agreements will be in a form determined by the Board and will contain appropriate terms and conditions for each participant. The agreements will detail the terms and conditions of the award, as well as any additional terms specific to the participant's country. The agreements will also incorporate the terms of the Plan by reference. Overall, each stock award agreement will be tailored to the individual participant and will adhere to the guidelines set forth in the Plan."
    },
    {
      "topic_id": "Topic_8",
      "topic_label": "Stock Award Assumption and Termination in Corporate Transactions and Change in Control",
      "topic_summary": "Restricted Stock Awards are a type of stock award granted to employees as part of their compensation package. In the event of a Change in Control where the surviving corporation does not assume outstanding Stock Awards, the vesting may be accelerated for current participants. However, for Stock Awards held by others, vesting may not be accelerated and the awards may terminate if not exercised prior to the Change in Control. The Plan also includes other stock awards like Incentive Stock Options and Stock Appreciation Rights, with terms outlined in the Stock Award Agreement. In the event of a Change in Control where Stock Awards are not assumed, vested Stock Awards for current participants will be accelerated to a date determined by the Board, and will terminate if not exercised before the Change in Control."
    },
    {
      "topic_id": "Topic_9",
      "topic_label": "Termination of Continuous Service and Exercise of Awards",
      "topic_summary": "In the event of termination of a participant's continuous service, the options or stock appreciation rights (SARs) granted to them may be subject to different vesting provisions. If the termination is due to death, the options or SARs will become fully vested and exercisable. However, if the termination is for any other reason, the participant may lose the right to participate in the plan and the options or SARs may expire immediately. In the case of restricted stock awards, shares may be subject to forfeiture if not vested at the time of termination. Participants may still be able to exercise their options or SARs in the event of disability, within a specified time frame. Different rules apply for termination for cause or other reasons, with a limited window for exercising options or SARs after termination."
    },
    {
      "topic_id": "Topic_10",
      "topic_label": "Performance Goals and Criteria for Compensation under Section 162(m) of the Code",
      "topic_summary": "Performance Periods can vary in duration and overlap, determined solely by the Committee or Board. Performance Goals are set by the Committee or Board based on Performance Criteria for each period. For awards intended to qualify as performance-based compensation under Section 162(m) of the Code, the Committee can adjust compensation based on various factors. The Committee must certify the satisfaction of Performance Goals before payment, except for stock value increases. Adjustments to Performance Goals calculation methods can be made by the Committee or Board, such as excluding stock-based compensation effects. The Performance Period is the timeframe over which Performance Goals are measured for Stock or Performance Cash Awards. The Committee or Board has sole discretion in determining the length of the Performance Period, the Performance Goals, and the criteria for measuring goal attainment."
    },
    {
      "topic_id": "Topic_11",
      "topic_label": "Stock Award Grants and Agreements",
      "topic_summary": "Stock Awards can be paid out in cash and will only count against the Performance Stock Award limit. Other Stock Award Agreements are written agreements between the Company and the holder of an Other Stock Award outlining the terms and conditions of the grant. Performance Stock Awards are granted under specific terms and conditions and may have accelerated vesting upon a Change in Control. Restricted Stock Unit Awards, Stock Appreciation Rights, Performance Stock Awards, and Other Stock Awards are all types of Stock Awards. If shares are withheld by the Company to satisfy the exercise or purchase price of a Stock Award, those shares will not be available for subsequent issuance under the Plan. If a Performance Stock Award is in the form of an Option, it will only count against the Performance Stock Award limit. A surviving or acquiring corporation may choose to assume or substitute a portion of a Stock Award."
    },
    {
      "topic_id": "Topic_13",
      "topic_label": "Restricted Stock Unit Awards and Agreements",
      "topic_summary": "The Appendix of the Global Restricted Stock Unit Agreement states that terms not defined within it are to be referred to the Plan, Global Restricted Stock Unit Grant Notice, or Global Restricted Stock Unit Agreement. The Board will determine the payment, if any, required by the Participant upon receiving each share of Common Stock from a Restricted Stock Unit Award. NVIDIA Corporation awards a Restricted Stock Unit Award to the Participant under the Amended & Restated 2007 Equity Incentive Plan, as outlined in various agreements and plans. The Participant must adhere to the terms and conditions set forth in the Global Restricted Stock Unit Agreement, including provisions related to law compliance, transfer limitations, tax responsibilities, and the nature of the grant."
    },
    {
      "topic_id": "Topic_16",
      "topic_label": "Stock Option Incentives",
      "topic_summary": "After termination of Continuous Service, if a Participant does not exercise their Option or SAR within the specified time, it will terminate. If an Option is not designated as an Incentive Stock Option, it will be a Nonstatutory Stock Option. The exercise price of each Option or SAR cannot be less than the Fair Market Value on the grant date. The minimum number of shares that can be exercised is subject to Option or SAR provisions. An Incentive Stock Option is intended to qualify as such. An Option or SAR can be transferred under certain circumstances, with an Incentive Stock Option potentially becoming a Nonstatutory Stock Option. There are limitations on Incentive Stock Options. If a Participant dies, the Option or SAR must be exercised within the specified time or it will terminate."
    },
    {
      "topic_id": "Topic_20",
      "topic_label": "Plan Participation and Agreement Acceptance",
      "topic_summary": "By accepting the Award, you agree to participate in the Plan and acknowledge that you have received and reviewed a copy of the Plan and the Agreement. Participation in the Plan is voluntary, and no Awards will be granted while the Plan is suspended or after it is terminated. The Company reserves the right to amend or discontinue your participation in the Plan at any time without liability. Your participation is contingent on your continued service, and if your service ends for any reason except death, your participation in the Plan will cease immediately. The French translation of the Plan and the Agreement will govern your participation unless otherwise indicated. By participating, you fully understand and accept all provisions of the Plan and the Agreement."
    },
    {
      "topic_id": "Topic_29",
      "topic_label": "Tax-Related Items and Service Recipients",
      "topic_summary": "In summary, you are responsible for all Tax-Related Items related to your participation in the Plan, even if the Company or Service Recipient withholds some amount. If you are subject to taxes in multiple jurisdictions, the Company may withhold or account for taxes accordingly. You agree to make arrangements to satisfy all Tax-Related Items and indemnify the Company and Service Recipient for any taxes they are required to pay on your behalf. You are liable for all Tax-Related Items and must pay them when requested. By accepting the Award, you authorize the Company to withhold shares of Common Stock to cover taxes. If there is under-withholding, you may need to pay the Tax-Related Items directly to the tax authority or the Company."
    },
    {
      "topic_id": "Topic_37",
      "topic_label": "Grant Date and Vesting of RSUs, PSUs, and Market-based PSUs Awards",
      "topic_summary": "Under the 2007 Plan, 160 million shares are available for future grants of RSUs, PSUs, and market-based PSUs. The Date of Grant is when the Board approves a grant for an employee. Market-based PSUs vest 100% after approximately three years. RSUs vest over a four-year period, with 25% vesting on a predetermined date and 6.25% quarterly thereafter. PSUs also vest over four years, with 25% vesting initially and 6.25% quarterly. The estimated total grant-date fair value and weighted average grant-date fair value per share are provided for RSUs, PSUs, and market-based PSUs. Recognition of these awards is expected over a weighted average period of 2.6 years. A Monte Carlo simulation is used to estimate the fair value of market-based PSUs. Various equity incentive plans are used to grant stock options, RSUs, PSUs, market-based PSUs, and stock purchase rights."
    },
    {
      "topic_id": "Topic_38",
      "topic_label": "Share Issuance and Sale",
      "topic_summary": "If shares subject to a Stock Award are withheld by the Company for tax purposes, those shares will not be available for future issuance under the Plan. The Company is authorized to instruct its broker to sell the shares on behalf of the Participant, with the proceeds (minus fees and taxes) to be paid to the Participant. If the shares are not sold within 90 days of termination, the Company can mandate the sale. The designated broker is not obligated to sell the shares at a specific price."
    },
    {
      "topic_id": "Topic_40",
      "topic_label": "Dividend Program and Commercial Paper Program",
      "topic_summary": "Following the date of vesting, no cash, stock, or other property related to dividends or distributions will be issued for vested Restricted Stock Units. NVIDIA has repurchased 1.10 billion shares for $17.12 billion through their share repurchase program. The cash dividend program is subject to the Board of Directors' determination. A $575 million commercial paper program supports general corporate purposes. Dividends or dividend equivalents may be paid with respect to shares of Common Stock subject to an Award, but only after the shares have vested and are subject to the terms of the Award Agreement. Any dividends or equivalents credited to unvested shares will be forfeited if the shares are forfeited or repurchased by the Company. In fiscal year 2023, $398 million was paid in quarterly cash dividends. No adjustments will be made to Awards for dividends or distributions not resulting from a Capitalization Adjustment."
    },
    {
      "topic_id": "Topic_41",
      "topic_label": "Company Affiliates and Employee Relationships",
      "topic_summary": "In the event of a merger or similar transaction, if the Company's stockholders do not own more than 50% of the combined voting power of the surviving entity, certain conditions may lead to employee termination. These conditions include breaches of agreement, failure to perform duties, or misconduct harmful to the company. A Change in Control allows for the assumption or substitution of Stock Awards by the surviving or acquiring corporation. Participants have no guaranteed right to continue employment, and termination may occur with or without cause. A Change in Control does not include acquisitions for financing purposes or changes in ownership percentage due to share repurchases, unless the new ownership exceeds a designated threshold, triggering a Change in Control."
    },
    {
      "topic_id": "Topic_42",
      "topic_label": "Board Committee Discretion",
      "topic_summary": "Under Section 5(h), the Board has the sole discretion to make determinations regarding the administration and powers of the Plan. This includes decisions on the sale or disposition of assets, limitations on the transferability of Options and SARs, and the purchase price of Common Stock acquired through Options. The Board may also allow cash payment for Performance Stock Awards and delegate administration to a Committee, granting them the same powers as the Board. The grant of RSUs is also at the sole discretion of the Board, and payment for Restricted Stock Unit Awards can be made in any form acceptable to the Board and permitted by law. The Board's decisions are final and must be made in accordance with applicable laws and the provisions of the Plan."
    }
  ],
  "Cloud Services and Technology": [
    {
      "topic_id": "Topic_5",
      "topic_label": "Cloud Service Providers and Stock Plan Administration Services",
      "topic_summary": "NVIDIA has seen a 41% increase in data center revenue, driven by strong growth from hyperscale customers and purchases made by cloud service providers to support multi-year agreements for AI cloud services and research activities. The company has partnered with leading cloud service providers to host these services in their data centers and has entered into multi-year agreements to support their offerings. They may choose different service providers in the future and share data with them accordingly. The increase in revenue is also attributed to growth in compute and networking services. Additionally, the company has non-inventory purchase obligations of $3.14 billion, including multi-year cloud service agreements."
    },
    {
      "topic_id": "Topic_15",
      "topic_label": "NVIDIA Computing Platforms and Software Solutions",
      "topic_summary": "NVIDIA's Compute & Networking segment focuses on providing accelerated computing platforms for various industries, including data centers, networking, automotive AI, autonomous driving, electric vehicles, robotics, and cryptocurrency mining processors. The company specializes in markets where their computing platforms can significantly accelerate applications. Leveraging their GPU architecture, NVIDIA has created platforms for scientific computing, AI, data science, autonomous vehicles, robotics, metaverse, and 3D internet applications. The Graphics segment includes GeForce GPUs for gaming, Quadro/NVIDIA RTX GPUs for enterprise workstation graphics, vGPU software for cloud-based computing, automotive platforms, and Omniverse Enterprise software for metaverse applications. The Automotive market includes solutions for AV, AI cockpit, electric vehicle computing, and infotainment platforms. NVIDIA continues to advance their accelerated computing platform to meet the growing demand for exceptional 3D graphics and gaming experiences."
    },
    {
      "topic_id": "Topic_24",
      "topic_label": "NVIDIA Corporation and its Subsidiaries",
      "topic_summary": "NVIDIA Corporation has various subsidiaries and holding companies around the world, including NVIDIA Pty Limited, NVIDIA Saudi Limited, and NVIDIA Semiconductor (Shenzhen) Co., Ltd. These entities are part of the NVIDIA Semiconductor Technology and Development network, which includes locations in Shanghai, Beijing, and Singapore. The company also has plans to succeed and continue previous equity incentive plans, such as the 1998 Equity Incentive Plan and the 2000 Nonstatutory Equity Incentive Plan. Additionally, NVIDIA is affiliated with Mellanox Technologies and has various international holdings and subsidiaries in countries like Sweden, the UK, Ukraine, and Brazil. All references to NVIDIA refer to NVIDIA Corporation and its subsidiaries, including NVIDIA Ltd. and NVIDIA New Zealand Limited."
    },
    {
      "topic_id": "Topic_34",
      "topic_label": "NVIDIA AI Cloud Services",
      "topic_summary": "NVIDIA is expanding its AI cloud services for enterprise customers, offering services directly and through partners. These services, such as NVIDIA DGX Cloud and pretrained AI models, require time, resources, and investment to succeed. NVIDIA has also developed language models like NeMo LLM and BioNeMo LLM for cloud AI services. However, competition from other cloud-based services may hinder market share growth. NVIDIA also offers standalone software solutions like AI Enterprise and Omniverse. Concerns about responsible AI use could impact public trust and adoption of AI. Additionally, NVIDIA provides paid licenses for AI Enterprise and vGPU software for virtual desktops. Overall, NVIDIA is working to establish itself as a leader in AI cloud services while addressing challenges in the market."
    },
    {
      "topic_id": "Topic_44",
      "topic_label": "Product Transitions and Demand for New Products",
      "topic_summary": "NVIDIA faces challenges in building technology and products for new use cases and applications that may not yet exist. Product transitions are complex and can negatively impact revenue as new and legacy architecture products are shipped simultaneously. Qualification time for new products, customer anticipation of transitions, and channel partners reducing inventory ahead of new product introductions can lead to revenue reductions or volatility. Demand for products is influenced by various factors, including lead times and engagement with customers in China to provide alternative products not subject to new license requirements. Gray market products and reseller marketplaces also pose competition. NVIDIA must navigate these challenges to effectively meet customer demand and maintain revenue growth."
    }
  ],
  "Inventory and Fair Value Management": [
    {
      "topic_id": "Topic_17",
      "topic_label": "Inventory Management and Provisions",
      "topic_summary": "The Company's inventory provisions primarily pertain to excess quantities of products, based on inventory levels and future purchase commitments compared to assumptions about future demand and market conditions. Management exercises significant judgment in developing provisions for excess or obsolete inventories and excess product purchase commitments, including assumptions related to future demand and market conditions. Inventory provisions for excess inventory and purchase obligations totaled $2.17 billion in fiscal year 2023. The Company charges cost of sales for inventory provisions to write-down inventory for excess or obsolete inventory and for excess product purchase commitments. Procedures were conducted to test the effectiveness of controls over these provisions, including controls over management's assumptions. Misalignment between inventory or supply commitments and product demand may result in inventory provisions. The inventory charges included $1.04 billion for inventory on hand and $1.13 billion for excess inventory purchase obligations."
    },
    {
      "topic_id": "Topic_18",
      "topic_label": "Fair Value Allocation in Acquisitions",
      "topic_summary": "During an acquisition, the fair value and useful life of acquired intangible assets are estimated. The fair value of IPR&D is determined using the Multi-Period Excess Earnings Method. The purchase price of the acquisition is allocated to tangible assets, liabilities, and intangible assets, including IPR&D, based on their estimated fair values. Marketable securities are valued based on quoted market prices, while derivative instruments are recognized as assets or liabilities and measured at fair value. Developed technology's fair value is identified using the Multi-Period Excess Earnings Method. Changes in fair value of contracts are recorded in other income or expense, offsetting changes in fair value of hedged foreign currency denominated assets and liabilities. Any excess of the purchase price over the fair values of net assets acquired is recorded as goodwill. Purchase price is allocated to assets and liabilities based on estimated fair values."
    },
    {
      "topic_id": "Topic_26",
      "topic_label": "Foreign Currency Forward Contracts",
      "topic_summary": "The company uses foreign currency forward contracts to minimize the impact of foreign exchange rate fluctuations on its operating expenses and monetary assets and liabilities denominated in currencies other than the U.S. dollar. With sales in U.S. dollars, direct exposure to foreign exchange rate movements is considered minimal. The notional value of outstanding foreign currency forward contracts as of January 29, 2023, and January 30, 2022, is presented in a table. Changes in fair values of these contracts are offset in other income (expense), net by corresponding changes in fair values of foreign currency denominated monetary assets and liabilities. The company expects realized gains and losses related to these contracts deferred into accumulated other comprehensive income (loss) within the next twelve months to be insignificant. All designated foreign currency forward contracts as of January 29, 2023, mature within eighteen months and are not designated for hedge accounting treatment."
    },
    {
      "topic_id": "Topic_27",
      "topic_label": "Accounting for Gains and Losses on Investments",
      "topic_summary": "The available-for-sale debt securities are reported at fair value with unrealized gains and losses included in accumulated other comprehensive income or loss, a part of shareholders' equity, net of tax. Marketable securities consist of available-for-sale securities reported at fair value with related gains or losses included in accumulated other comprehensive income or loss. Foreign currency remeasurement gains or losses are included in other income or expense. Gains or losses on contracts are recorded in accumulated other comprehensive income or loss and reclassified to operating expense when recognized in earnings. Realized gains and losses on the sale of marketable securities are determined using the specific-identification method and recorded in other income (expense), net. Allowances for credit losses and write-downs are recognized in other income (expense), net. Marketable equity investments in publicly-held companies are recorded at fair value with related gains and losses recognized in other income (expense), net."
    }
  ],
  "Data Privacy and Compliance": [
    {
      "topic_id": "Topic_19",
      "topic_label": "Data Privacy and Processing Regulations",
      "topic_summary": "Certain jurisdictions have implemented data localization and cross-border personal data transfer laws, which may require companies to store and process data within specific geographic boundaries. Failure to comply with these laws can result in severe consequences such as government enforcement actions, litigation, and bans on processing personal data. In the United States, various federal, state, and local laws govern data privacy and security, including regulations for data breach notification and consumer protection. The inability to transfer personal data to the US could have a detrimental impact on business operations and collaborations with parties subject to other data privacy laws. Companies may need to increase their data processing capabilities in Europe or other regions to comply with these regulations, resulting in significant expenses. Data retention and data subject rights are also important considerations for companies handling personal data."
    },
    {
      "topic_id": "Topic_31",
      "topic_label": "Securities Exchange Act of 1934 and SEC Filings",
      "topic_summary": "This certification is not to be considered as filed with the Securities and Exchange Commission or incorporated by reference into any filing under the Securities Act of 1933 or the Exchange Act. Annual and quarterly reports, as well as amendments, are available on the company's website after being filed with the SEC. The amended complaint alleges that NVIDIA and certain executives violated securities laws by making false statements regarding inventory and cryptocurrency mining impact on GPU demand. The Form 10-K is an annual report filed with the SEC, providing detailed financial information about the company. NVIDIA Corporation, a Delaware-based company, has one class of securities registered under the Securities Exchange Act of 1934. The report is signed by authorized individuals on behalf of the company in compliance with SEC regulations."
    },
    {
      "topic_id": "Topic_32",
      "topic_label": "Termination of Arm Acquisition by NVIDIA and SoftBank due to Regulatory Challenges",
      "topic_summary": "In February 2022, NVIDIA and SoftBank terminated the Share Purchase Agreement for NVIDIA to acquire Arm due to significant regulatory challenges. This decision was made as the completion of the transaction was hindered by regulatory issues. Such challenges can have a material impact on business operations and may result in significant costs without achieving substantial revenue. The termination of the agreement highlights the importance of government regulatory reviews in acquisitions and the potential risks involved in such transactions. NVIDIA and SoftBank's decision to end the deal underscores the complexities and uncertainties that can arise in the acquisition process, emphasizing the need for careful consideration and planning when pursuing such opportunities."
    }
  ],
  "Corporate Governance and Proxy Statements": [
    {
      "topic_id": "Topic_25",
      "topic_label": "Proxy Statement Information",
      "topic_summary": "The 2023 Proxy Statement for the company will contain information on recommending directors, ownership of NVIDIA securities, the Audit Committee, equity compensation plans, compliance with Section 16(a) of the Exchange Act, related transactions and director independence, executive compensation, the Code of Conduct, and accounting fees and services. This information will be found under various captions such as Information About the Board of Directors and Corporate Governance, Proposal 1 - Election of Directors, Security Ownership of Certain Beneficial Owners and Management, Report of the Audit Committee of the Board of Directors, Equity Compensation Plan Information, Delinquent Section 16(a) Reports, Review of Transactions with Related Persons, Executive Compensation, Compensation Committee Interlocks and Insider Participation, Director Compensation and Compensation Committee Report, and Fees Billed by the Independent Registered Public Accounting Firm."
    },
    {
      "topic_id": "Topic_43",
      "topic_label": "Executive Leadership at NVIDIA Corporation",
      "topic_summary": "Debora Shoquist, Colette M. Kress, Ajay K. Puri, and Timothy S. Teter are key executives at NVIDIA Corporation. Shoquist joined in 2007 as Senior Vice President of Operations and later became Executive Vice President. Kress joined in 2013 as Executive Vice President and Chief Financial Officer. Puri joined in 2005 and became Executive Vice President of Worldwide Field Operations in 2009. Teter joined in 2017 as Senior Vice President, General Counsel, and Secretary, later becoming Executive Vice President. Jen-Hsun Huang co-founded NVIDIA in 1993 and has been President, CEO, and a Board member since then. Prior to NVIDIA, Shoquist was EVP of Operations at JDS Uniphase Corp, and Kress was CFO at Cisco Systems. The executives certify their knowledge and responsibilities in their respective roles at the company."
    }
  ],
  "Acquisition and Regulatory Challenges": [
    {
      "topic_id": "Topic_30",
      "topic_label": "Long-term Operating Leases and Liabilities",
      "topic_summary": "Operating leases with terms longer than 12 months are reflected in various sections of the consolidated balance sheet, including operating lease assets, accrued and other current liabilities, and long-term operating lease liabilities. These assets represent the right to use an underlying asset for the lease term, while liabilities represent the obligation to make lease payments. The balance sheet also includes accounts payable, short-term and long-term debt, deferred tax liabilities, and other long-term liabilities. Operating lease assets and liabilities are recognized based on the present value of remaining lease payments discounted using the company's incremental borrowing rate. Initial direct costs and prepaid lease payments are included in operating lease assets. As of January 29, 2023, the company's operating leases had a weighted average remaining lease term of 6.8 years and a weighted average discount rate of 3.21%."
    }
  ],
  "Time Management and Updates": [
    {
      "topic_id": "Topic_36",
      "topic_label": "Time Management/Updates",
      "topic_summary": "The summary explains that the time at which an Award may be exercised or vested can be accelerated under certain circumstances, such as the participant's death, disability, or a corporate transaction. The Plan can be amended or modified by the Board at any time. The list of exchange control laws may be updated periodically. Demand predictions may not always be accurate. The company may restructure its businesses or affiliates as needed. Channels for investor relations information may be updated on NVIDIA's website. Changes in time commitment may occur. The Plan can be accessed through an online system provided by the Company. Inaccurate estimates of customer demand could lead to supply and demand mismatches."
    }
  ],
  "Securities and Financial Markets": [
    {
      "topic_id": "Topic_33",
      "topic_label": "United States debt securities and financial markets",
      "topic_summary": "Our semiconductor wafers are primarily manufactured, assembled, tested, and packaged by third parties outside of the United States, with 69% of our revenue coming from international sales in fiscal year 2023. We are subject to taxation in both the US and other countries. Our investments include corporate debt securities, US Treasury debt securities, government agency debt securities, certificates of deposit, money market funds, and foreign government bonds. We hold patents in the US and abroad. The company and its service providers, including Schwab, are US-based, requiring the transfer and processing of personal data in the US. Foreign laws may not offer the same level of protection for our products and intellectual property rights as US law."
    }
  ],
  "NVIDIA Headquarters and Operations": [
    {
      "topic_id": "Topic_47",
      "topic_label": "NVIDIA Headquarters and Operations in Santa Clara, California",
      "topic_summary": "The company is based in Santa Clara, California, with offices located at 2788 San Tomas Expressway. The company is responsible for the administration of the Plan and may be affected by power safety shut offs due to wildfire risk in Northern California. NVIDIA Corporation, incorporated in California in 1993 and reincorporated in Delaware in 1998, acknowledges the exclusive jurisdiction of the State of California for any disputes. The company also leases data center space in Santa Clara and may be impacted by extreme weather conditions. The company's employees may face challenges in working effectively during such conditions. Additionally, the company's headquarters in Santa Clara may be affected by adverse implications due to the extreme heat, wind, and dry conditions in Northern California."
    }
  ]
}


st.title("Cluster Data Viewer")
import re
# Text area to input JSON data
#json_input = st.text_area("Paste your JSON data here:", sample_json, height=200)
#import pdb;pdb.set_trace()
# Try to parse JSON
try:
    #leaned_response = re.sub(r"```json\n|\n```", "", json_input.strip())
    data = sample_json
except json.JSONDecodeError:
    st.error("Invalid JSON format. Please correct and try again.")
    st.stop()

# Dropdown for cluster selection
cluster_names = list(data.keys())
selected_cluster = st.selectbox("Select a Cluster:", cluster_names)

# Extract and display data for the selected cluster
if selected_cluster:
    cluster_data = data[selected_cluster]
    df = pd.DataFrame(cluster_data)[["topic_label", "topic_summary"]]  # Remove 'topic_id' column
    st.write(f"### Details for {selected_cluster}")
    st.dataframe(df, height=500)  # Larger table height for better visibility


