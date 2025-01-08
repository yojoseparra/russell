
### UNDER CONSTRUCTION ...
## Russell 2000 components: Financial analysis based on Reese Interpretation of Warren Buffett

### Project Description

The problem that we want to solve is to be able to compare the financials of two companies in the same industries or the same company across the years in an easy manner. The objective is to be able to see how the company is changing accross the years and related to the competition.

This comes in handy when we have to manage a portfolio of public traded companies. Since, once evaluating a holding, we want to be aware through the changes of the company at many levels, this is nearly impossible for a regular analyst without standardizing the financial data.

Finnaly, we want to have a single value of comparison for companies that summarize how close is the data from one period to the next. This is important to identify simmilar companies or estable companies overtime. To do this we use the 'cosine distance' with values between -1 0 1. values close to -1 or 1 indicate high simmilarity. 

### Methodology

* Russell 2000 composite
  
   The first step was filtering companies with financials that we consider sound and stable. Based on any theoretical concepts and the methodology explained by Reese in his book 'The Guru Investor'. Particularly, in the page 109 regarding 'The Buffett Strategy: Step by Step', we find answers to what is like a sound and estable company. The REESE method to look for companies based on numeric criteria in the vein of Warren Buffett investment ideas. 
   
   This is an analysis of the Russell 2000 stocks from data comming from Yahoo finance.  Close to 2000 companies were screened, with yearly finanacials from 2020-2023. The full Warren Buffett investment technique is described by REESE book  The Guru Investor pag. 111. The metodology is simple. It is of interest group companies based on financials, regardless the industry of size. In the search of a 'good' company as described by REESE we want to normalize and scale the data. To scale the data we divide by its yearly revenue.
   
   To normalize the data we use basic vector normalization to feed the data into a function that calculates the cosine distance. 
   
   Any of the Reese method based on his Buffett approach.
   1. Earnings Predictability Y1 > Y2... >Yn

   Searching in DB the candidates based on increasing yearly EPS in the last 4 years. While doing this analysis, we noticed there were interesting materials producer companies that had steady earnings growth with high debt level.

   2. Long Term Debt < 5 earnings.

   3. Return On equity
   
   The idea i sto use ROIC defined as NOPAT/ Invested Capital, where NOPAT = EBIT(1-Tax Rate). Invested Capital= Total Debt+Equity−Cash and Cash Equivalents.

   Basic normalization and cosine formulas are available on Wikipedia.

* Standard portfolio comparison. 
  
  After finding companies that are good in terms of the bibliography here exposed, we compare this companies with the companies in our portfolio and the 'wide MOAT' companies from Morningstar. 


#### Database

Another objective for this programming exercise is to create a Postgres database to store our data. The objective is to apply the CDISC methodology to make the data structurally more sound. This is not easy as CDISC is deemed for clinical trials research. Nevertheless, there are more standards for that in the pharmaceutical industry than in the financial industry. Data structure and data governance is very important in the long term, the idea is to give a glimpse of that in the database. 

### Data Download and exploration

Data was filtered based on the parameters explained in the methodology section. Data from Yahoo was download and programatically and visually analyzed. Few candidates were analyzed.

Table 1. 
| subjid_x | sctestcd                                                   | fiperiod_x_x | 9/30/2021 | 9/30/2022 | subjid_y | 6/30/2024 | 6/30/2024 |
|----------|------------------------------------------------------------|--------------|-----------|-----------|----------|-----------|-----------|
|          |                                                            |              | fistresn  | chg       |          | fistresn  | chg       |
| AAPL     | Cash And Cash Equivalents                                  | 12M          | 10%       | -32%      | MSFT     | 7%        | -47%      |
| AAPL     | Cash Equivalents                                           | 12M          | 5%        | -71%      | MSFT     | 3%        | -74%      |
| AAPL     | Cash Financial                                             | 12M          | 5%        | 7%        | MSFT     | 5%        | 36%       |
| AAPL     | Cash Cash Equivalents And Short Term Investments           | 12M          | 17%       | -23%      | MSFT     | 31%       | -32%      |
| AAPL     | Commercial Paper                                           | 12M          | 2%        | 66%       |          |           |           |
| AAPL     | Accounts Receivable                                        | 12M          | 7%        | 7%        | MSFT     | 23%       | 17%       |
|          | Gross Accounts Receivable                                  |              |           |           | MSFT     | 24%       | 17%       |
|          | Allowance For Doubtful Accounts Receivable                 |              |           |           | MSFT     | 0%        | 28%       |
| AAPL     | Inventory                                                  | 12M          | 2%        | -25%      | MSFT     | 1%        | -50%      |
|          | Raw Materials                                              |              |           |           | MSFT     | 0%        | -44%      |
|          | Work In Process                                            |              |           |           | MSFT     | 0%        | -70%      |
| AAPL     | Current Assets                                             | 12M          | 37%       | 0%        | MSFT     | 65%       | -13%      |
|          | Finished Goods                                             |              |           |           | MSFT     | 0%        | -52%      |
| AAPL     | Receivables                                                | 12M          | 14%       | 18%       | MSFT     | 23%       | 17%       |
|          | Hedging Assets Current                                     |              |           |           | MSFT     | 0%        | 100%      |
| AAPL     | Other Current Assets                                       | 12M          | 4%        | 50%       | MSFT     | 11%       | 19%       |
| AAPL     | Gross PPE                                                  | 12M          | 33%       | 4%        | MSFT     | 94%       | 30%       |
| AAPL     | Accumulated Depreciation                                   | 12M          | -19%      | 3%        | MSFT     | -31%      | 12%       |
| AAPL     | Net PPE                                                    | 12M          | 14%       | 6%        | MSFT     | 63%       | 41%       |
| AAPL     | Land And Improvements                                      | 12M          | 5%        | 10%       | MSFT     | 3%        | 44%       |
|          | Buildings And Improvements                                 |              |           |           | MSFT     | 38%       | 37%       |
| AAPL     | Machinery Furniture Equipment                              | 12M          | 22%       | 3%        | MSFT     | 41%       | 24%       |
| AAPL     | Investments And Advances                                   | 12M          | 35%       | -6%       | MSFT     | 6%        | 48%       |
| AAPL     | Investmentin Financial Assets                              | 12M          | 35%       | -6%       |          |           |           |
|          | Goodwill                                                   |              |           |           | MSFT     | 49%       | 76%       |
|          | Goodwill And Other Intangible Assets                       |              |           |           | MSFT     | 60%       | 90%       |
|          | Other Intangible Assets                                    |              |           |           | MSFT     | 11%       | 195%      |
| AAPL     | Leases                                                     | 12M          | 3%        | 2%        | MSFT     | 4%        | 12%       |
| AAPL     | Other Properties                                           | 12M          | 3%        | 3%        | MSFT     | 8%        | 32%       |
| AAPL     | Properties                                                 | 12M          | 0%        |           | MSFT     | 0%        |           |
| AAPL     | Non Current Deferred Assets                                | 12M          |           |           |          |           |           |
| AAPL     | Available For Sale Securities                              | 12M          | 35%       | -6%       |          |           |           |
| AAPL     | Other Non Current Assets                                   | 12M          | 11%       | -26%      | MSFT     | 15%       | 19%       |
| AAPL     | Other Investments                                          | 12M          | 35%       | -6%       |          |           |           |
| AAPL     | Net Tangible Assets                                        | 12M          | 17%       | -20%      | MSFT     | 50%       | -6%       |
| AAPL     | Other Short Term Investments                               | 12M          | 8%        | -11%      | MSFT     | 23%       | -25%      |
| AAPL     | Total Assets                                               | 12M          | 96%       | 0%        | MSFT     | 209%      | 24%       |
| AAPL     | Accounts Payable                                           | 12M          | 15%       | 17%       | MSFT     | 9%        | 22%       |
| AAPL     | Payables                                                   | 12M          | 15%       | 29%       | MSFT     | 11%       | 21%       |
| AAPL     | Payables And Accrued Expenses                              | 12M          | 15%       | 29%       | MSFT     | 11%       | 21%       |
| AAPL     | Income Tax Payable                                         | 12M          |           |           | MSFT     | 2%        | 21%       |
| AAPL     | Other Current Liabilities                                  | 12M          | 13%       | 15%       | MSFT     | 8%        | 30%       |
| AAPL     | Current Liabilities                                        | 12M          | 34%       | 23%       | MSFT     | 51%       | 20%       |
|          | Pensionand Other Post Retirement Benefit Plans Current     |              |           |           | MSFT     | 5%        | 14%       |
| AAPL     | Current Deferred Revenue                                   | 12M          | 2%        | 4%        | MSFT     | 23%       | 13%       |
| AAPL     | Other Current Borrowings                                   | 12M          | 3%        | 16%       |          |           |           |
| AAPL     | Current Debt                                               | 12M          | 4%        | 35%       | MSFT     | 4%        | 70%       |
| AAPL     | Current Debt And Capital Lease Obligation                  | 12M          | 5%        | 33%       | MSFT     | 4%        | 70%       |
| AAPL     | Current Capital Lease Obligation                           | 12M          | 0%        | 9%        |          |           |           |
| AAPL     | Long Term Debt                                             | 12M          | 30%       | -9%       | MSFT     | 17%       | 2%        |
| AAPL     | Current Deferred Liabilities                               | 12M          | 2%        | 4%        | MSFT     | 23%       | 13%       |
| AAPL     | Long Term Capital Lease Obligation                         | 12M          | 3%        | 5%        | MSFT     | 6%        | 22%       |
| AAPL     | Long Term Debt And Capital Lease Obligation                | 12M          | 33%       | -8%       | MSFT     | 24%       | 6%        |
|          | Long Term Equity Investment                                |              |           |           | MSFT     | 6%        | 48%       |
|          | Non Current Deferred Liabilities                           |              |           |           | MSFT     | 2%        | 56%       |
|          | Non Current Deferred Revenue                               |              |           |           | MSFT     | 1%        | -11%      |
| AAPL     | Non Current Deferred Taxes Assets                          | 12M          |           |           |          |           |           |
|          | Non Current Deferred Taxes Liabilities                     |              |           |           | MSFT     | 1%        | 505%      |
| AAPL     | Tradeand Other Payables Non Current                        | 12M          | 7%        | -33%      | MSFT     | 11%       | 9%        |
| AAPL     | Other Non Current Liabilities                              | 12M          | 5%        | 18%       | MSFT     | 11%       | 51%       |
| AAPL     | Total Liabilities Net Minority Interest                    | 12M          | 79%       | 5%        | MSFT     | 99%       | 18%       |
| AAPL     | Common Stock                                               | 12M          | 16%       | 13%       | MSFT     | 41%       | 8%        |
| AAPL     | Common Stock Equity                                        | 12M          | 17%       | -20%      | MSFT     | 110%      | 30%       |
| AAPL     | Capital Lease Obligations                                  | 12M          | 3%        | 5%        | MSFT     | 6%        | 22%       |
| AAPL     | Capital Stock                                              | 12M          | 16%       | 13%       | MSFT     | 41%       | 8%        |
| AAPL     | Retained Earnings                                          | 12M          | 2%        | -155%     | MSFT     | 71%       | 46%       |
| AAPL     | Tangible Book Value                                        | 12M          | 17%       | -20%      | MSFT     | 50%       | -6%       |
| AAPL     | Other Equity Adjustments                                   | 12M          | 0%        | -6915%    | MSFT     | -2%       | -12%      |
| AAPL     | Gains Losses Not Affecting Retained Earnings               | 12M          | 0%        | -6915%    | MSFT     | -2%       | -12%      |
| AAPL     | Treasury Shares Number                                     | 12M          |           |           |          |           |           |
| AAPL     | Total Equity Gross Minority Interest                       | 12M          | 17%       | -20%      | MSFT     | 110%      | 30%       |
| AAPL     | Net Debt                                                   | 12M          | 25%       | 7%        | MSFT     | 14%       | 166%      |
| AAPL     | Total Debt                                                 | 12M          | 37%       | -3%       | MSFT     | 27%       | 12%       |
| AAPL     | Total Capitalization                                       | 12M          | 47%       | -13%      | MSFT     | 127%      | 25%       |
| AAPL     | Working Capital                                            | 12M          | 3%        | -299%     | MSFT     | 14%       | -57%      |
| AAPL     | Ordinary Shares Number                                     | 12M          | 4%        | -3%       | MSFT     | 3%        | 0%        |
| AAPL     | Stockholders Equity                                        | 12M          | 17%       | -20%      | MSFT     | 110%      | 30%       |
| AAPL     | Share Issued                                               | 12M          | 4%        | -3%       | MSFT     | 3%        | 0%        |
| AAPL     | Total Non Current Assets                                   | 12M          | 59%       | 1%        | MSFT     | 144%      | 55%       |
| AAPL     | Total Non Current Liabilities Net Minority Interest        | 12M          | 44%       | -9%       | MSFT     | 48%       | 17%       |
| AAPL     | Total Tax Payable                                          | 12M          |           |           | MSFT     | 2%        | 21%       |
| AAPL     | Other Receivables                                          | 12M          | 7%        | 30%       |          |           |           |
| AAPL     | Invested Capital                                           | 12M          | 51%       | -9%       | MSFT     | 131%      | 26%       |
| AAPL     | Change In Account Payable                                  | 12M          | 3%        | -23%      | MSFT     | 1%        | -230%     |
| AAPL     | Change In Payable                                          | 12M          | 3%        | -23%      | MSFT     | 2%        | -270%     |
| AAPL     | Income Tax Paid Supplemental Data                          | 12M          | 7%        | -23%      |          |           |           |
| AAPL     | Change In Payables And Accrued Expense                     | 12M          | 3%        | -23%      | MSFT     | 2%        | -270%     |
| AAPL     | Change In Other Current Liabilities                        | 12M          | 2%        | -18%      | MSFT     | 2%        | 99%       |
| AAPL     | Change In Other Working Capital                            | 12M          | 0%        | -71%      | MSFT     | 2%        | -3%       |
| AAPL     | Change In Inventory                                        | 12M          | -1%       | -156%     | MSFT     | 1%        | 3%        |
| AAPL     | Change In Receivables                                      | 12M          | -4%       | -33%      | MSFT     | -3%       | 76%       |
|          | Change In Tax Payable                                      |              |           |           | MSFT     | 1%        | -571%     |
| AAPL     | Change In Working Capital                                  | 12M          | -1%       | -124%     | MSFT     | 1%        | -176%     |
|          | Change In Income Tax Payable                               |              |           |           | MSFT     | 1%        | -571%     |
| AAPL     | Deferred Income Tax                                        | 12M          | -1%       | -119%     | MSFT     | -2%       | -22%      |
| AAPL     | Deferred Tax                                               | 12M          | -1%       | -119%     | MSFT     | -2%       | -22%      |
| AAPL     | Changes In Account Receivables                             | 12M          | -3%       | -82%      | MSFT     | -3%       | 76%       |
| AAPL     | Change In Other Current Assets                             | 12M          | -2%       | -19%      | MSFT     | -3%       | 75%       |
|          | Depreciation                                               |              |           |           | MSFT     | 9%        | 61%       |
| AAPL     | Depreciation Amortization Depletion                        | 12M          | 3%        | -2%       | MSFT     | 9%        | 61%       |
| AAPL     | Depreciation And Amortization                              | 12M          | 3%        | -2%       | MSFT     | 9%        | 61%       |
| AAPL     | Stock Based Compensation                                   | 12M          | 2%        | 14%       | MSFT     | 4%        | 12%       |
| AAPL     | Interest Paid Supplemental Data                            | 12M          | 1%        | 7%        |          |           |           |
|          | Gain Loss On Investment Securities                         |              |           |           | MSFT     |           |           |
|          | Operating Gains Losses                                     |              |           |           | MSFT     | 0%        | 56%       |
| AAPL     | Other Non Cash Items                                       | 12M          | -1%       | -120%     |          |           |           |
| AAPL     | Operating Cash Flow                                        | 12M          | 28%       | 17%       | MSFT     | 48%       | 35%       |
| AAPL     | Cash Flow From Continuing Operating Activities             | 12M          | 28%       | 17%       | MSFT     | 48%       | 35%       |
| AAPL     | Sale Of Investment                                         | 12M          | 29%       | -37%      | MSFT     | 15%       | -25%      |
| AAPL     | Purchase Of Business                                       | 12M          | 0%        | 827%      | MSFT     | -28%      | 4040%     |
| AAPL     | Purchase Of PPE                                            | 12M          | -3%       | -3%       | MSFT     | -18%      | 58%       |
| AAPL     | Purchase Of Investment                                     | 12M          | -30%      | -30%      | MSFT     | -7%       | -53%      |
| AAPL     | Net PPEPurchase And Sale                                   | 12M          | -3%       | -3%       | MSFT     | -18%      | 58%       |
| AAPL     | Net Business Purchase And Sale                             | 12M          | 0%        | 827%      | MSFT     | -28%      | 4040%     |
| AAPL     | Net Income                                                 | 12M          | 26%       | 5%        | MSFT     | 36%       | 22%       |
| AAPL     | Net Income From Continuing Operations                      | 12M          | 26%       | 5%        | MSFT     | 36%       | 22%       |
| AAPL     | Net Investment Purchase And Sale                           | 12M          | -1%       | 211%      | MSFT     | 7%        | 76%       |
| AAPL     | Cash Flow From Continuing Investing Activities             | 12M          | -4%       | 54%       | MSFT     | -40%      | 328%      |
| AAPL     | Investing Cash Flow                                        | 12M          | -4%       | 54%       | MSFT     | -40%      | 328%      |
| AAPL     | Issuance Of Debt                                           | 12M          | 6%        | -73%      | MSFT     | 12%       | inf%      |
| AAPL     | Long Term Debt Issuance                                    | 12M          | 6%        | -73%      | MSFT     | 10%       | inf%      |
|          | Short Term Debt Issuance                                   |              |           |           | MSFT     | 2%        | inf%      |
| AAPL     | Net Short Term Debt Issuance                               | 12M          | 0%        | 287%      | MSFT     | 2%        | inf%      |
| AAPL     | Net Long Term Debt Issuance                                | 12M          | 3%        | -135%     | MSFT     | -2%       | 70%       |
| AAPL     | Issuance Of Capital Stock                                  | 12M          | 0%        |           | MSFT     | 1%        | 7%        |
| AAPL     | Common Stock Issuance                                      | 12M          | 0%        |           | MSFT     | 1%        | 7%        |
| AAPL     | Repayment Of Debt                                          | 12M          | -2%       | 9%        | MSFT     | -12%      | 957%      |
| AAPL     | Long Term Debt Payments                                    | 12M          | -2%       | 9%        | MSFT     | -12%      | 957%      |
| AAPL     | Net Issuance Payments Of Debt                              | 12M          | 3%        | -101%     | MSFT     | 0%        | -121%     |
| AAPL     | Common Stock Payments                                      | 12M          | -24%      | 4%        | MSFT     | -7%       | -22%      |
| AAPL     | Cash Dividends Paid                                        | 12M          | -4%       | 3%        | MSFT     | -9%       | 10%       |
| AAPL     | Capital Expenditure                                        | 12M          | -3%       | -3%       | MSFT     | -18%      | 58%       |
| AAPL     | Repurchase Of Capital Stock                                | 12M          | -24%      | 4%        | MSFT     | -7%       | -22%      |
| AAPL     | Net Common Stock Issuance                                  | 12M          | -24%      | 4%        | MSFT     | -6%       | -25%      |
| AAPL     | Net Other Financing Charges                                | 12M          | -2%       | 14%       | MSFT     | -1%       | 30%       |
| AAPL     | Financing Cash Flow                                        | 12M          | -26%      | 19%       | MSFT     | -15%      | -14%      |
| AAPL     | Cash Flow From Continuing Financing Activities             | 12M          | -26%      | 19%       | MSFT     | -15%      | -14%      |
| AAPL     | Beginning Cash Position                                    | 12M          | 11%       | -10%      | MSFT     | 14%       | 149%      |
| AAPL     | Net Other Investing Changes                                | 12M          | 0%        | 442%      | MSFT     | -1%       | -58%      |
| AAPL     | End Cash Position                                          | 12M          | 10%       | -30%      | MSFT     | 7%        | -47%      |
| AAPL     | Changes In Cash                                            | 12M          | -1%       | 184%      | MSFT     | -7%       | -177%     |
| AAPL     | Change In Cash Supplemental As Reported                    | 12M          | -1%       | 184%      | MSFT     | -7%       | -179%     |
|          | Effect Of Exchange Rate Changes                            |              |           |           | MSFT     | 0%        | 8%        |
| AAPL     | Free Cash Flow                                             | 12M          | 25%       | 20%       | MSFT     | 30%       | 25%       |
| AAPL     | Other Non Cash Items                                       | 12M          | -1%       | -120%     |          |           |           |
| AAPL     | Common Stock Dividend Paid                                 | 12M          | -4%       | 3%        | MSFT     | -9%       | 10%       |
| AAPL     | Total Revenue                                              | 12M          | 100%      | 8%        | MSFT     | 100%      | 16%       |
| AAPL     | Operating Revenue                                          | 12M          | 100%      | 8%        | MSFT     | 100%      | 16%       |
| AAPL     | Cost Of Revenue                                            | 12M          | 58%       | 5%        | MSFT     | 30%       | 13%       |
| AAPL     | Reconciled Cost Of Revenue                                 | 12M          | 58%       | 5%        | MSFT     | 30%       | 13%       |
| AAPL     | Gross Profit                                               | 12M          | 42%       | 12%       | MSFT     | 70%       | 17%       |
| AAPL     | Research And Development                                   | 12M          | 6%        | 20%       | MSFT     | 12%       | 9%        |
|          | Selling And Marketing Expense                              |              |           |           | MSFT     | 10%       | 7%        |
| AAPL     | Selling General And Administration                         | 12M          | 6%        | 14%       | MSFT     | 13%       | 6%        |
|          | General And Administrative Expense                         |              |           |           | MSFT     | 3%        | 0%        |
| AAPL     | Reconciled Depreciation                                    | 12M          | 3%        | -2%       | MSFT     | 9%        | 61%       |
| AAPL     | Operating Expense                                          | 12M          | 12%       | 17%       | MSFT     | 25%       | 7%        |
| AAPL     | EBIT                                                       | 12M          | 31%       | 7%        | MSFT     | 45%       | 21%       |
| AAPL     | Operating Income                                           | 12M          | 30%       | 10%       | MSFT     | 45%       | 24%       |
| AAPL     | Interest Income                                            | 12M          | 1%        | -1%       | MSFT     | 1%        | 5%        |
| AAPL     | Interest Income Non Operating                              | 12M          | 1%        | -1%       | MSFT     | 1%        | 5%        |
| AAPL     | Interest Expense                                           | 12M          | 1%        | 11%       | MSFT     | 1%        | 49%       |
| AAPL     | Interest Expense Non Operating                             | 12M          | 1%        | 11%       | MSFT     | 1%        | 49%       |
| AAPL     | Net Interest Income                                        | 12M          | 0%        | -154%     | MSFT     | 0%        | -78%      |
| AAPL     | Net Non Operating Interest Income Expense                  | 12M          | 0%        | -154%     | MSFT     | 0%        | -78%      |
| AAPL     | Other Income Expense                                       | 12M          | 0%        | -657%     | MSFT     | -1%       | 685%      |
| AAPL     | Other Non Operating Income Expenses                        | 12M          | 0%        | -657%     | MSFT     | -1%       | 491%      |
|          | Gain On Sale Of Security                                   |              |           |           | MSFT     | 0%        | -2387%    |
| AAPL     | Pretax Income                                              | 12M          | 30%       | 9%        | MSFT     | 44%       | 21%       |
| AAPL     | Tax Provision                                              | 12M          | 4%        | 33%       | MSFT     | 8%        | 16%       |
| AAPL     | Tax Effect Of Unusual Items                                | 12M          | 0%        |           | MSFT     | 0%        | 3406%     |
| AAPL     | Tax Rate For Calcs                                         | 12M          | 0%        | 22%       | MSFT     | 0%        | -4%       |
| AAPL     | Net Income                                                 | 12M          | 26%       | 5%        | MSFT     | 36%       | 22%       |
| AAPL     | Net Income Common Stockholders                             | 12M          | 26%       | 5%        | MSFT     | 36%       | 22%       |
| AAPL     | Net Income Continuous Operations                           | 12M          | 26%       | 5%        | MSFT     | 36%       | 22%       |
| AAPL     | Net Income From Continuing And Discontinued Operation      | 12M          | 26%       | 5%        | MSFT     | 36%       | 22%       |
| AAPL     | Net Income From Continuing Operation Net Minority Interest | 12M          | 26%       | 5%        | MSFT     | 36%       | 22%       |
| AAPL     | Net Income Including Noncontrolling Interests              | 12M          | 26%       | 5%        | MSFT     | 36%       | 22%       |
| AAPL     | Normalized Income                                          | 12M          | 26%       | 5%        | MSFT     | 36%       | 22%       |
| AAPL     | Diluted NIAvailto Com Stockholders                         | 12M          | 26%       | 5%        | MSFT     | 36%       | 22%       |
| AAPL     | Basic EPS                                                  | 12M          | 0%        | 8%        | MSFT     | 0%        | 22%       |
| AAPL     | Diluted EPS                                                | 12M          | 0%        | 9%        | MSFT     | 0%        | 22%       |
| AAPL     | Basic Average Shares                                       | 12M          | 5%        | -3%       | MSFT     | 3%        | 0%        |
| AAPL     | Diluted Average Shares                                     | 12M          | 5%        | -3%       | MSFT     | 3%        | 0%        |
| AAPL     | EBITDA                                                     | 12M          | 34%       | 6%        | MSFT     | 54%       | 27%       |
| AAPL     | Normalized EBITDA                                          | 12M          | 34%       | 6%        | MSFT     | 54%       | 27%       |
| AAPL     | Total Expenses                                             | 12M          | 70%       | 7%        | MSFT     | 55%       | 10%       |
| AAPL     | Total Operating Income As Reported                         | 12M          | 30%       | 10%       | MSFT     | 45%       | 24%       |
|          | Special Income Charges                                     |              |           |           | MSFT     | 0%        | 587%      |
|          | Write Off                                                  |              |           |           | MSFT     | 0%        | 587%      |
|          | Total Unusual Items                                        |              |           |           | MSFT     | 0%        | 3560%     |
|          | Total Unusual Items Excluding Goodwill                     |              |           |           | MSFT     | 0%        | 3560%     |
|          | Other Gand A                                               |              |           |           | MSFT     | 3%        | 0%        |


Using a Basic research method based on Reese approach to Warren Buffett way of investing, we came accross with Coca-Cola (COKE) thus, the method might be interesting indeed. We came accross with CHRD which is a company in the oil industry. Buffett has companies in this sector. Notice that the method requires 10Y statement analysis, here we consider only 4Y and yet, from about 2000 companies, we get less than 10 that fullfill this basic criteria. Notice COKE dropped from the Russell 2000 index in 2024, but it was up to 2023.

There are other requirements with many projections like free cash flow and stock price and return on investment in the comming 10 years. Thinking this is Buffett method is controversial. Therefore, we stop here. We just want to identify a bunch of good companies based in these basic numbers. This is wider accepted, i.e. a company with low debt, with hight ROE, and with strong margins and low capital expenditure is a good company. Other aspects are less numerical, like re-investment oportunities or protective moat. This wont be quantified.

Notice additionally, that we rely on yahoo, as it provide us with already standardize data, but we need at least 10 years of financials, or we may be interested in small or unknown companies requiring finacial standardization, just to be able to fee the data into the model.



One approach to make companies more comparable is to present all financial data in terms of the percentage respect to the total revenue. This way we center all data arround 1. This way te embeddings will be more comparable accross companies. 
The following is the SQL query. EBIT > 30% and Total debt less than 3X its revenue. These requirements are 'at least once' or at least in one of the years analyzed.
So far there is only one company that summarizes what we are looking for. Casually, it is undervalued. Its name is Diodes Inc. Hereunder its profile
Diodes Incorporated, together with its subsidiaries, manufactures and supplies application-specific standard products in the broad discrete, logic, analog, and mixed-signal semiconductor markets worldwide. The company offers discrete semiconductor products, such as MOSFETs, SiC MOSFETs; data line protection, power line protection, thyristers, USB Type-C protection, and transient voltage suppressors; Schottky, small signal switching, Zener, and SiC diodes; bridges, super barrier, Schottky, Schottky bridge, and fast/ultra-fast rectifiers; and bipolar, avalanche, gate driver, and pre-bias transistors. It also provides analog products, including power management devices comprising AC-DC and DC-DC converters, USB power switches, low dropout, photocoupler and linear voltage regulators; standard linear devices consisting of operational amplifiers and comparators, current monitors, voltage references, and reset generators; LED lighting drivers; audio amplifiers; and sensor products, such as hall-effect sensors and motor drivers. In addition, the company offers mixed-signal products, such as high speed mux/demux, digital switches, interface, redrivers, universal level shifters/voltage translators, clock ICs and packet switches; standard logic products comprising low-voltage complementary metal-oxide-semiconductor (Â“CMOSÂ”) and advanced high-speed CMOS devices; ultra-low power CMOS logic; and analog switches; multichip products and co-packaged discrete, analog and mixed-signal silicon in miniature packages; and silicon and silicon epitaxial wafers used in manufacturing frequency control products and contact images sensors. It serves the industrial, automotive, computing, communications, and consumer markets through direct sales, marketing personnel, independent sales representatives, and distributors. The company was incorporated in 1959 and is headquartered in Plano, Texas.

Table of Diods Inc. Columns represent the percentage % respect to the revenue for each year. Change columns represent the percentage change from one year to the next.
|        | ficat            | scgrpid | sccat                            | <div style="width:50px">fitest</div>               | 2021-2020  | 2022-2021  | 2023-2022  | 12/31/2019 | 12/31/2020 | 12/31/2021 | 12/31/2022 | 12/31/2023 |
|--------|------------------|---------|----------------------------------|-----------------------------------------------------|---------|---------|---------|------------|------------|------------|------------|------------|
| DIOD   | BALANCE SHEET    | 1       | ASSETS                           | cashAndCashEquivalents                              | 36%     | -7%     | -6%     |            | 22%        | 20%        | 17%        | 19%        |
| DIOD   | BALANCE SHEET    | 2       | ASSETS                           | cashCashEquivalentsAndShortTermInvestments          | 35%     | -7%     | -5%     |            | 22%        | 21%        | 17%        | 20%        |
| DIOD   | BALANCE SHEET    | 4       | ASSETS                           | restrictedCash                                      | -94%    | 36%     | -31%    |            | 4%         | 0%         | 0%         | 0%         |
| DIOD   | BALANCE SHEET    | 6       | ASSETS                           | accountsReceivable                                  | 12%     | 3%      | 1%      |            | 26%        | 20%        | 18%        | 22%        |
| DIOD   | BALANCE SHEET    | 7       | ASSETS                           | grossAccountsReceivable                             | 12%     | 3%      | 1%      |            | 26%        | 20%        | 19%        | 23%        |
| DIOD   | BALANCE SHEET    | 8       | ASSETS                           | allowanceForDoubtfulAccountsReceivable              | 14%     | 35%     | -4%     |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | BALANCE SHEET    | 11      | ASSETS                           | prepaidAssets                                       | 53%     | -22%    | 0%      |            | 6%         | 6%         | 4%         |            |
| DIOD   | BALANCE SHEET    | 13      | ASSETS                           | currentAssets                                       | 16%     | -2%     | 2%      |            | 83%        | 66%        | 58%        | 71%        |
| DIOD   | BALANCE SHEET    | 14      | ASSETS                           | receivables                                         | 12%     | 3%      | 1%      |            | 26%        | 20%        | 18%        | 22%        |
| DIOD   | BALANCE SHEET    | 18      | ASSETS                           | inventory                                           | 14%     | 3%      | 8%      |            | 25%        | 19%        | 18%        | 23%        |
| DIOD   | BALANCE SHEET    | 19      | ASSETS                           | finishedGoods                                       | 27%     | -11%    | 34%     |            | 7%         | 6%         | 5%         | 8%         |
| DIOD   | BALANCE SHEET    | 20      | ASSETS                           | rawMaterials                                        | 7%      | 16%     | 2%      |            | 12%        | 9%         | 9%         | 11%        |
| DIOD   | BALANCE SHEET    | 21      | ASSETS                           | otherCurrentAssets                                  | 53%     | -22%    | 16%     |            | 6%         | 6%         | 4%         | 6%         |
| DIOD   | BALANCE SHEET    | 37      | ASSETS                           | nonCurrentDeferredAssets                            | -63%    | 66%     | 46%     |            | 5%         | 1%         | 2%         | 3%         |
| DIOD   | BALANCE SHEET    | 38      | ASSETS                           | nonCurrentDeferredTaxesAssets                       | -63%    | 66%     | 46%     |            | 5%         | 1%         | 2%         | 3%         |
| DIOD   | BALANCE SHEET    | 40      | ASSETS                           | properties                                          |         |         |         |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | BALANCE SHEET    | 41      | ASSETS                           | landAndImprovements                                 | 0%      | 1%      | 9%      |            | 5%         | 4%         | 3%         | 4%         |
| DIOD   | BALANCE SHEET    | 42      | ASSETS                           | machineryFurnitureEquipment                         | 2%      | 18%     | 6%      |            | 77%        | 53%        | 57%        | 72%        |
| DIOD   | BALANCE SHEET    | 43      | ASSETS                           | constructionInProgress                              | 149%    | 8%      | 12%     |            | 4%         | 6%         | 6%         | 8%         |
| DIOD   | BALANCE SHEET    | 44      | ASSETS                           | grossPPE                                            | 7%      | 16%     | 6%      |            | 108%       | 79%        | 82%        | 105%       |
| DIOD   | BALANCE SHEET    | 45      | ASSETS                           | buildingsAndImprovements                            | 3%      | 17%     | 5%      |            | 22%        | 15%        | 16%        | 20%        |
| DIOD   | BALANCE SHEET    | 49      | ASSETS                           | netTangibleAssets                                   | 43%     | 30%     | 19%     |            | 57%        | 55%        | 64%        | 92%        |
| DIOD   | BALANCE SHEET    | 50      | ASSETS                           | accumulatedDepreciation                             | 6%      | 9%      | 10%     |            | -64%       | -46%       | -46%       | -60%       |
| DIOD   | BALANCE SHEET    | 51      | ASSETS                           | netPPE                                              | 10%     | 27%     | 1%      |            | 43%        | 32%        | 37%        | 45%        |
| DIOD   | BALANCE SHEET    | 53      | ASSETS                           | goodwill                                            | -5%     | -3%     | 1%      |            | 13%        | 8%         | 7%         | 9%         |
| DIOD   | BALANCE SHEET    | 54      | ASSETS                           | goodwillAndOtherIntangibleAssets                    | -9%     | -8%     | -6%     |            | 22%        | 14%        | 11%        | 13%        |
| DIOD   | BALANCE SHEET    | 55      | ASSETS                           | otherIntangibleAssets                               | -15%    | -16%    | -19%    |            | 9%         | 5%         | 4%         | 4%         |
| DIOD   | BALANCE SHEET    | 56      | ASSETS                           | otherNonCurrentAssets                               | 62%     | -18%    | 32%     |            | 8%         | 9%         | 7%         | 10%        |
| DIOD   | BALANCE SHEET    | 59      | ASSETS                           | totalAssets                                         | 11%     | 4%      | 3%      |            | 161%       | 122%       | 114%       | 142%       |
| DIOD   | BALANCE SHEET    | 60      | LIABILITIES                      | currentLiabilities                                  | -8%     | -8%     | -9%     |            | 41%        | 26%        | 22%        | 24%        |
| DIOD   | BALANCE SHEET    | 62      | LIABILITIES                      | otherCurrentBorrowings                              | -20%    | -90%    | 161%    |            | 2%         | 1%         | 0%         | 0%         |
| DIOD   | BALANCE SHEET    | 63      | LIABILITIES                      | accountsPayable                                     | 32%     | -27%    | -1%     |            | 14%        | 12%        | 8%         | 10%        |
| DIOD   | BALANCE SHEET    | 64      | LIABILITIES                      | payables                                            | 30%     | -28%    | -6%     |            | 16%        | 14%        | 9%         | 10%        |
| DIOD   | BALANCE SHEET    | 65      | LIABILITIES                      | payablesAndAccruedExpenses                          | 21%     | -13%    | -9%     |            | 23%        | 19%        | 15%        | 17%        |
| DIOD   | BALANCE SHEET    | 66      | LIABILITIES                      | incomeTaxPayable                                    | 55%     | -34%    | -47%    |            | 2%         | 2%         | 1%         | 1%         |
| DIOD   | BALANCE SHEET    | 68      | LIABILITIES                      | currentAccruedExpenses                              | 2%      | 25%     | -13%    |            | 7%         | 5%         | 6%         | 6%         |
| DIOD   | BALANCE SHEET    | 69      | LIABILITIES                      | currentDebt                                         | -78%    | 7%      | 19%     |            | 13%        | 2%         | 2%         | 3%         |
| DIOD   | BALANCE SHEET    | 70      | LIABILITIES                      | currentCapitalLeaseObligation                       | 4%      | -34%    | 20%     |            | 1%         | 1%         | 0%         | 1%         |
| DIOD   | BALANCE SHEET    | 71      | LIABILITIES                      | currentDebtAndCapitalLeaseObligation                | -73%    | -3%     | 19%     |            | 14%        | 3%         | 2%         | 3%         |
| DIOD   | BALANCE SHEET    | 77      | LIABILITIES                      | otherCurrentLiabilities                             | 600%    | -10%    | -96%    |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | BALANCE SHEET    | 78      | LIABILITIES                      | longTermDebt                                        | -8%     | -44%    | -88%    |            | 23%        | 15%        | 7%         | 1%         |
| DIOD   | BALANCE SHEET    | 79      | LIABILITIES                      | longTermCapitalLeaseObligation                      | -18%    | -7%     | 32%     |            | 2%         | 1%         | 1%         | 2%         |
| DIOD   | BALANCE SHEET    | 80      | LIABILITIES                      | longTermDebtAndCapitalLeaseObligation               | -9%     | -42%    | -74%    |            | 26%        | 16%        | 8%         | 3%         |
| DIOD   | BALANCE SHEET    | 84      | LIABILITIES                      | nonCurrentDeferredLiabilities                       | 8%      | -41%    | 6%      |            | 5%         | 4%         | 2%         | 2%         |
| DIOD   | BALANCE SHEET    | 85      | LIABILITIES                      | nonCurrentDeferredTaxesLiabilities                  | -7%     | -60%    | 6%      |            | 3%         | 2%         | 1%         | 1%         |
| DIOD   | BALANCE SHEET    | 88      | LIABILITIES                      | pensionandOtherPostRetirementBenefitPlansCurrent    | 50%     | 13%     | -22%    |            | 4%         | 4%         | 4%         | 4%         |
| DIOD   | BALANCE SHEET    | 90      | LIABILITIES                      | otherNonCurrentLiabilities                          | 70%     | 58%     | 63%     |            | 0%         | 0%         | 1%         | 1%         |
| DIOD   | BALANCE SHEET    | 92      | LIABILITIES                      | capitalLeaseObligations                             | -11%    | -16%    | 28%     |            | 3%         | 2%         | 1%         | 2%         |
| DIOD   | BALANCE SHEET    | 93      | LIABILITIES                      | tradeandOtherPayablesNonCurrent                     | 5%      | 5%      | 6%      |            | 3%         | 2%         | 2%         | 3%         |
| DIOD   | BALANCE SHEET    | 94      | LIABILITIES                      | totalLiabilitiesNetMinorityInterest                 | -7%     | -21%    | -21%    |            | 78%        | 49%        | 35%        | 34%        |
| DIOD   | BALANCE SHEET    | 95      | EQUITY                           | capitalStock                                        | 1%      | 1%      | 1%      |            | 3%         | 2%         | 2%         | 2%         |
| DIOD   | BALANCE SHEET    | 96      | EQUITY                           | commonStock                                         | 1%      | 1%      | 1%      |            | 3%         | 2%         | 2%         | 2%         |
| DIOD   | BALANCE SHEET    | 97      | EQUITY                           | commonStockEquity                                   | 28%     | 22%     | 15%     |            | 78%        | 69%        | 76%        | 105%       |
| DIOD   | BALANCE SHEET    | 98      | EQUITY                           | additionalPaidInCapital                             | 5%      | 5%      | 3%      |            | 37%        | 26%        | 25%        | 31%        |
| DIOD   | BALANCE SHEET    | 100     | EQUITY                           | preferredStock                                      |         |         |         |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | BALANCE SHEET    | 102     | EQUITY                           | retainedEarnings                                    | 26%     | 30%     | 16%     |            | 72%        | 62%        | 72%        | 101%       |
| DIOD   | BALANCE SHEET    | 103     | EQUITY                           | treasurySharesNumber                                | 0%      | 0%      | 0%      |            | 1%         | 1%         | 0%         | 1%         |
| DIOD   | BALANCE SHEET    | 104     | EQUITY                           | treasuryStock                                       | 0%      | 0%      | 0%      |            | 27%        | 19%        | 17%        | 20%        |
| DIOD   | BALANCE SHEET    | 105     | EQUITY                           | otherEquityAdjustments                              | -31%    | 154%    | 12%     |            | -6%        | -3%        | -6%        | -9%        |
| DIOD   | BALANCE SHEET    | 111     | EQUITY                           | ordinarySharesNumber                                | 2%      | 1%      | 1%      |            | 4%         | 2%         | 2%         | 3%         |
| DIOD   | BALANCE SHEET    | 113     | EQUITY                           | minorityInterest                                    | 25%     | 6%      | 0%      |            | 4%         | 4%         | 3%         | 4%         |
| DIOD   | BALANCE SHEET    | 114     | EQUITY                           | totalEquityGrossMinorityInterest                    | 28%     | 22%     | 14%     |            | 83%        | 72%        | 79%        | 109%       |
| DIOD   | BALANCE SHEET    | 115     | EQUITY                           | totalCapitalization                                 | 20%     | 11%     | 6%      |            | 102%       | 83%        | 83%        | 106%       |
| DIOD   | BALANCE SHEET    | 116     | EQUITY                           | stockholdersEquity                                  | 28%     | 22%     | 15%     |            | 78%        | 69%        | 76%        | 105%       |
| DIOD   | BALANCE SHEET    | 117     | EQUITY                           | shareIssued                                         | 1%      | 1%      | 1%      |            | 4%         | 3%         | 3%         | 3%         |
| DIOD   | BALANCE SHEET    | 118     | EQUITY                           | tangibleBookValue                                   | 43%     | 30%     | 19%     |            | 57%        | 55%        | 64%        | 92%        |
| DIOD   | BALANCE SHEET    | 119     | OTHER                            | workingCapital                                      | 39%     | 2%      | 9%      |            | 42%        | 40%        | 36%        | 48%        |
| DIOD   | BALANCE SHEET    | 120     | OTHER                            | netDebt                                             |         |         |         |            | 15%        |            |            |            |
| DIOD   | BALANCE SHEET    | 121     | OTHER                            | totalDebt                                           | -32%    | -36%    | -54%    |            | 40%        | 19%        | 11%        | 6%         |
| DIOD   | BALANCE SHEET    | 122     | OTHER                            | totalNonCurrentAssets                               | 5%      | 12%     | 5%      |            | 78%        | 56%        | 56%        | 71%        |
| DIOD   | BALANCE SHEET    | 123     | OTHER                            | totalNonCurrentLiabilitiesNetMinorityInterest       | -7%     | -35%    | -40%    |            | 37%        | 23%        | 14%        | 10%        |
| DIOD   | BALANCE SHEET    | 124     | OTHER                            | totalTaxPayable                                     | 18%     | -29%    | -40%    |            | 2%         | 2%         | 1%         | 1%         |
| DIOD   | BALANCE SHEET    | 126     | OTHER                            | lineOfCredit                                        | -87%    | 101%    | 12%     |            | 11%        | 1%         | 2%         | 2%         |
| DIOD   | BALANCE SHEET    | 128     | OTHER                            | employeeBenefits                                    | -44%    | -38%    | 21%     |            | 3%         | 1%         | 1%         | 1%         |
| DIOD   | BALANCE SHEET    | 130     | OTHER                            | gainsLossesNotAffectingRetainedEarnings             | -31%    | 154%    | 12%     |            | -6%        | -3%        | -6%        | -9%        |
| DIOD   | BALANCE SHEET    | 135     | OTHER                            | workInProcess                                       | 11%     | -1%     | -10%    |            | 6%         | 5%         | 4%         | 4%         |
| DIOD   | BALANCE SHEET    | 139     | OTHER                            | otherShortTermInvestments                           | 7%      | 8%      | 44%     |            | 0%         | 0%         | 0%         | 1%         |
| DIOD   | BALANCE SHEET    | 142     | OTHER                            | investedCapital                                     | 9%      | 10%     | 6%      |            | 115%       | 85%        | 85%        | 108%       |
| DIOD   | CASH FLOWS       | 1       | OPERATING ACTIVITIES             | amortizationCashFlow                                | 0%      | -4%     | -2%     |            | 1%         | 1%         | 1%         | 1%         |
| DIOD   | CASH FLOWS       | 2       | OPERATING ACTIVITIES             | amortizationOfIntangibles                           | 0%      | -4%     | -2%     |            | 1%         | 1%         | 1%         | 1%         |
| DIOD   | CASH FLOWS       | 5       | OPERATING ACTIVITIES             | cashFlowFromContinuingOperatingActivities           | 81%     | 16%     | -28%    |            | 15%        | 19%        | 20%        | 17%        |
| DIOD   | CASH FLOWS       | 8       | OPERATING ACTIVITIES             | changeInAccountPayable                              | 650%    | -190%   | -96%    |            | 1%         | 3%         | -3%        | 0%         |
| DIOD   | CASH FLOWS       | 9       | OPERATING ACTIVITIES             | changeInAccruedExpense                              | -419%   | 8%      | -156%   |            | -1%        | 2%         | 2%         | -1%        |
| DIOD   | CASH FLOWS       | 11      | OPERATING ACTIVITIES             | changeInIncomeTaxPayable                            | -57%    | 473%    | 12%     |            | 0%         | 0%         | 0%         | -1%        |
| DIOD   | CASH FLOWS       | 13      | OPERATING ACTIVITIES             | changeInInventory                                   | 844%    | -31%    | -2%     |            | 0%         | -2%        | -1%        | -2%        |
| DIOD   | CASH FLOWS       | 14      | OPERATING ACTIVITIES             | changeInOtherCurrentAssets                          | 0%      | -107%   | -1073%  |            |            | -1%        | 0%         | -1%        |
| DIOD   | CASH FLOWS       | 15      | OPERATING ACTIVITIES             | changeInOtherCurrentLiabilities                     | -31%    | 330%    | -118%   |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | CASH FLOWS       | 16      | OPERATING ACTIVITIES             | changeInOtherWorkingCapital                         |         |         |         |            | 0%         |            |            |            |
| DIOD   | CASH FLOWS       | 17      | OPERATING ACTIVITIES             | changeInPayable                                     | 1233%   | -208%   | -80%    |            | 0%         | 3%         | -3%        | -1%        |
| DIOD   | CASH FLOWS       | 18      | OPERATING ACTIVITIES             | changeInPayablesAndAccruedExpense                   | -1727%  | -132%   | 10%     |            | 0%         | 5%         | -1%        | -2%        |
| DIOD   | CASH FLOWS       | 19      | OPERATING ACTIVITIES             | changeInPrepaidAssets                               | 181%    | 0%      | 0%      |            | -1%        | -1%        |            |            |
| DIOD   | CASH FLOWS       | 20      | OPERATING ACTIVITIES             | changeInReceivables                                 | 402%    | -62%    | -87%    |            | -1%        | -3%        | -1%        | 0%         |
| DIOD   | CASH FLOWS       | 21      | OPERATING ACTIVITIES             | changeInTaxPayable                                  | -57%    | 473%    | 12%     |            | 0%         | 0%         | 0%         | -1%        |
| DIOD   | CASH FLOWS       | 22      | OPERATING ACTIVITIES             | changeInWorkingCapital                              | 25%     | 107%    | -4%     |            | -3%        | -2%        | -4%        | -5%        |
| DIOD   | CASH FLOWS       | 23      | OPERATING ACTIVITIES             | changesInAccountReceivables                         | 402%    | -62%    | -87%    |            | -1%        | -3%        | -1%        | 0%         |
| DIOD   | CASH FLOWS       | 27      | OPERATING ACTIVITIES             | deferredIncomeTax                                   | -248%   | -283%   | -66%    |            | -1%        | 1%         | -2%        | -1%        |
| DIOD   | CASH FLOWS       | 28      | OPERATING ACTIVITIES             | deferredTax                                         | -248%   | -283%   | -66%    |            | -1%        | 1%         | -2%        | -1%        |
| DIOD   | CASH FLOWS       | 30      | OPERATING ACTIVITIES             | depreciation                                        | 16%     | 6%      | 9%      |            | 7%         | 6%         | 6%         | 7%         |
| DIOD   | CASH FLOWS       | 31      | OPERATING ACTIVITIES             | depreciationAmortizationDepletion                   | 13%     | 4%      | 7%      |            | 9%         | 7%         | 6%         | 8%         |
| DIOD   | CASH FLOWS       | 32      | OPERATING ACTIVITIES             | depreciationAndAmortization                         | 13%     | 4%      | 7%      |            | 9%         | 7%         | 6%         | 8%         |
| DIOD   | CASH FLOWS       | 35      | OPERATING ACTIVITIES             | interestPaidSupplementalData                        | -32%    | 6%      | -37%    |            | 1%         | 0%         | 0%         | 0%         |
| DIOD   | CASH FLOWS       | 40      | OPERATING ACTIVITIES             | changesInCash                                       | 37%     | -96%    | -1551%  |            | 2%         | 2%         | 0%         | -1%        |
| DIOD   | CASH FLOWS       | 48      | OPERATING ACTIVITIES             | effectOfExchangeRateChanges                         | -70%    | -362%   | -98%    |            | 3%         | 1%         | -1%        | 0%         |
| DIOD   | CASH FLOWS       | 51      | OPERATING ACTIVITIES             | stockBasedCompensation                              | 31%     | 9%      | -15%    |            | 2%         | 2%         | 2%         | 2%         |
| DIOD   | CASH FLOWS       | 54      | OPERATING ACTIVITIES             | incomeTaxPaidSupplementalData                       | 17%     | 58%     | 10%     |            | 4%         | 3%         | 4%         | 6%         |
| DIOD   | CASH FLOWS       | 57      | OPERATING ACTIVITIES             | otherNonCashItems                                   | -12%    | -254%   | 83%     |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | CASH FLOWS       | 59      | OPERATING ACTIVITIES             | operatingCashFlow                                   | 81%     | 16%     | -28%    |            | 15%        | 19%        | 20%        | 17%        |
| DIOD   | CASH FLOWS       | 60      | OPERATING ACTIVITIES             | netIncome                                           | 133%    | 45%     | -31%    |            | 8%         | 13%        | 17%        | 14%        |
| DIOD   | CASH FLOWS       | 61      | NET INCOME                       | netIncome                                           | 133%    | 45%     | -31%    |            | 8%         | 13%        | 17%        | 14%        |
| DIOD   | CASH FLOWS       | 61      | OPERATING ACTIVITIES             | netIncomeFromContinuingOperations                   | 138%    | 44%     | -32%    |            | 8%         | 13%        | 17%        | 14%        |
| DIOD   | CASH FLOWS       | 62      | OPERATING ACTIVITIES             | operatingGainsLosses                                | 2186%   | -133%   | -270%   |            | 0%         | -2%        | 1%         | -1%        |
| DIOD   | CASH FLOWS       | 64      | INVESTING ACTIVITIES             | gainLossOnInvestmentSecurities                      | 2046%   | 0%      | 0%      |            | 0%         | -2%        |            |            |
| DIOD   | CASH FLOWS       | 66      | INVESTING ACTIVITIES             | gainLossOnSaleOfPPE                                 | 104%    | -1592%  | -44%    |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | CASH FLOWS       | 68      | INVESTING ACTIVITIES             | cashFlowFromContinuingInvestingActivities           | 35%     | 84%     | -40%    |            | -9%        | -8%        | -13%       | -10%       |
| DIOD   | CASH FLOWS       | 70      | INVESTING ACTIVITIES             | netInvestmentPurchaseAndSale                        | 109%    | -126%   | -615%   |            | -1%        | -1%        | 0%         | -1%        |
| DIOD   | CASH FLOWS       | 72      | INVESTING ACTIVITIES             | netPPEPurchaseAndSale                               | 83%     | 53%     | -30%    |            | -6%        | -8%        | -11%       | -9%        |
| DIOD   | CASH FLOWS       | 74      | INVESTING ACTIVITIES             | purchaseOfInvestment                                | 29%     | -41%    | 103%    |            | -1%        | -1%        | -1%        | -2%        |
| DIOD   | CASH FLOWS       | 76      | INVESTING ACTIVITIES             | purchaseOfPPE                                       | 86%     | 50%     | -29%    |            | -6%        | -8%        | -11%       | -9%        |
| DIOD   | CASH FLOWS       | 78      | INVESTING ACTIVITIES             | purchaseOfBusiness                                  | -99%    | 53390%  | -100%   |            | -2%        | 0%         | -4%        | 0%         |
| DIOD   | CASH FLOWS       | 79      | INVESTING ACTIVITIES             | saleOfInvestment                                    | -29%    | 138%    | -63%    |            | 1%         | 0%         | 1%         | 0%         |
| DIOD   | CASH FLOWS       | 81      | INVESTING ACTIVITIES             | saleOfPPE                                           | 1282%   | -87%    | 562%    |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | CASH FLOWS       | 83      | INVESTING ACTIVITIES             | saleOfBusiness                                      | 0%      | 94%     | -67%    |            |            | 1%         | 1%         | 0%         |
| DIOD   | CASH FLOWS       | 84      | INVESTING ACTIVITIES             | investingCashFlow                                   | 35%     | 84%     | -40%    |            | -9%        | -8%        | -13%       | -10%       |
| DIOD   | CASH FLOWS       | 85      | INVESTING ACTIVITIES             | capitalExpenditure                                  | 86%     | 50%     | -29%    |            | -6%        | -8%        | -11%       | -9%        |
| DIOD   | CASH FLOWS       | 88      | INVESTING ACTIVITIES             | netBusinessPurchaseAndSale                          | -140%   | -762%   | -110%   |            | -2%        | 1%         | -3%        | 0%         |
| DIOD   | CASH FLOWS       | 92      | INVESTING ACTIVITIES             | netOtherInvestingChanges                            | -191%   | -1094%  | -39%    |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | CASH FLOWS       | 95      | FINANCING ACTIVITIES             | cashFlowFromContinuingFinancingActivities           | 192%    | -21%    | 15%     |            | -4%        | -9%        | -6%        | -9%        |
| DIOD   | CASH FLOWS       | 97      | FINANCING ACTIVITIES             | issuanceOfCapitalStock                              | -37%    | -97%    | 0%      |            | 1%         | 0%         | 0%         | 0%         |
| DIOD   | CASH FLOWS       | 98      | FINANCING ACTIVITIES             | issuanceOfDebt                                      | -44%    | -16%    | -89%    |            | 84%        | 32%        | 24%        | 3%         |
| DIOD   | CASH FLOWS       | 101     | FINANCING ACTIVITIES             | repurchaseOfCapitalStock                            |         |         |         |            | -24%       | 0%         | 0%         |            |
| DIOD   | CASH FLOWS       | 102     | FINANCING ACTIVITIES             | repaymentOfDebt                                     | -7%     | -18%    | -70%    |            | -64%       | -41%       | -30%       | -11%       |
| DIOD   | CASH FLOWS       | 107     | FINANCING ACTIVITIES             | financingCashFlow                                   | 192%    | -21%    | 15%     |            | -4%        | -9%        | -6%        | -9%        |
| DIOD   | CASH FLOWS       | 110     | FINANCING ACTIVITIES             | netShortTermDebtIssuance                            | -437%   | -117%   | -78%    |            | 3%         | -7%        | 1%         | 0%         |
| DIOD   | CASH FLOWS       | 111     | FINANCING ACTIVITIES             | netIssuancePaymentsOfDebt                           | -162%   | -27%    | 11%     |            | 20%        | -8%        | -6%        | -7%        |
| DIOD   | CASH FLOWS       | 112     | FINANCING ACTIVITIES             | netLongTermDebtIssuance                             | -113%   | 368%    | -3%     |            | 17%        | -2%        | -7%        | -8%        |
| DIOD   | CASH FLOWS       | 113     | FINANCING ACTIVITIES             | longTermDebtIssuance                                | -42%    | -33%    | -93%    |            | 78%        | 31%        | 19%        | 2%         |
| DIOD   | CASH FLOWS       | 115     | FINANCING ACTIVITIES             | longTermDebtPayments                                | -21%    | -14%    | -70%    |            | -61%       | -32%       | -25%       | -9%        |
| DIOD   | CASH FLOWS       | 117     | FINANCING ACTIVITIES             | netCommonStockIssuance                              | -101%   | -97%    | 0%      |            | -24%       | 0%         | 0%         | 0%         |
| DIOD   | CASH FLOWS       | 118     | FINANCING ACTIVITIES             | freeCashFlow                                        | 77%     | -8%     | -28%    |            | 9%         | 11%        | 9%         | 8%         |
| DIOD   | CASH FLOWS       | 119     | FINANCING ACTIVITIES             | netOtherFinancingCharges                            | -22%    | 38%     | 50%     |            | -1%        | -1%        | -1%        | -1%        |
| DIOD   | CASH FLOWS       | 122     | FINANCING ACTIVITIES             | commonStockIssuance                                 | -37%    | -97%    | 0%      |            | 1%         | 0%         | 0%         | 0%         |
| DIOD   | CASH FLOWS       | 123     | FINANCING ACTIVITIES             | commonStockPayments                                 |         |         |         |            | -24%       | 0%         | 0%         |            |
| DIOD   | CASH FLOWS       | 125     | FINANCING ACTIVITIES             | shortTermDebtIssuance                               | -72%    | 423%    | -75%    |            | 6%         | 1%         | 6%         | 2%         |
| DIOD   | CASH FLOWS       | 126     | FINANCING ACTIVITIES             | shortTermDebtPayments                               | 261%    | -36%    | -74%    |            | -3%        | -8%        | -5%        | -1%        |
| DIOD   | CASH FLOWS       | 127     | SUPPLEMENTAL DISCLOSURES         | changeInCashSupplementalAsReported                  | -24%    | -156%   | -12%    |            | 5%         | 3%         | -1%        | -1%        |
| DIOD   | CASH FLOWS       | 128     | STARTING ENDING BALANCES         | beginningCashPosition                               | 24%     | 14%     | -7%     |            | 21%        | 18%        | 18%        | 21%        |
| DIOD   | CASH FLOWS       | 129     | STARTING ENDING BALANCES         | endCashPosition                                     | 14%     | -7%     | -7%     |            | 26%        | 20%        | 17%        | 19%        |
| DIOD   | INCOME STATEMENT | 1       | REVENUE                          | totalRevenue                                        | 47%     | 11%     | -17%    |            | 100%       | 100%       | 100%       | 100%       |
| DIOD   | INCOME STATEMENT | 2       | REVENUE                          | operatingRevenue                                    | 47%     | 11%     | -17%    |            | 100%       | 100%       | 100%       | 100%       |
| DIOD   | INCOME STATEMENT | 3       | REVENUE                          | grossProfit                                         | 55%     | 23%     | -20%    |            | 35%        | 37%        | 41%        | 40%        |
| DIOD   | INCOME STATEMENT | 4       | COST OF REVENUE                  | costOfRevenue                                       | 42%     | 3%      | -14%    |            | 65%        | 63%        | 59%        | 60%        |
| DIOD   | INCOME STATEMENT | 5       | COST OF REVENUE                  | reconciledCostOfRevenue                             | 46%     | 3%      | -17%    |            | 57%        | 57%        | 53%        | 53%        |
| DIOD   | INCOME STATEMENT | 9       | COST OF REVENUE                  | depreciationAmortizationDepletionIncomeStatement    | 0%      | -4%     | -2%     |            | 1%         | 1%         | 1%         | 1%         |
| DIOD   | INCOME STATEMENT | 10      | COST OF REVENUE                  | depreciationAndAmortizationInIncomeStatement        | 0%      | -4%     | -2%     |            | 1%         | 1%         | 1%         | 1%         |
| DIOD   | INCOME STATEMENT | 11      | OPERATING EXPENSES               | operatingExpense                                    | 33%     | 7%      | -3%     |            | 24%        | 22%        | 21%        | 25%        |
| DIOD   | INCOME STATEMENT | 12      | OPERATING EXPENSES               | researchAndDevelopment                              | 26%     | 6%      | 7%      |            | 8%         | 7%         | 6%         | 8%         |
| DIOD   | INCOME STATEMENT | 14      | OPERATING EXPENSES               | sellingGeneralAndAdministration                     | 39%     | 9%      | -8%     |            | 15%        | 14%        | 14%        | 16%        |
| DIOD   | INCOME STATEMENT | 17      | OPERATING EXPENSES               | otherOperatingExpenses                              | -6%     | -111%   | -85%    |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | INCOME STATEMENT | 23      | OPERATING EXPENSES               | totalExpenses                                       | 40%     | 4%      | -12%    |            | 89%        | 85%        | 80%        | 85%        |
| DIOD   | INCOME STATEMENT | 24      | SPECIAL OPERATING ITEMS          | restructuringAndMergernAcquisition                  | 0%      | 0%      | 0%      |            |            | 0%         | 0%         | 0%         |
| DIOD   | INCOME STATEMENT | 25      | SPECIAL OPERATING ITEMS          | impairmentOfCapitalAssets                           |         |         |         |            |            |            |            |            |
| DIOD   | INCOME STATEMENT | 27      | OPERATING INCOME                 | operatingIncome                                     | 105%    | 46%     | -38%    |            | 11%        | 15%        | 20%        | 15%        |
| DIOD   | INCOME STATEMENT | 28      | OPERATING INCOME                 | ebit                                                | 144%    | 25%     | -30%    |            | 11%        | 18%        | 20%        | 17%        |
| DIOD   | INCOME STATEMENT | 29      | OPERATING INCOME                 | normalizedEBITDA                                    | 69%     | 29%     | -25%    |            | 20%        | 23%        | 27%        | 25%        |
| DIOD   | INCOME STATEMENT | 30      | OPERATING INCOME                 | eBITDA                                              | 85%     | 20%     | -21%    |            | 20%        | 25%        | 27%        | 25%        |
| DIOD   | INCOME STATEMENT | 31      | OPERATING INCOME                 | totalOperatingIncomeAsReported                      | 105%    | 48%     | -39%    |            | 11%        | 15%        | 20%        | 15%        |
| DIOD   | INCOME STATEMENT | 32      | OTHER INCOME OR EXPENSE          | otherIncomeExpense                                  | -1334%  | -109%   | -611%   |            | 0%         | 2%         | 0%         | 1%         |
| DIOD   | INCOME STATEMENT | 33      | OTHER INCOME OR EXPENSE          | otherNonOperatingIncomeExpenses                     | 305%    | -61%    | -1%     |            | 0%         | 1%         | 0%         | 0%         |
| DIOD   | INCOME STATEMENT | 36      | OTHER INCOME OR EXPENSE          | gainOnSaleOfPPE                                     | 132%    | -1584%  | -44%    |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | INCOME STATEMENT | 38      | OTHER INCOME OR EXPENSE          | gainOnSaleOfSecurity                                | -435%   | -156%   | -190%   |            | -1%        | 1%         | -1%        | 1%         |
| DIOD   | INCOME STATEMENT | 39      | INTEREST INCOME OR EXPENSE       | interestIncome                                      | 194%    | 17%     | 263%    |            | 0%         | 0%         | 0%         | 1%         |
| DIOD   | INCOME STATEMENT | 40      | INTEREST INCOME OR EXPENSE       | interestIncomeNonOperating                          | 194%    | 17%     | 263%    |            | 0%         | 0%         | 0%         | 1%         |
| DIOD   | INCOME STATEMENT | 41      | INTEREST INCOME OR EXPENSE       | interestExpense                                     | -36%    | 11%     | -31%    |            | 1%         | 0%         | 0%         | 0%         |
| DIOD   | INCOME STATEMENT | 42      | INTEREST INCOME OR EXPENSE       | interestExpenseNonOperating                         | -36%    | 11%     | -31%    |            | 1%         | 0%         | 0%         | 0%         |
| DIOD   | INCOME STATEMENT | 43      | INTEREST INCOME OR EXPENSE       | netInterestIncome                                   | -59%    | 7%      | -264%   |            | -1%        | 0%         | 0%         | 0%         |
| DIOD   | INCOME STATEMENT | 44      | INTEREST INCOME OR EXPENSE       | netNonOperatingInterestIncomeExpense                | -59%    | 7%      | -264%   |            | -1%        | 0%         | 0%         | 0%         |
| DIOD   | INCOME STATEMENT | 45      | PRETAX INCOME                    | pretaxIncome                                        | 162%    | 26%     | -30%    |            | 10%        | 17%        | 20%        | 17%        |
| DIOD   | INCOME STATEMENT | 46      | TAX PROVISION                    | taxProvision                                        | 273%    | -28%    | -17%    |            | 2%         | 4%         | 3%         | 3%         |
| DIOD   | INCOME STATEMENT | 47      | TAX PROVISION                    | taxRateForCalcs                                     | 43%     | -43%    | 19%     |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | INCOME STATEMENT | 48      | TAX PROVISION                    | taxEffectOfUnusualItems                             | -568%   | -124%   | -249%   |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | INCOME STATEMENT | 50      | AMORTIZATION                     | amortization                                        | 0%      | -4%     | -2%     |            | 1%         | 1%         | 1%         | 1%         |
| DIOD   | INCOME STATEMENT | 51      | AMORTIZATION                     | amortizationOfIntangiblesIncomeStatement            | 0%      | -4%     | -2%     |            | 1%         | 1%         | 1%         | 1%         |
| DIOD   | INCOME STATEMENT | 54      | NET INCOME                       | netIncomeFromContinuingOperationNetMinorityInterest | 133%    | 45%     | -31%    |            | 8%         | 13%        | 17%        | 14%        |
| DIOD   | INCOME STATEMENT | 55      | NET INCOME                       | netIncomeFromContinuingAndDiscontinuedOperation     | 133%    | 45%     | -31%    |            | 8%         | 13%        | 17%        | 14%        |
| DIOD   | INCOME STATEMENT | 56      | NET INCOME                       | netIncomeContinuousOperations                       | 138%    | 44%     | -32%    |            | 8%         | 13%        | 17%        | 14%        |
| DIOD   | INCOME STATEMENT | 59      | NET INCOME                       | netIncomeIncludingNoncontrollingInterests           | 138%    | 44%     | -32%    |            | 8%         | 13%        | 17%        | 14%        |
| DIOD   | INCOME STATEMENT | 60      | OPERATING ACTIVITIES             | netIncome                                           | 133%    | 45%     | -31%    |            | 8%         | 13%        | 17%        | 14%        |
| DIOD   | INCOME STATEMENT | 61      | NET INCOME                       | netIncome                                           | 133%    | 45%     | -31%    |            | 8%         | 13%        | 17%        | 14%        |
| DIOD   | INCOME STATEMENT | 62      | NET INCOME                       | netIncomeCommonStockholders                         | 133%    | 45%     | -31%    |            | 8%         | 13%        | 17%        | 14%        |
| DIOD   | INCOME STATEMENT | 63      | NET INCOME                       | normalizedIncome                                    | 100%    | 63%     | -37%    |            | 9%         | 12%        | 17%        | 13%        |
| DIOD   | INCOME STATEMENT | 64      | NET INCOME                       | dilutedNIAvailtoComStockholders                     | 133%    | 45%     | -31%    |            | 8%         | 13%        | 17%        | 14%        |
| DIOD   | INCOME STATEMENT | 65      | EPS                              | basicEPS                                            | 166%    | 43%     | -32%    |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | INCOME STATEMENT | 66      | EPS                              | dilutedEPS                                          | 166%    | 44%     | -32%    |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | INCOME STATEMENT | 67      | EPS                              | basicAverageShares                                  | -12%    | 1%      | 1%      |            | 4%         | 2%         | 2%         | 3%         |
| DIOD   | INCOME STATEMENT | 68      | EPS                              | dilutedAverageShares                                | -12%    | 1%      | 1%      |            | 4%         | 3%         | 2%         | 3%         |
| DIOD   | INCOME STATEMENT | 71      | DIVIDENDS AND MINORITY INTERESTS | minorityInterests                                   | 560%    | 6%      | -57%    |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | INCOME STATEMENT | 73      | SPECIAL INCOME OR CHARGES        | specialIncomeCharges                                | 132%    | -1584%  | -87%    |            | 0%         | 0%         | 0%         | 0%         |
| DIOD   | INCOME STATEMENT | 74      | SPECIAL INCOME OR CHARGES        | totalUnusualItems                                   | -427%   | -142%   | -225%   |            | -1%        | 1%         | -1%        | 1%         |
| DIOD   | INCOME STATEMENT | 75      | SPECIAL INCOME OR CHARGES        | totalUnusualItemsExcludingGoodwill                  | -427%   | -142%   | -225%   |            | -1%        | 1%         | -1%        | 1%         |
| DIOD   | INCOME STATEMENT | 76      | OTHER ITEMS                      | reconciledDepreciation                              | 13%     | 4%      | 7%      |            | 9%         | 7%         | 6%         | 8%         |

The idea is thus to use this and selected companies to define what is a healthy company. About 20 companies where selected: DIOD EVRI FWRD GRBK HCKT HDSN IDCC JBI KAI MATX MCRI METCB MHO MTH NRC SHLS TH UHG XPEL.

At the end the following companies were chosen 'TH','MATX', 'HDSN','MCRI','IDCC','SHLS','MTH','KAI','FWRD' and 'XPEL'. The approach to chosing these companies was by means of stability in their earnings, retained earnings, low debt, positive operating earnings and operating cashflow. The following table show the type of comparative tables that were calculated. all the values have beeing divided by its corresponding revenue for each company. This type of analysis is more interesting when considering two companies from the same industry. The following are for instance two building companies MTH and UHG. The 'fistres' columns refer to the percentagers respect to the revenue for that year for that company. 'chgn' represents the change from year to year, since we consider only 4 years, only 3 year changes are calculated. None of these two companies were chosen and they serve here as an example.
| subjid_x | ficat            | sctestcd                                                   | 2020_x  | 2021_x  | 2022_x  | 2023_x  | 2021_x | 2022_x | 2023_x | subjid_y | 2020_y  | 2021_y  | 2022_y  | 2023_y  | 2021_y | 2022_y | 2023_y |
|----------|------------------|------------------------------------------------------------|---------|---------|---------|---------|--------|--------|--------|----------|---------|---------|---------|---------|--------|--------|--------|
|          |                  |                                                            | fistres | fistres | fistres | fistres | chgn   | chgn   | chgn   |          | fistres | fistres | fistres | fistres | chgn   | chgn   | chgn   |
| MTH      | BALANCE SHEET    | cash And Cash Equivalents                                  | 17      | 12      | 14      | 15      | -4.53  | 1.67   | 1.33   | UHG      | 9       | 12      | 3       | 13      | 2.98   | -9.33  | 10.88  |
| MTH      | BALANCE SHEET    | cash Cash Equivalents And Short Term Investments           | 17      | 12      | 14      | 15      | -4.53  | 1.67   | 1.33   | UHG      | 9       | 12      | 3       | 13      | 2.98   | -9.33  | 10.88  |
| MTH      | BALANCE SHEET    | prepaid Assets                                             | 1       | 2       | 1       | 2       | 0.44   | -0.54  | 0.6    | UHG      | 1       | 1       | 1       | 8       | -0.35  | 0.12   | 7.04   |
| MTH      | BALANCE SHEET    | current Assets                                             | 82      | 89      | 88      | 98      | 7.49   | -1.68  | 10.59  | UHG      | 39      | 45      | 42      | 66      | 5.96   | -3.55  | 23.93  |
| MTH      | BALANCE SHEET    | receivables                                                | 2       | 3       | 3       | 4       | 0.68   | 0.55   | 0.94   | UHG      | 0       | 0       | 1       | 1       | 0.2    | 0.23   | -0.16  |
| MTH      | BALANCE SHEET    | inventory                                                  | 62      | 73      | 69      | 77      | 10.9   | -3.35  | 7.72   | UHG      | 29      | 32      | 38      | 43      | 3.12   | 5.43   | 5.6    |
| MTH      | BALANCE SHEET    | finished Goods                                             | 62      | 73      | 69      | 77      | 10.9   | -3.35  | 7.72   | UHG      | 29      | 32      | 38      | 43      | 3.12   | 5.43   | 5.6    |
| MTH      | BALANCE SHEET    | investments And Advances                                   | 0       | 0       | 0       | 0       | 0.02   | 0.07   | 0.09   | UHG      |         | 0       | 0       | 0       |        | 0.04   | 0.3    |
| MTH      | BALANCE SHEET    | investment Properties                                      | 0       | 0       | 0       |         | 0.16   | -0.16  |        |          |         |         |         |         |        |        |        |
| MTH      | BALANCE SHEET    | long Term Equity Investment                                | 0       | 0       | 0       | 0       | 0.02   | 0.07   | 0.09   | UHG      |         | 0       | 0       | 0       |        | 0.04   | 0.3    |
| MTH      | BALANCE SHEET    | non Current Deferred Assets                                | 1       | 1       | 1       | 1       | -0.01  | -0.07  | 0.05   |          |         |         |         |         |        |        |        |
| MTH      | BALANCE SHEET    | non Current Deferred Taxes Assets                          | 1       | 1       | 1       | 1       | -0.01  | -0.07  | 0.05   |          |         |         |         |         |        |        |        |
| MTH      | BALANCE SHEET    | non Current Prepaid Assets                                 | 2       | 2       |         |         | 0.13   |        |        |          |         |         |         |         |        |        |        |
| MTH      | BALANCE SHEET    | machinery Furniture Equipment                              | 3       | 2       | 2       | 2       | -0.61  | -0.45  | 0.04   | UHG      | 0       | 1       | 1       | 0       | 0.09   | -0.03  | -0.26  |
| MTH      | BALANCE SHEET    | gross PPE                                                  | 3       | 2       | 2       | 2       | -0.61  | -0.45  | 0.04   | UHG      | 1       | 1       | 1       | 2       | 0.07   | 0.18   | 0.81   |
| MTH      | BALANCE SHEET    | net Tangible Assets                                        | 52      | 59      | 63      | 75      | 7.04   | 3.57   | 12.43  | UHG      |         | 15      | 12      | -9      |        | -3.01  | -21.12 |
| MTH      | BALANCE SHEET    | accumulated Depreciation                                   | -2      | -2      | -1      | -1      | 0.47   | 0.34   | 0.14   | UHG      | 0       | 0       | 0       | 0       | -0.07  | -0.04  | 0.23   |
| MTH      | BALANCE SHEET    | net PPE                                                    | 1       | 1       | 1       | 1       | -0.14  | -0.11  | 0.18   | UHG      | 0       | 0       | 1       | 2       | -0.01  | 0.13   | 1.04   |
| MTH      | BALANCE SHEET    | other Non Current Assets                                   |         | 2       | 3       | 4       |        | 0.19   | 0.95   | UHG      | 0       | 1       | 1       | 2       | 0.56   | 0.33   | 0.56   |
| MTH      | BALANCE SHEET    | total Assets                                               | 86      | 93      | 92      | 104     | 7.64   | -1.75  | 11.86  | UHG      | 40      | 47      | 44      | 71      | 6.51   | -3.05  | 27.18  |
| MTH      | BALANCE SHEET    | current Liabilities                                        | 10      | 11      | 10      | 10      | 0.7    | -0.82  | 0.71   | UHG      | 30      | 31      | 31      | 30      | 1.57   | -0.25  | -1.35  |
| MTH      | BALANCE SHEET    | accounts Payable                                           | 4       | 4       | 4       | 4       | 0.31   | 0.14   | 0.09   | UHG      | 6       | 7       | 5       | 9       | 0.89   | -2.01  | 4.55   |
| MTH      | BALANCE SHEET    | payables                                                   | 5       | 5       | 5       | 5       | 0.27   | -0.18  | 0.1    | UHG      | 6       | 7       | 5       | 9       | 0.89   | -2.01  | 4.82   |
| MTH      | BALANCE SHEET    | payables And Accrued Expenses                              | 9       | 10      | 9       | 10      | 0.42   | -0.59  | 0.72   | UHG      | 7       | 8       | 6       | 11      | 0.76   | -1.9   | 5.65   |
| MTH      | BALANCE SHEET    | interest Payable                                           | 0       | 0       | 0       | 0       | -0.08  | 0      | -0.01  |          |         |         |         |         |        |        |        |
| MTH      | BALANCE SHEET    | current Accrued Expenses                                   | 5       | 5       | 4       | 5       | 0.15   | -0.41  | 0.62   | UHG      | 1       | 1       | 1       | 2       | -0.14  | 0.12   | 0.84   |
| MTH      | BALANCE SHEET    | current Capital Lease Obligation                           | 1       |         |         |         |        |        |        |          |         |         |         |         |        |        |        |
| MTH      | BALANCE SHEET    | current Debt And Capital Lease Obligation                  | 1       |         |         |         |        |        |        | UHG      | 23      | 24      | 25      | 18      | 0.82   | 1.64   | -7.01  |
| MTH      | BALANCE SHEET    | current Provisions                                         | 1       |         |         |         |        |        |        |          |         |         |         |         |        |        |        |
| MTH      | BALANCE SHEET    | current Deferred Liabilities                               | 1       | 1       | 1       | 1       | 0.27   | -0.23  | -0.01  |          |         |         |         |         |        |        |        |
| MTH      | BALANCE SHEET    | current Deferred Revenue                                   | 1       | 1       | 1       | 1       | 0.27   | -0.23  | -0.01  |          |         |         |         |         |        |        |        |
| MTH      | BALANCE SHEET    | long Term Debt                                             | 23      | 23      | 18      | 16      | -0.1   | -4.27  | -1.84  | UHG      |         |         |         | 17      |        |        |        |
| MTH      | BALANCE SHEET    | long Term Capital Lease Obligation                         | 1       | 1       | 0       | 1       | -0.12  | -0.15  | 0.52   | UHG      |         | 0       | 0       | 1       |        | 0.21   | 1.11   |
| MTH      | BALANCE SHEET    | long Term Debt And Capital Lease Obligation                | 23      | 23      | 19      | 17      | -0.22  | -4.41  | -1.32  | UHG      |         | 0       | 0       | 18      |        | 0.21   | 18.03  |
| MTH      | BALANCE SHEET    | long Term Provisions                                       | 1       | 1       | 1       | 1       | -0.02  | 0.05   | 0.04   |          |         |         |         |         |        |        |        |
| MTH      | BALANCE SHEET    | non Current Deferred Liabilities                           | 1       |         |         |         |        |        |        |          |         |         |         |         |        |        |        |
| MTH      | BALANCE SHEET    | non Current Deferred Revenue                               | 1       |         |         |         |        |        |        |          |         |         |         |         |        |        |        |
| MTH      | BALANCE SHEET    | other Non Current Liabilities                              |         | 0       |         |         |        |        |        |          |         |         |         |         |        |        |        |
| MTH      | BALANCE SHEET    | capital Lease Obligations                                  | 1       | 1       | 0       | 1       | -0.12  | -0.15  | 0.52   | UHG      |         | 0       | 0       | 1       |        | 0.21   | 1.11   |
| MTH      | BALANCE SHEET    | total Liabilities Net Minority Interest                    | 34      | 34      | 29      | 28      | 0.6    | -5.32  | -0.57  | UHG      | 30      | 31      | 31      | 78      | 1.57   | -0.04  | 46.95  |
| MTH      | BALANCE SHEET    | capital Stock                                              | 0       | 0       | 0       | 0       | 0      | 0      | 0      | UHG      |         | 19      | 0       | 0       |        | -19.31 | 0      |
| MTH      | BALANCE SHEET    | common Stock                                               | 0       | 0       | 0       | 0       | 0      | 0      | 0      | UHG      |         | 19      | 0       | 0       |        | -19.31 | 0      |
| MTH      | BALANCE SHEET    | common Stock Equity                                        | 52      | 59      | 63      | 75      | 7.04   | 3.57   | 12.43  | UHG      |         | 15      | 12      | -7      |        | -3.01  | -19.77 |
| MTH      | BALANCE SHEET    | additional Paid In Capital                                 | 10      | 8       | 5       | 5       | -2.05  | -2.85  | -0.47  | UHG      |         |         | 0       | 1       |        |        | 0.36   |
| MTH      | BALANCE SHEET    | preferred Stock                                            | 0       | 0       | 0       | 0       | 0      | 0      | 0      | UHG      |         |         | 0       | 0       |        |        | 0      |
| MTH      | BALANCE SHEET    | retained Earnings                                          | 42      | 51      | 57      | 70      | 9.1    | 6.42   | 12.9   | UHG      |         |         | 12      | -8      |        |        | -20.13 |
| MTH      | BALANCE SHEET    | ordinary Shares Number                                     | 1       | 1       | 1       | 1       | -0.11  | -0.14  | 0.01   | UHG      | 15      | 11      | 10      | 11      | -3.55  | -1.02  | 1.5    |
| MTH      | BALANCE SHEET    | total Equity Gross Minority Interest                       | 52      | 59      | 63      | 75      | 7.04   | 3.57   | 12.43  | UHG      |         | 15      | 12      | -7      |        | -3.01  | -19.77 |
| MTH      | BALANCE SHEET    | total Capitalization                                       | 75      | 82      | 81      | 92      | 6.94   | -0.7   | 10.59  | UHG      |         | 15      | 12      | 10      |        | -3.01  | -2.85  |
| MTH      | BALANCE SHEET    | stockholders Equity                                        | 52      | 59      | 63      | 75      | 7.04   | 3.57   | 12.43  | UHG      |         | 15      | 12      | -7      |        | -3.01  | -19.77 |
| MTH      | BALANCE SHEET    | share Issued                                               | 1       | 1       | 1       | 1       | -0.11  | -0.14  | 0.01   | UHG      | 15      | 11      | 10      | 11      | -3.55  | -1.02  | 1.5    |
| MTH      | BALANCE SHEET    | tangible Book Value                                        | 52      | 59      | 63      | 75      | 7.04   | 3.57   | 12.43  | UHG      |         | 15      | 12      | -9      |        | -3.01  | -21.12 |
| MTH      | BALANCE SHEET    | working Capital                                            | 72      | 79      | 78      | 88      | 6.79   | -0.86  | 9.87   | UHG      | 10      | 14      | 11      | 36      | 4.38   | -3.3   | 25.28  |
| MTH      | BALANCE SHEET    | net Debt                                                   | 6       | 11      | 5       | 1       | 4.43   | -5.93  | -3.17  | UHG      | 14      | 12      | 23      | 22      | -2.16  | 10.98  | -0.97  |
| MTH      | BALANCE SHEET    | total Debt                                                 | 23      | 23      | 19      | 17      | -0.22  | -4.41  | -1.32  | UHG      | 23      | 24      | 26      | 37      | 0.82   | 1.85   | 11.02  |
| MTH      | BALANCE SHEET    | total Non Current Assets                                   | 4       | 4       | 4       | 5       | 0.15   | -0.07  | 1.28   | UHG      | 1       | 1       | 2       | 5       | 0.55   | 0.5    | 3.25   |
| MTH      | BALANCE SHEET    | total Non Current Liabilities Net Minority Interest        | 24      | 24      | 19      | 18      | -0.1   | -4.5   | -1.28  | UHG      | 0       | 0       | 0       | 49      | 0      | 0.21   | 48.3   |
| MTH      | BALANCE SHEET    | total Tax Payable                                          | 1       | 1       | 0       | 0       | -0.04  | -0.32  | 0.02   | UHG      |         |         | 0       | 0       |        |        | 0.27   |
| MTH      | BALANCE SHEET    | line Of Credit                                             | 0       | 0       | 0       | 0       | 0      | 0      | 0      | UHG      | 22      | 24      | 25      | 18      | 1.17   | 1.68   | -7.01  |
| MTH      | BALANCE SHEET    | other Receivables                                          | 2       | 3       | 3       | 4       | 0.68   | 0.55   | 0.94   |          |         |         |         |         |        |        |        |
| MTH      | BALANCE SHEET    | invested Capital                                           | 75      | 82      | 81      | 92      | 6.94   | -0.7   | 10.59  | UHG      | 23      | 39      | 38      | 28      | 16.19  | -1.36  | -9.86  |
| MTH      | CASH FLOWS       | cash Flow From Continuing Operating Activities             | 12      | -3      | 6       | 6       | -14.72 | 9.39   | -0.64  | UHG      | 22      | 13      | 7       | 7       | -8.46  | -6.22  | -0.56  |
| MTH      | CASH FLOWS       | change In Inventory                                        | -1      | -18     | -10     | -6      | -17.53 | 8.5    | 4.09   | UHG      | 9       | -3      | -6      | 5       | -11.89 | -2.65  | 10.87  |
| MTH      | CASH FLOWS       | change In Other Current Assets                             | -1      | -18     | -10     |         | -17.53 | 8.5    |        | UHG      |         |         | 0       | -1      |        |        | -0.62  |
| MTH      | CASH FLOWS       | change In Other Working Capital                            | 0       |         |         |         |        |        |        |          |         |         |         |         |        |        |        |
| MTH      | CASH FLOWS       | change In Payables And Accrued Expense                     | 2       | 1       | 1       | 0       | -0.49  | -0.26  | -0.85  | UHG      | 1       | 2       | -1      | 3       | 1.06   | -3.63  | 4.57   |
| MTH      | CASH FLOWS       | change In Prepaid Assets                                   | 0       | 0       | 0       | -1      | -0.09  | 0.37   | -0.7   | UHG      | 0       | 0       | -1      | -6      | -0.04  | -0.32  | -5.37  |
| MTH      | CASH FLOWS       | change In Receivables                                      | 0       | -1      | -2      | -1      | -1.31  | -0.37  | 0.59   | UHG      | 0       | 0       | 0       | 0       | -0.1   | -0.01  | 0.63   |
| MTH      | CASH FLOWS       | change In Working Capital                                  | 1       | -18     | -10     | -7      | -19.42 | 8.25   | 3.12   | UHG      | 10      | -1      | -8      | 2       | -10.97 | -6.72  | 9.97   |
| MTH      | CASH FLOWS       | changes In Account Receivables                             | 0       | -1      | -2      | -1      | -1.31  | -0.37  | 0.59   | UHG      | 0       | 0       | 0       | 0       | -0.1   | 0.3    | 0.01   |
| MTH      | CASH FLOWS       | deferred Income Tax                                        | 0       |         |         |         |        |        |        |          |         |         |         |         |        |        |        |
| MTH      | CASH FLOWS       | deferred Tax                                               | 0       |         |         |         |        |        |        |          |         |         |         |         |        |        |        |
| MTH      | CASH FLOWS       | depreciation Amortization Depletion                        | 1       | 1       | 0       | 0       | -0.18  | -0.12  | 0.02   | UHG      | 0       | 0       | 0       | 0       | 0.03   | 0.1    | 0.13   |
| MTH      | CASH FLOWS       | depreciation And Amortization                              | 1       | 1       | 0       | 0       | -0.18  | -0.12  | 0.02   | UHG      | 0       | 0       | 0       | 0       | 0.03   | 0.1    | 0.13   |
| MTH      | CASH FLOWS       | interest Paid Supplemental Data                            | 0       | 0       | 0       | 0       | 0      | 0.03   | -0.01  | UHG      | 1       | 1       | 1       | 4       | -0.56  | 0.31   | 2.67   |
| MTH      | CASH FLOWS       | changes In Cash                                            | 9       | -2      | 4       | 1       | -11.93 | 6.33   | -2.89  | UHG      | 6       | 5       | -8      | 11      | -0.82  | -13.39 | 18.77  |
| MTH      | CASH FLOWS       | dividend Received CFO                                      | 0       | 0       | 0       | 0       | 0.02   | 0      | 0.02   |          |         |         |         |         |        |        |        |
| MTH      | CASH FLOWS       | earnings Losses From Equity Investments                    | 0       | 0       | 0       | 0       | 0.01   | -0.01  | -0.01  | UHG      | 0       | 0       | 0       | 0       | 0      | -0.03  | -0.27  |
| MTH      | CASH FLOWS       | stock Based Compensation                                   | 0       | 0       | 0       | 0       | -0.05  | -0.04  | 0.01   | UHG      | 0       | 0       | 0       | 2       | 0      | 0.3    | 1.37   |
| MTH      | CASH FLOWS       | income Tax Paid Supplemental Data                          | 2       | 4       | 5       |         | 2.42   | 0.65   |        | UHG      |         |         | 0       | 1       |        |        | 1.22   |
| MTH      | CASH FLOWS       | other Non Cash Items                                       | 0       | 0       | 0       | 0       | -0.38  | 0.23   | -0.11  | UHG      | 0       | 0       | 0       | -30     | -0.03  | -0.01  | -29.6  |
| MTH      | CASH FLOWS       | operating Cash Flow                                        | 12      | -3      | 6       | 6       | -14.72 | 9.39   | -0.64  | UHG      | 22      | 13      | 7       | 7       | -8.46  | -6.22  | -0.56  |
| MTH      | CASH FLOWS       | net Income                                                 | 9       | 14      | 16      | 12      | 4.93   | 1.43   | -3.72  | UHG      | 12      | 14      | 15      | 30      | 2.51   | 0.15   | 15.11  |
| MTH      | CASH FLOWS       | net Income From Continuing Operations                      | 9       | 14      | 16      | 12      | 4.93   | 1.43   | -3.72  | UHG      | 12      | 14      | 15      | 30      | 2.51   | 0.15   | 15.11  |
| MTH      | CASH FLOWS       | operating Gains Losses                                     | 0       | 0       | 0       | 0       | 0.36   | -0.36  | 0.01   | UHG      | 0       | 0       | 0       | 2       | 0      | -0.03  | 2.42   |
| MTH      | CASH FLOWS       | cash Flow From Continuing Investing Activities             | 0       | -1      | -1      | -1      | -0.12  | 0.01   | -0.2   | UHG      | 0       | 0       | 0       | -6      | 0.15   | 0.05   | -5.72  |
| MTH      | CASH FLOWS       | net Investment Purchase And Sale                           | 0       | 0       | 0       | 0       | 0      | 0      | 0      |          |         |         |         |         |        |        |        |
| MTH      | CASH FLOWS       | net PPEPurchase And Sale                                   | 0       | 0       | 0       | -1      | -0.06  | 0.07   | -0.19  | UHG      | 0       | 0       | 0       | 0       | 0.15   | 0.06   | 0.03   |
| MTH      | CASH FLOWS       | purchase Of Investment                                     | 0       | 0       | 0       | 0       | 0      | 0.04   | 0      |          |         |         |         |         |        |        |        |
| MTH      | CASH FLOWS       | purchase Of PPE                                            | 0       | 0       | 0       | -1      | -0.06  | 0.07   | -0.19  | UHG      | 0       | 0       | 0       | 0       | 0.15   | 0.06   | 0      |
| MTH      | CASH FLOWS       | purchase Of Business                                       | 0       | 0       | 0       | 0       | -0.03  | -0.06  | -0.01  | UHG      | 0       | 0       | 0       | -6      | 0      | -0.01  | -5.75  |
| MTH      | CASH FLOWS       | sale Of Investment                                         | 0       | 0       | 0       | 0       | 0      | -0.04  | 0      |          |         |         |         |         |        |        |        |
| MTH      | CASH FLOWS       | sale Of PPE                                                | 0       | 0       | 0       | 0       | 0      | 0      | 0      | UHG      | 0       | 0       | 0       | 0       | 0      | 0      | 0.03   |
| MTH      | CASH FLOWS       | investing Cash Flow                                        | 0       | -1      | -1      | -1      | -0.12  | 0.01   | -0.2   | UHG      | 0       | 0       | 0       | -6      | 0.15   | 0.05   | -5.72  |
| MTH      | CASH FLOWS       | capital Expenditure                                        | 0       | 0       | 0       | -1      | -0.06  | 0.07   | -0.19  | UHG      | 0       | 0       | 0       | 0       | 0.15   | 0.06   | 0      |
| MTH      | CASH FLOWS       | net Business Purchase And Sale                             | 0       | 0       | 0       | 0       | -0.03  | -0.06  | -0.01  | UHG      | 0       | 0       | 0       | -6      | 0      | -0.01  | -5.75  |
| MTH      | CASH FLOWS       | cash Flow From Continuing Financing Activities             | -2      | 1       | -2      | -4      | 2.91   | -3.06  | -2.05  | UHG      | -16     | -8      | -15     | 10      | 7.49   | -7.22  | 25.06  |
| MTH      | CASH FLOWS       | issuance Of Debt                                           | 0       | 9       | 0       | 0       | 8.74   | -8.74  | 0      | UHG      | 63      | 68      | 40      | 34      | 4.78   | -28.38 | -5.67  |
| MTH      | CASH FLOWS       | repurchase Of Capital Stock                                | -2      | -1      | -2      | -1      | 0.36   | -0.55  | 0.77   |          |         |         |         |         |        |        |        |
| MTH      | CASH FLOWS       | repayment Of Debt                                          | 0       | -6      | 0       | -3      | -6.07  | 6.11   | -2.18  | UHG      | -67     | -62     | -36     | -25     | 4.72   | 25.82  | 11.08  |
| MTH      | CASH FLOWS       | dividends Received CFI                                     | 0       | 0       | 0       | 0       | -0.02  | 0      | 0      |          |         |         |         |         |        |        |        |
| MTH      | CASH FLOWS       | financing Cash Flow                                        | -2      | 1       | -2      | -4      | 2.91   | -3.06  | -2.05  | UHG      | -16     | -8      | -15     | 10      | 7.49   | -7.22  | 25.06  |
| MTH      | CASH FLOWS       | net Issuance Payments Of Debt                              | 0       | 2       | 0       | -3      | 2.67   | -2.63  | -2.18  | UHG      | -3      | 6       | 4       | 9       | 9.5    | -2.56  | 5.41   |
| MTH      | CASH FLOWS       | net Long Term Debt Issuance                                | 0       | 2       | 0       | -3      | 2.67   | -2.63  | -2.18  | UHG      | 0       | 0       | 0       | 17      | 0.02   | -0.02  | 16.97  |
| MTH      | CASH FLOWS       | long Term Debt Issuance                                    | 0       | 9       | 0       | 0       | 8.74   | -8.74  | 0      | UHG      | 0       | 0       | 0       | 17      | 0      | 0      | 16.96  |
| MTH      | CASH FLOWS       | long Term Debt Payments                                    | 0       | -6      | 0       | -3      | -6.07  | 6.11   | -2.18  | UHG      | 0       | 0       | 0       | 0       | 0.02   | -0.02  | 0      |
| MTH      | CASH FLOWS       | cash Dividends Paid                                        |         | 0       | 0       | -1      |        | 0      | -0.64  | UHG      | -7      | -8      | -11     | -4      | -0.92  | -3.61  | 7.11   |
| MTH      | CASH FLOWS       | net Common Stock Issuance                                  | -2      | -1      | -2      | -1      | 0.36   | -0.55  | 0.77   | UHG      |         |         | 0       | 1       |        |        | 1.12   |
| MTH      | CASH FLOWS       | free Cash Flow                                             | 11      | -3      | 6       | 5       | -14.78 | 9.46   | -0.84  | UHG      | 22      | 13      | 7       | 7       | -8.31  | -6.16  | -0.56  |
| MTH      | CASH FLOWS       | net Other Financing Charges                                |         | 0       |         |         |        |        |        | UHG      | -6      | -7      | -8      | 3       | -1.09  | -1.05  | 11.42  |
| MTH      | CASH FLOWS       | common Stock Payments                                      | -2      | -1      | -2      | -1      | 0.36   | -0.55  | 0.77   |          |         |         |         |         |        |        |        |
| MTH      | CASH FLOWS       | common Stock Dividend Paid                                 |         | 0       | 0       | -1      |        | 0      | -0.64  | UHG      | -7      | -8      | -11     | -4      | -0.92  | -3.61  | 7.11   |
| MTH      | CASH FLOWS       | change In Cash Supplemental As Reported                    | 9       | -2      | 4       | 1       | -11.93 | 6.33   | -2.89  | UHG      | 6       | 5       | -8      | 11      | -0.82  | -13.39 | 18.77  |
| MTH      | CASH FLOWS       | beginning Cash Position                                    | 7       | 14      | 10      | 14      | 7.4    | -4.67  | 4.22   | UHG      | 3       | 7       | 11      | 3       | 3.81   | 4.06   | -7.89  |
| MTH      | CASH FLOWS       | end Cash Position                                          | 17      | 12      | 14      | 15      | -4.53  | 1.67   | 1.33   | UHG      | 9       | 12      | 3       | 13      | 2.98   | -9.33  | 10.88  |
| MTH      | INCOME STATEMENT | total Revenue                                              | 100     | 100     | 100     | 100     | 0      | 0      | 0      | UHG      | 100     | 100     | 100     | 100     | 0      | 0      | 0      |
| MTH      | INCOME STATEMENT | operating Revenue                                          | 100     | 100     | 100     | 100     | 0      | 0.02   | 0.11   | UHG      | 100     | 100     | 100     | 100     | 0      | 0      | 0      |
| MTH      | INCOME STATEMENT | gross Profit                                               | 22      | 28      | 29      | 25      | 6.23   | 0.74   | -3.88  | UHG      | 21      | 23      | 25      | 19      | 2.73   | 1.66   | -5.99  |
| MTH      | INCOME STATEMENT | cost Of Revenue                                            | 78      | 72      | 71      | 75      | -6.23  | -0.74  | 3.88   | UHG      | 79      | 77      | 75      | 81      | -2.73  | -1.66  | 5.99   |
| MTH      | INCOME STATEMENT | reconciled Cost Of Revenue                                 | 78      | 72      | 71      | 75      | -6.23  | -0.74  | 3.88   | UHG      | 79      | 77      | 75      | 81      | -2.73  | -1.66  | 5.99   |
| MTH      | INCOME STATEMENT | operating Expense                                          | 10      | 9       | 8       | 10      | -0.85  | -0.87  | 1.85   | UHG      | 9       | 9       | 10      | 15      | -0.25  | 1.53   | 5.03   |
| MTH      | INCOME STATEMENT | selling And Marketing Expense                              | 6       | 6       | 5       | 6       | -0.84  | -0.41  | 1.14   |          |         |         |         |         |        |        |        |
| MTH      | INCOME STATEMENT | selling General And Administration                         | 10      | 9       | 8       | 10      | -0.85  | -0.87  | 1.85   | UHG      | 9       | 9       | 10      | 15      | -0.25  | 1.53   | 5.03   |
| MTH      | INCOME STATEMENT | general And Administrative Expense                         | 4       | 4       | 3       | 4       | 0      | -0.46  | 0.71   |          |         |         |         |         |        |        |        |
| MTH      | INCOME STATEMENT | other Gand A                                               | 4       | 4       | 3       | 4       | 0      | -0.46  | 0.71   |          |         |         |         |         |        |        |        |
| MTH      | INCOME STATEMENT | total Expenses                                             | 88      | 81      | 80      | 85      | -7.07  | -1.61  | 5.73   | UHG      | 89      | 86      | 86      | 97      | -2.98  | -0.13  | 11.02  |
| MTH      | INCOME STATEMENT | operating Income                                           | 12      | 19      | 20      | 15      | 7.07   | 1.61   | -5.73  | UHG      | 11      | 14      | 14      | 3       | 2.98   | 0.13   | -11.02 |
| MTH      | INCOME STATEMENT | ebit                                                       | 12      | 19      | 20      | 15      | 6.67   | 1.92   | -5     | UHG      | 11      | 14      | 14      | 3       | 2.98   | 0.13   | -11.02 |
| MTH      | INCOME STATEMENT | normalized EBITDA                                          | 13      | 19      | 21      | 16      | 6.84   | 1.45   | -4.97  | UHG      | 11      | 14      | 15      | -24     | 3      | 0.23   | -38.39 |
| MTH      | INCOME STATEMENT | e BITDA                                                    | 13      | 19      | 21      | 16      | 6.49   | 1.8    | -4.98  | UHG      | 11      | 14      | 15      | 4       | 3      | 0.23   | -10.89 |
| MTH      | INCOME STATEMENT | other Income Expense                                       | 0       | 0       | 0       | 1       | -0.41  | 0.3    | 0.72   | UHG      | 1       | 0       | 0       | 27      | -0.47  | 0.02   | 26.83  |
| MTH      | INCOME STATEMENT | other Non Operating Income Expenses                        | 0       | 0       | 0       | 1       | -0.05  | -0.05  | 0.74   | UHG      | 1       | 0       | 0       | -1      | -0.47  | -0.01  | -0.94  |
| MTH      | INCOME STATEMENT | interest Expense                                           | 0       | 0       | 0       | 0       | -0.04  | -0.01  | 0      |          |         |         |         |         |        |        |        |
| MTH      | INCOME STATEMENT | interest Expense Non Operating                             | 0       | 0       | 0       | 0       | -0.04  | -0.01  | 0      |          |         |         |         |         |        |        |        |
| MTH      | INCOME STATEMENT | net Interest Income                                        | 0       | 0       | 0       | 0       | 0.04   | 0.01   | 0      |          |         |         |         |         |        |        |        |
| MTH      | INCOME STATEMENT | net Non Operating Interest Income Expense                  | 0       | 0       | 0       | 0       | 0.04   | 0.01   | 0      |          |         |         |         |         |        |        |        |
| MTH      | INCOME STATEMENT | pretax Income                                              | 12      | 19      | 20      | 15      | 6.71   | 1.92   | -5     | UHG      | 12      | 14      | 15      | 30      | 2.51   | 0.15   | 15.81  |
| MTH      | INCOME STATEMENT | tax Provision                                              | 2       | 4       | 5       | 3       | 1.78   | 0.49   | -1.29  | UHG      |         |         | 0       | 1       |        |        | 0.7    |
| MTH      | INCOME STATEMENT | tax Rate For Calcs                                         | 0       | 0       | 0       | 0       | 0      | 0      | 0      | UHG      | 0       | 0       | 0       | 0       | 0      | 0      | 0      |
| MTH      | INCOME STATEMENT | tax Effect Of Unusual Items                                | 0       | 0       | 0       | 0       | -0.08  | 0.08   | 0      | UHG      | 0       | 0       | 0       | 1       | 0      | 0      | 0.66   |
| MTH      | INCOME STATEMENT | other Special Charges                                      |         | 0       |         | 0       |        |        |        |          |         |         |         |         |        |        |        |
| MTH      | INCOME STATEMENT | net Income From Continuing Operation Net Minority Interest | 9       | 14      | 16      | 12      | 4.93   | 1.43   | -3.72  | UHG      | 12      | 14      | 15      | 30      | 2.51   | 0.15   | 15.11  |
| MTH      | INCOME STATEMENT | net Income From Continuing And Discontinued Operation      | 9       | 14      | 16      | 12      | 4.93   | 1.43   | -3.72  | UHG      | 12      | 14      | 15      | 30      | 2.51   | 0.15   | 15.11  |
| MTH      | INCOME STATEMENT | net Income Continuous Operations                           | 9       | 14      | 16      | 12      | 4.93   | 1.43   | -3.72  | UHG      | 12      | 14      | 15      | 30      | 2.51   | 0.15   | 15.11  |
| MTH      | INCOME STATEMENT | net Income Including Noncontrolling Interests              | 9       | 14      | 16      | 12      | 4.93   | 1.43   | -3.72  | UHG      | 12      | 14      | 15      | 30      | 2.51   | 0.15   | 15.11  |
| MTH      | INCOME STATEMENT | net Income                                                 | 9       | 14      | 16      | 12      | 4.93   | 1.43   | -3.72  | UHG      | 12      | 14      | 15      | 30      | 2.51   | 0.15   | 15.11  |
| MTH      | INCOME STATEMENT | net Income Common Stockholders                             | 9       | 14      | 16      | 12      | 4.93   | 1.43   | -3.72  | UHG      | 12      | 14      | 15      | 30      | 2.51   | 0.15   | 15.11  |
| MTH      | INCOME STATEMENT | normalized Income                                          | 9       | 15      | 16      | 12      | 5.2    | 1.15   | -3.71  | UHG      | 12      | 14      | 15      | 3       | 2.51   | 0.15   | -11.73 |
| MTH      | INCOME STATEMENT | diluted NIAvailto Com Stockholders                         | 9       | 14      | 16      | 12      | 4.93   | 1.43   | -3.72  | UHG      | 12      | 14      | 15      | 30      | 2.51   | 0.15   | 15.11  |
| MTH      | INCOME STATEMENT | basic EPS                                                  | 0       | 0       | 0       | 0       | 0      | 0      | 0      | UHG      | 0       | 0       | 0       | 0       | 0      | 0      | 0      |
| MTH      | INCOME STATEMENT | diluted EPS                                                | 0       | 0       | 0       | 0       | 0      | 0      | 0      | UHG      | 0       | 0       | 0       | 0       | 0      | 0      | 0      |
| MTH      | INCOME STATEMENT | basic Average Shares                                       | 1       | 1       | 1       | 1       | -0.11  | -0.15  | 0.01   | UHG      | 11      | 9       | 10      | 11      | -2.8   | 1.3    | 0.85   |
| MTH      | INCOME STATEMENT | diluted Average Shares                                     | 1       | 1       | 1       | 1       | -0.12  | -0.14  | 0.01   | UHG      | 11      | 9       | 10      | 13      | -2.8   | 1.3    | 3.25   |
| MTH      | INCOME STATEMENT | special Income Charges                                     | 0       | 0       | 0       | 0       | -0.35  | 0.35   | -0.01  |          |         |         |         |         |        |        |        |
| MTH      | INCOME STATEMENT | total Unusual Items                                        | 0       | 0       | 0       | 0       | -0.35  | 0.35   | -0.01  | UHG      |         |         |         | 27      |        |        |        |
| MTH      | INCOME STATEMENT | total Unusual Items Excluding Goodwill                     | 0       | 0       | 0       | 0       | -0.35  | 0.35   | -0.01  | UHG      |         |         |         | 27      |        |        |        |
| MTH      | INCOME STATEMENT | reconciled Depreciation                                    | 1       | 1       | 0       | 0       | -0.18  | -0.12  | 0.02   | UHG      | 0       | 0       | 0       | 0       | 0.03   | 0.1    | 0.13   |

Following table presents the Cosine Distance between financials of chosen companies. It can be seing that FWRD and MATX have a cosine distance very close to 100 for the year 2022. This is expected. Normally, the cosine distance goes here from -100 to 100. values close to -100 or 100 indicate strong similarity. FWRD and MATX are logistic companies with similar economics, therefore you expect them to have scores closer to 100 compared to companies from different industries or different ways of operate. This tecnique is important to identify companies whose financials diverge from companies within the same industry or with simmilar economics.

I use this method to choose solid companies accross the years. Here 'fistresn' and 'change' are normalized variables comming from the finanacials after dividing by revenue. To finish, notice that KAI and FWRD are very close as well, despite these companies are in different industries. The reason for this is that both companies have very similar economics. KAI is a flow control company. 
| param  |        |         |            | CHG        | CHG        | CHG        | FISTRESN   | FISTRESN   | FISTRESN   | FISTRESN   | FISTRESN  |
|--------|--------|---------|------------|------------|------------|------------|------------|------------|------------|------------|-----------|
| afidtc |        |         |            | 12/31/2021 | 12/31/2022 | 12/31/2023 | 12/31/2020 | 12/31/2021 | 12/31/2022 | 12/31/2023 | 9/30/2024 |
| dtype  | subjid | asubjid | fidtc      |            |            |            |            |            |            |            |           |
| COSINE | FWRD   | MATX    | 12/31/2020 |            |            |            | 88         | 88         | 87         | 91         | 61        |
| COSINE | FWRD   | MATX    | 12/31/2021 | 6          | -18        | -35        | 90         | 91         | 90         | 91         | 61        |
| COSINE | FWRD   | MATX    | 12/31/2022 | 77         | 32         | -56        | 77         | 84         | 84         | 82         | 61        |
| COSINE | FWRD   | MATX    | 12/31/2023 | -37        | -11        | 38         | 67         | 64         | 61         | 65         | 21        |
| COSINE | FWRD   | MATX    | 9/30/2024  |            |            |            | 17         | 7          | 6          | 15         | 30        |
| COSINE | HDSN   | MATX    | 12/31/2020 |            |            |            | 78         | 70         | 66         | 70         | 42        |
| COSINE | HDSN   | MATX    | 12/31/2021 | 59         | 24         | -32        | 77         | 80         | 77         | 75         | 45        |
| COSINE | HDSN   | MATX    | 12/31/2022 | 46         | 32         | -35        | 69         | 82         | 82         | 73         | 52        |
| COSINE | HDSN   | MATX    | 12/31/2023 | -6         | 40         | 62         | 68         | 81         | 83         | 81         | 48        |
| COSINE | HDSN   | MATX    | 9/30/2024  |            |            |            | 41         | 54         | 53         | 38         | 93        |
| COSINE | IDCC   | MATX    | 12/31/2020 |            |            |            | 57         | 61         | 64         | 67         | 15        |
| COSINE | IDCC   | MATX    | 12/31/2021 | 18         | -50        | -23        | 55         | 59         | 61         | 64         | 12        |
| COSINE | IDCC   | MATX    | 12/31/2022 | -18        | 13         | -9         | 57         | 60         | 63         | 63         | 14        |
| COSINE | IDCC   | MATX    | 12/31/2023 | 29         | -7         | -34        | 52         | 59         | 62         | 59         | 19        |
| COSINE | IDCC   | MATX    | 9/30/2024  |            |            |            | 21         | 37         | 37         | 20         | 49        |
| COSINE | KAI    | MATX    | 12/31/2020 |            |            |            | 82         | 82         | 83         | 85         | 37        |
| COSINE | KAI    | MATX    | 12/31/2021 | 11         | -10        | -28        | 82         | 83         | 83         | 84         | 40        |
| COSINE | KAI    | MATX    | 12/31/2022 | 50         | 15         | -21        | 81         | 86         | 87         | 87         | 44        |
| COSINE | KAI    | MATX    | 12/31/2023 | 36         | 44         | 7          | 79         | 85         | 87         | 88         | 44        |
| COSINE | KAI    | MATX    | 9/30/2024  |            |            |            | 42         | 51         | 49         | 36         | 85        |
| COSINE | MATX   | MATX    | 12/31/2020 |            |            |            | 100        | 93         | 89         | 92         | 45        |
| COSINE | MATX   | MATX    | 12/31/2021 | 100        | 31         | -66        | 93         | 100        | 99         | 94         | 57        |
| COSINE | MATX   | MATX    | 12/31/2022 | 31         | 100        | 16         | 89         | 99         | 100        | 95         | 56        |
| COSINE | MATX   | MATX    | 12/31/2023 | -66        | 16         | 100        | 92         | 94         | 95         | 100        | 42        |
| COSINE | MATX   | MATX    | 9/30/2024  |            |            |            | 45         | 57         | 56         | 42         | 100       |
| COSINE | MCRI   | MATX    | 12/31/2020 |            |            |            | 82         | 80         | 80         | 88         | 13        |
| COSINE | MCRI   | MATX    | 12/31/2021 | 53         | -19        | -75        | 82         | 85         | 86         | 90         | 26        |
| COSINE | MCRI   | MATX    | 12/31/2022 | 59         | 6          | -55        | 78         | 83         | 86         | 89         | 29        |
| COSINE | MCRI   | MATX    | 12/31/2023 | -12        | -38        | -30        | 79         | 84         | 85         | 88         | 31        |
| COSINE | MCRI   | MATX    | 9/30/2024  |            |            |            | 35         | 49         | 48         | 32         | 77        |
| COSINE | MTH    | MATX    | 12/31/2020 |            |            |            | 60         | 68         | 69         | 69         | 49        |
| COSINE | MTH    | MATX    | 12/31/2021 | 6          | 18         | 8          | 58         | 67         | 69         | 68         | 43        |
| COSINE | MTH    | MATX    | 12/31/2022 | 49         | 34         | -16        | 57         | 68         | 70         | 69         | 45        |
| COSINE | MTH    | MATX    | 12/31/2023 | -21        | 47         | 69         | 57         | 66         | 69         | 70         | 41        |
| COSINE | MTH    | MATX    | 9/30/2024  |            |            |            | 36         | 43         | 41         | 33         | 77        |
| COSINE | SHLS   | MATX    | 12/31/2020 |            |            |            | 39         | 29         | 22         | 19         | 18        |
| COSINE | SHLS   | MATX    | 12/31/2021 | 6          | 20         | 24         | 50         | 42         | 38         | 39         | 15        |
| COSINE | SHLS   | MATX    | 12/31/2022 | 32         | 35         | -1         | 73         | 79         | 79         | 76         | 35        |
| COSINE | SHLS   | MATX    | 12/31/2023 | -6         | 20         | 35         | 72         | 75         | 77         | 80         | 31        |
| COSINE | SHLS   | MATX    | 9/30/2024  |            |            |            | 43         | 46         | 44         | 33         | 78        |
| COSINE | TH     | MATX    | 12/31/2020 |            |            |            | 85         | 74         | 70         | 76         | 18        |
| COSINE | TH     | MATX    | 12/31/2021 | 71         | 7          | -64        | 87         | 78         | 74         | 78         | 25        |
| COSINE | TH     | MATX    | 12/31/2022 | 71         | 18         | -52        | 87         | 87         | 84         | 83         | 34        |
| COSINE | TH     | MATX    | 12/31/2023 | 40         | 36         | -13        | 84         | 91         | 91         | 87         | 37        |
| COSINE | TH     | MATX    | 9/30/2024  |            |            |            | 35         | 55         | 54         | 33         | 83        |


