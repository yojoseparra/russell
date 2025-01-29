
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

#### Making the data more comparable

Data was filtered based on the parameters explained in the methodology section. Data from Yahoo was download and programatically and visually analyzed. Few candidates were analyzed. Additionally, these few candidate companies were compared with wide MOAT companies that have strong financials. Hereunder there is an expample of high quality companies side by side.

Table 1. Table of standardized yearly data between AAPL and MSFT, Two Wide MOAT companies

| subjid_x | sctestcd                                                   | 9/30/2021 | 9/30/2022 | 9/30/2022 | subjid_y | 6/30/2024 | 6/30/2021 | 6/30/2024 |
|----------|------------------------------------------------------------|-----------|-----------|-----------|----------|-----------|-----------|-----------|
|          |                                                            | fistresn  | fistresn  | chg       |          | fistresn  | fistresn  | chg       |
| AAPL     | Cash And Cash Equivalents                                  | 10%       | 6%        | -32%      | MSFT     | 7%        | 8%        | -47%      |
| AAPL     | Cash Equivalents                                           | 5%        | 1%        | -71%      | MSFT     | 3%        | 4%        | -74%      |
| AAPL     | Cash Financial                                             | 5%        | 5%        | 7%        | MSFT     | 5%        | 4%        | 36%       |
| AAPL     | Cash Cash Equivalents And Short Term Investments           | 17%       | 12%       | -23%      | MSFT     | 31%       | 77%       | -32%      |
| AAPL     | Commercial Paper                                           | 2%        | 3%        | 66%       |          |           |           |           |
| AAPL     | Accounts Receivable                                        | 7%        | 7%        | 7%        | MSFT     | 23%       | 23%       | 17%       |
|          | Gross Accounts Receivable                                  |           |           |           | MSFT     | 24%       | 23%       | 17%       |
|          | Allowance For Doubtful Accounts Receivable                 |           |           |           | MSFT     | 0%        | 0%        | 28%       |
| AAPL     | Inventory                                                  | 2%        | 1%        | -25%      | MSFT     | 1%        | 2%        | -50%      |
|          | Raw Materials                                              |           |           |           | MSFT     | 0%        | 1%        | -44%      |
|          | Work In Process                                            |           |           |           | MSFT     | 0%        | 0%        | -70%      |
| AAPL     | Current Assets                                             | 37%       | 34%       | 0%        | MSFT     | 65%       | 110%      | -13%      |
|          | Finished Goods                                             |           |           |           | MSFT     | 0%        | 1%        | -52%      |
| AAPL     | Receivables                                                | 14%       | 15%       | 18%       | MSFT     | 23%       | 23%       | 17%       |
|          | Hedging Assets Current                                     |           |           |           | MSFT     | 0%        | 0%        | 100%      |
| AAPL     | Other Current Assets                                       | 4%        | 5%        | 50%       | MSFT     | 11%       | 8%        | 19%       |
| AAPL     | Gross PPE                                                  | 33%       | 32%       | 4%        | MSFT     | 94%       | 73%       | 30%       |
| AAPL     | Accumulated Depreciation                                   | -19%      | -18%      | 3%        | MSFT     | -31%      | -31%      | 12%       |
| AAPL     | Net PPE                                                    | 14%       | 13%       | 6%        | MSFT     | 63%       | 42%       | 41%       |
| AAPL     | Land And Improvements                                      | 5%        | 6%        | 10%       | MSFT     | 3%        | 2%        | 44%       |
|          | Buildings And Improvements                                 |           |           |           | MSFT     | 38%       | 26%       | 37%       |
| AAPL     | Machinery Furniture Equipment                              | 22%       | 21%       | 3%        | MSFT     | 41%       | 34%       | 24%       |
| AAPL     | Investments And Advances                                   | 35%       | 31%       | -6%       | MSFT     | 6%        | 4%        | 48%       |
| AAPL     | Investmentin Financial Assets                              | 35%       | 31%       | -6%       |          |           |           |           |
|          | Goodwill                                                   |           |           |           | MSFT     | 49%       | 30%       | 76%       |
|          | Goodwill And Other Intangible Assets                       |           |           |           | MSFT     | 60%       | 34%       | 90%       |
|          | Other Intangible Assets                                    |           |           |           | MSFT     | 11%       | 5%        | 195%      |
| AAPL     | Leases                                                     | 3%        | 3%        | 2%        | MSFT     | 4%        | 4%        | 12%       |
| AAPL     | Other Properties                                           | 3%        | 3%        | 3%        | MSFT     | 8%        | 7%        | 32%       |
| AAPL     | Properties                                                 | 0%        | 0%        |           | MSFT     | 0%        | 0%        |           |
| AAPL     | Non Current Deferred Assets                                |           | 4%        |           |          |           |           |           |
| AAPL     | Available For Sale Securities                              | 35%       | 31%       | -6%       |          |           |           |           |
| AAPL     | Other Non Current Assets                                   | 11%       | 7%        | -26%      | MSFT     | 15%       | 9%        | 19%       |
| AAPL     | Other Investments                                          | 35%       | 31%       | -6%       |          |           |           |           |
| AAPL     | Net Tangible Assets                                        | 17%       | 13%       | -20%      | MSFT     | 50%       | 50%       | -6%       |
| AAPL     | Other Short Term Investments                               | 8%        | 6%        | -11%      | MSFT     | 23%       | 69%       | -25%      |
| AAPL     | Total Assets                                               | 96%       | 89%       | 0%        | MSFT     | 209%      | 199%      | 24%       |
| AAPL     | Accounts Payable                                           | 15%       | 16%       | 17%       | MSFT     | 9%        | 9%        | 22%       |
| AAPL     | Payables                                                   | 15%       | 18%       | 29%       | MSFT     | 11%       | 10%       | 21%       |
| AAPL     | Payables And Accrued Expenses                              | 15%       | 18%       | 29%       | MSFT     | 11%       | 10%       | 21%       |
| AAPL     | Income Tax Payable                                         |           | 2%        |           | MSFT     | 2%        | 1%        | 21%       |
| AAPL     | Other Current Liabilities                                  | 13%       | 13%       | 15%       | MSFT     | 8%        | 7%        | 30%       |
| AAPL     | Current Liabilities                                        | 34%       | 39%       | 23%       | MSFT     | 51%       | 53%       | 20%       |
|          | Pensionand Other Post Retirement Benefit Plans Current     |           |           |           | MSFT     | 5%        | 6%        | 14%       |
| AAPL     | Current Deferred Revenue                                   | 2%        | 2%        | 4%        | MSFT     | 23%       | 25%       | 13%       |
| AAPL     | Other Current Borrowings                                   | 3%        | 3%        | 16%       |          |           |           |           |
| AAPL     | Current Debt                                               | 4%        | 5%        | 35%       | MSFT     | 4%        | 5%        | 70%       |
| AAPL     | Current Debt And Capital Lease Obligation                  | 5%        | 6%        | 33%       | MSFT     | 4%        | 5%        | 70%       |
| AAPL     | Current Capital Lease Obligation                           | 0%        | 0%        | 9%        |          |           |           |           |
| AAPL     | Long Term Debt                                             | 30%       | 25%       | -9%       | MSFT     | 17%       | 30%       | 2%        |
| AAPL     | Current Deferred Liabilities                               | 2%        | 2%        | 4%        | MSFT     | 23%       | 25%       | 13%       |
| AAPL     | Long Term Capital Lease Obligation                         | 3%        | 3%        | 5%        | MSFT     | 6%        | 6%        | 22%       |
| AAPL     | Long Term Debt And Capital Lease Obligation                | 33%       | 28%       | -8%       | MSFT     | 24%       | 36%       | 6%        |
|          | Long Term Equity Investment                                |           |           |           | MSFT     | 6%        | 4%        | 48%       |
|          | Non Current Deferred Liabilities                           |           |           |           | MSFT     | 2%        | 2%        | 56%       |
|          | Non Current Deferred Revenue                               |           |           |           | MSFT     | 1%        | 2%        | -11%      |
| AAPL     | Non Current Deferred Taxes Assets                          |           | 4%        |           |          |           |           |           |
|          | Non Current Deferred Taxes Liabilities                     |           |           |           | MSFT     | 1%        | 0%        | 505%      |
| AAPL     | Tradeand Other Payables Non Current                        | 7%        | 4%        | -33%      | MSFT     | 11%       | 16%       | 9%        |
| AAPL     | Other Non Current Liabilities                              | 5%        | 6%        | 18%       | MSFT     | 11%       | 8%        | 51%       |
| AAPL     | Total Liabilities Net Minority Interest                    | 79%       | 77%       | 5%        | MSFT     | 99%       | 114%      | 18%       |
| AAPL     | Common Stock                                               | 16%       | 16%       | 13%       | MSFT     | 41%       | 49%       | 8%        |
| AAPL     | Common Stock Equity                                        | 17%       | 13%       | -20%      | MSFT     | 110%      | 84%       | 30%       |
| AAPL     | Capital Lease Obligations                                  | 3%        | 3%        | 5%        | MSFT     | 6%        | 6%        | 22%       |
| AAPL     | Capital Stock                                              | 16%       | 16%       | 13%       | MSFT     | 41%       | 49%       | 8%        |
| AAPL     | Retained Earnings                                          | 2%        | -1%       | -155%     | MSFT     | 71%       | 34%       | 46%       |
| AAPL     | Tangible Book Value                                        | 17%       | 13%       | -20%      | MSFT     | 50%       | 50%       | -6%       |
| AAPL     | Other Equity Adjustments                                   | 0%        | -3%       | -6915%    | MSFT     | -2%       | 1%        | -12%      |
| AAPL     | Gains Losses Not Affecting Retained Earnings               | 0%        | -3%       | -6915%    | MSFT     | -2%       | 1%        | -12%      |
| AAPL     | Treasury Shares Number                                     |           |           |           |          |           |           |           |
| AAPL     | Total Equity Gross Minority Interest                       | 17%       | 13%       | -20%      | MSFT     | 110%      | 84%       | 30%       |
| AAPL     | Net Debt                                                   | 25%       | 24%       | 7%        | MSFT     | 14%       | 26%       | 166%      |
| AAPL     | Total Debt                                                 | 37%       | 34%       | -3%       | MSFT     | 27%       | 40%       | 12%       |
| AAPL     | Total Capitalization                                       | 47%       | 38%       | -13%      | MSFT     | 127%      | 114%      | 25%       |
| AAPL     | Working Capital                                            | 3%        | -5%       | -299%     | MSFT     | 14%       | 57%       | -57%      |
| AAPL     | Ordinary Shares Number                                     | 4%        | 4%        | -3%       | MSFT     | 3%        | 4%        | 0%        |
| AAPL     | Stockholders Equity                                        | 17%       | 13%       | -20%      | MSFT     | 110%      | 84%       | 30%       |
| AAPL     | Share Issued                                               | 4%        | 4%        | -3%       | MSFT     | 3%        | 4%        | 0%        |
| AAPL     | Total Non Current Assets                                   | 59%       | 55%       | 1%        | MSFT     | 144%      | 89%       | 55%       |
| AAPL     | Total Non Current Liabilities Net Minority Interest        | 44%       | 38%       | -9%       | MSFT     | 48%       | 61%       | 17%       |
| AAPL     | Total Tax Payable                                          |           | 2%        |           | MSFT     | 2%        | 1%        | 21%       |
| AAPL     | Other Receivables                                          | 7%        | 8%        | 30%       |          |           |           |           |
| AAPL     | Invested Capital                                           | 51%       | 43%       | -9%       | MSFT     | 131%      | 119%      | 26%       |
| AAPL     | Change In Account Payable                                  | 3%        | 2%        | -23%      | MSFT     | 1%        | 2%        | -230%     |
| AAPL     | Change In Payable                                          | 3%        | 2%        | -23%      | MSFT     | 2%        | 2%        | -270%     |
| AAPL     | Income Tax Paid Supplemental Data                          | 7%        | 5%        | -23%      |          |           |           |           |
| AAPL     | Change In Payables And Accrued Expense                     | 3%        | 2%        | -23%      | MSFT     | 2%        | 2%        | -270%     |
| AAPL     | Change In Other Current Liabilities                        | 2%        | 2%        | -18%      | MSFT     | 2%        | 3%        | 99%       |
| AAPL     | Change In Other Working Capital                            | 0%        | 0%        | -71%      | MSFT     | 2%        | 1%        | -3%       |
| AAPL     | Change In Inventory                                        | -1%       | 0%        | -156%     | MSFT     | 1%        | 0%        | 3%        |
| AAPL     | Change In Receivables                                      | -4%       | -2%       | -33%      | MSFT     | -3%       | -4%       | 76%       |
|          | Change In Tax Payable                                      |           |           |           | MSFT     | 1%        |           | -571%     |
| AAPL     | Change In Working Capital                                  | -1%       | 0%        | -124%     | MSFT     | 1%        | -1%       | -176%     |
|          | Change In Income Tax Payable                               |           |           |           | MSFT     | 1%        |           | -571%     |
| AAPL     | Deferred Income Tax                                        | -1%       | 0%        | -119%     | MSFT     | -2%       | 0%        | -22%      |
| AAPL     | Deferred Tax                                               | -1%       | 0%        | -119%     | MSFT     | -2%       | 0%        | -22%      |
| AAPL     | Changes In Account Receivables                             | -3%       | 0%        | -82%      | MSFT     | -3%       | -4%       | 76%       |
| AAPL     | Change In Other Current Assets                             | -2%       | -2%       | -19%      | MSFT     | -3%       | -3%       | 75%       |
|          | Depreciation                                               |           |           |           | MSFT     | 9%        | 7%        | 61%       |
| AAPL     | Depreciation Amortization Depletion                        | 3%        | 3%        | -2%       | MSFT     | 9%        | 7%        | 61%       |
| AAPL     | Depreciation And Amortization                              | 3%        | 3%        | -2%       | MSFT     | 9%        | 7%        | 61%       |
| AAPL     | Stock Based Compensation                                   | 2%        | 2%        | 14%       | MSFT     | 4%        | 4%        | 12%       |
| AAPL     | Interest Paid Supplemental Data                            | 1%        | 1%        | 7%        |          |           |           |           |
|          | Gain Loss On Investment Securities                         |           |           |           | MSFT     |           |           |           |
|          | Operating Gains Losses                                     |           |           |           | MSFT     | 0%        | -1%       | 56%       |
| AAPL     | Other Non Cash Items                                       | -1%       | 0%        | -120%     |          |           |           |           |
| AAPL     | Operating Cash Flow                                        | 28%       | 31%       | 17%       | MSFT     | 48%       | 46%       | 35%       |
| AAPL     | Cash Flow From Continuing Operating Activities             | 28%       | 31%       | 17%       | MSFT     | 48%       | 46%       | 35%       |
| AAPL     | Sale Of Investment                                         | 29%       | 17%       | -37%      | MSFT     | 15%       | 39%       | -25%      |
| AAPL     | Purchase Of Business                                       | 0%        | 0%        | 827%      | MSFT     | -28%      | -5%       | 4040%     |
| AAPL     | Purchase Of PPE                                            | -3%       | -3%       | -3%       | MSFT     | -18%      | -12%      | 58%       |
| AAPL     | Purchase Of Investment                                     | -30%      | -20%      | -30%      | MSFT     | -7%       | -37%      | -53%      |
| AAPL     | Net PPEPurchase And Sale                                   | -3%       | -3%       | -3%       | MSFT     | -18%      | -12%      | 58%       |
| AAPL     | Net Business Purchase And Sale                             | 0%        | 0%        | 827%      | MSFT     | -28%      | -5%       | 4040%     |
| AAPL     | Net Income                                                 | 26%       | 25%       | 5%        | MSFT     | 36%       | 36%       | 22%       |
| AAPL     | Net Income From Continuing Operations                      | 26%       | 25%       | 5%        | MSFT     | 36%       | 36%       | 22%       |
| AAPL     | Net Investment Purchase And Sale                           | -1%       | -2%       | 211%      | MSFT     | 7%        | 2%        | 76%       |
| AAPL     | Cash Flow From Continuing Investing Activities             | -4%       | -6%       | 54%       | MSFT     | -40%      | -16%      | 328%      |
| AAPL     | Investing Cash Flow                                        | -4%       | -6%       | 54%       | MSFT     | -40%      | -16%      | 328%      |
| AAPL     | Issuance Of Debt                                           | 6%        | 1%        | -73%      | MSFT     | 12%       |           | inf%      |
| AAPL     | Long Term Debt Issuance                                    | 6%        | 1%        | -73%      | MSFT     | 10%       |           | inf%      |
|          | Short Term Debt Issuance                                   |           |           |           | MSFT     | 2%        |           | inf%      |
| AAPL     | Net Short Term Debt Issuance                               | 0%        | 1%        | 287%      | MSFT     | 2%        |           | inf%      |
| AAPL     | Net Long Term Debt Issuance                                | 3%        | -1%       | -135%     | MSFT     | -2%       | -2%       | 70%       |
| AAPL     | Issuance Of Capital Stock                                  | 0%        |           |           | MSFT     | 1%        | 1%        | 7%        |
| AAPL     | Common Stock Issuance                                      | 0%        |           |           | MSFT     | 1%        | 1%        | 7%        |
| AAPL     | Repayment Of Debt                                          | -2%       | -2%       | 9%        | MSFT     | -12%      | -2%       | 957%      |
| AAPL     | Long Term Debt Payments                                    | -2%       | -2%       | 9%        | MSFT     | -12%      | -2%       | 957%      |
| AAPL     | Net Issuance Payments Of Debt                              | 3%        | 0%        | -101%     | MSFT     | 0%        | -2%       | -121%     |
| AAPL     | Common Stock Payments                                      | -24%      | -23%      | 4%        | MSFT     | -7%       | -16%      | -22%      |
| AAPL     | Cash Dividends Paid                                        | -4%       | -4%       | 3%        | MSFT     | -9%       | -10%      | 10%       |
| AAPL     | Capital Expenditure                                        | -3%       | -3%       | -3%       | MSFT     | -18%      | -12%      | 58%       |
| AAPL     | Repurchase Of Capital Stock                                | -24%      | -23%      | 4%        | MSFT     | -7%       | -16%      | -22%      |
| AAPL     | Net Common Stock Issuance                                  | -24%      | -23%      | 4%        | MSFT     | -6%       | -15%      | -25%      |
| AAPL     | Net Other Financing Charges                                | -2%       | -2%       | 14%       | MSFT     | -1%       | -2%       | 30%       |
| AAPL     | Financing Cash Flow                                        | -26%      | -28%      | 19%       | MSFT     | -15%      | -29%      | -14%      |
| AAPL     | Cash Flow From Continuing Financing Activities             | -26%      | -28%      | 19%       | MSFT     | -15%      | -29%      | -14%      |
| AAPL     | Beginning Cash Position                                    | 11%       | 9%        | -10%      | MSFT     | 14%       | 8%        | 149%      |
| AAPL     | Net Other Investing Changes                                | 0%        | -1%       | 442%      | MSFT     | -1%       | -1%       | -58%      |
| AAPL     | End Cash Position                                          | 10%       | 6%        | -30%      | MSFT     | 7%        | 8%        | -47%      |
| AAPL     | Changes In Cash                                            | -1%       | -3%       | 184%      | MSFT     | -7%       | 0%        | -177%     |
| AAPL     | Change In Cash Supplemental As Reported                    | -1%       | -3%       | 184%      | MSFT     | -7%       | 0%        | -179%     |
|          | Effect Of Exchange Rate Changes                            |           |           |           | MSFT     | 0%        | 0%        | 8%        |
| AAPL     | Free Cash Flow                                             | 25%       | 28%       | 20%       | MSFT     | 30%       | 33%       | 25%       |
| AAPL     | Other Non Cash Items                                       | -1%       | 0%        | -120%     |          |           |           |           |
| AAPL     | Common Stock Dividend Paid                                 | -4%       | -4%       | 3%        | MSFT     | -9%       | -10%      | 10%       |
| AAPL     | Total Revenue                                              | 100%      | 100%      | 8%        | MSFT     | 100%      | 100%      | 16%       |
| AAPL     | Operating Revenue                                          | 100%      | 100%      | 8%        | MSFT     | 100%      | 100%      | 16%       |
| AAPL     | Cost Of Revenue                                            | 58%       | 57%       | 5%        | MSFT     | 30%       | 31%       | 13%       |
| AAPL     | Reconciled Cost Of Revenue                                 | 58%       | 57%       | 5%        | MSFT     | 30%       | 31%       | 13%       |
| AAPL     | Gross Profit                                               | 42%       | 43%       | 12%       | MSFT     | 70%       | 69%       | 17%       |
| AAPL     | Research And Development                                   | 6%        | 7%        | 20%       | MSFT     | 12%       | 12%       | 9%        |
|          | Selling And Marketing Expense                              |           |           |           | MSFT     | 10%       | 12%       | 7%        |
| AAPL     | Selling General And Administration                         | 6%        | 6%        | 14%       | MSFT     | 13%       | 15%       | 6%        |
|          | General And Administrative Expense                         |           |           |           | MSFT     | 3%        | 3%        | 0%        |
| AAPL     | Reconciled Depreciation                                    | 3%        | 3%        | -2%       | MSFT     | 9%        | 7%        | 61%       |
| AAPL     | Operating Expense                                          | 12%       | 13%       | 17%       | MSFT     | 25%       | 27%       | 7%        |
| AAPL     | EBIT                                                       | 31%       | 30%       | 7%        | MSFT     | 45%       | 44%       | 21%       |
| AAPL     | Operating Income                                           | 30%       | 30%       | 10%       | MSFT     | 45%       | 42%       | 24%       |
| AAPL     | Interest Income                                            | 1%        | 1%        | -1%       | MSFT     | 1%        | 1%        | 5%        |
| AAPL     | Interest Income Non Operating                              | 1%        | 1%        | -1%       | MSFT     | 1%        | 1%        | 5%        |
| AAPL     | Interest Expense                                           | 1%        | 1%        | 11%       | MSFT     | 1%        | 1%        | 49%       |
| AAPL     | Interest Expense Non Operating                             | 1%        | 1%        | 11%       | MSFT     | 1%        | 1%        | 49%       |
| AAPL     | Net Interest Income                                        | 0%        | 0%        | -154%     | MSFT     | 0%        | 0%        | -78%      |
| AAPL     | Net Non Operating Interest Income Expense                  | 0%        | 0%        | -154%     | MSFT     | 0%        | 0%        | -78%      |
| AAPL     | Other Income Expense                                       | 0%        | 0%        | -657%     | MSFT     | -1%       | 1%        | 685%      |
| AAPL     | Other Non Operating Income Expenses                        | 0%        | 0%        | -657%     | MSFT     | -1%       | 0%        | 491%      |
|          | Gain On Sale Of Security                                   |           |           |           | MSFT     | 0%        | 1%        | -2387%    |
| AAPL     | Pretax Income                                              | 30%       | 30%       | 9%        | MSFT     | 44%       | 42%       | 21%       |
| AAPL     | Tax Provision                                              | 4%        | 5%        | 33%       | MSFT     | 8%        | 6%        | 16%       |
| AAPL     | Tax Effect Of Unusual Items                                | 0%        | 0%        |           | MSFT     | 0%        | 0%        | 3406%     |
| AAPL     | Tax Rate For Calcs                                         | 0%        | 0%        | 22%       | MSFT     | 0%        | 0%        | -4%       |
| AAPL     | Net Income                                                 | 26%       | 25%       | 5%        | MSFT     | 36%       | 36%       | 22%       |
| AAPL     | Net Income Common Stockholders                             | 26%       | 25%       | 5%        | MSFT     | 36%       | 36%       | 22%       |
| AAPL     | Net Income Continuous Operations                           | 26%       | 25%       | 5%        | MSFT     | 36%       | 36%       | 22%       |
| AAPL     | Net Income From Continuing And Discontinued Operation      | 26%       | 25%       | 5%        | MSFT     | 36%       | 36%       | 22%       |
| AAPL     | Net Income From Continuing Operation Net Minority Interest | 26%       | 25%       | 5%        | MSFT     | 36%       | 36%       | 22%       |
| AAPL     | Net Income Including Noncontrolling Interests              | 26%       | 25%       | 5%        | MSFT     | 36%       | 36%       | 22%       |
| AAPL     | Normalized Income                                          | 26%       | 25%       | 5%        | MSFT     | 36%       | 36%       | 22%       |
| AAPL     | Diluted NIAvailto Com Stockholders                         | 26%       | 25%       | 5%        | MSFT     | 36%       | 36%       | 22%       |
| AAPL     | Basic EPS                                                  | 0%        | 0%        | 8%        | MSFT     | 0%        | 0%        | 22%       |
| AAPL     | Diluted EPS                                                | 0%        | 0%        | 9%        | MSFT     | 0%        | 0%        | 22%       |
| AAPL     | Basic Average Shares                                       | 5%        | 4%        | -3%       | MSFT     | 3%        | 4%        | 0%        |
| AAPL     | Diluted Average Shares                                     | 5%        | 4%        | -3%       | MSFT     | 3%        | 5%        | 0%        |
| AAPL     | EBITDA                                                     | 34%       | 33%       | 6%        | MSFT     | 54%       | 51%       | 27%       |
| AAPL     | Normalized EBITDA                                          | 34%       | 33%       | 6%        | MSFT     | 54%       | 50%       | 27%       |
| AAPL     | Total Expenses                                             | 70%       | 70%       | 7%        | MSFT     | 55%       | 58%       | 10%       |
| AAPL     | Total Operating Income As Reported                         | 30%       | 30%       | 10%       | MSFT     | 45%       | 42%       | 24%       |
|          | Special Income Charges                                     |           |           |           | MSFT     | 0%        | 0%        | 587%      |
|          | Write Off                                                  |           |           |           | MSFT     | 0%        | 0%        | 587%      |
|          | Total Unusual Items                                        |           |           |           | MSFT     | 0%        | 1%        | 3560%     |
|          | Total Unusual Items Excluding Goodwill                     |           |           |           | MSFT     | 0%        | 1%        | 3560%     |
|          | Other Gand A                                               |           |           |           | MSFT     | 3%        | 3%        | 0%        |

The 'fistres' columns refer to the percentagers respect to the revenue for that year for that company. 'chgn' represents the change from year to year, since we consider only 4 years, only 3 year changes are calculated. None of these two companies were chosen and they serve here as an example.

Our approach to make companies more comparable is to present all financial data in terms of the percentage respect to the total revenue ( as shown in Fig. 1). 

There are other requirements with many projections like free cash flow and stock price and return on investment in the comming 10 years. Thinking this is Buffett method is controversial. Therefore, we stop here. We just want to identify a bunch of good companies based in these basic numbers. This is wider accepted, i.e. a company with low debt, with hight ROE, and with strong margins and low capital expenditure is a good company. Other aspects are less numerical, like re-investment oportunities or protective moat. This wont be quantified.

Notice additionally, that we rely on yahoo, as it provide us with already standardize data, but we need at least 10 years of financials, or we may be interested in small or unknown companies requiring finacial standardization, just to be able to fee the data into the model.

#### Finding companies with strong financials from the Russell 2000

There were about 10 companies that were selected based on the financial research using Reese approach with our limitations (hereup exposed). These companies are TH, MATX, HDSN, MCRI, IDCC, SHLS, MTH, KAI, FWRD, DIOD. 
The idea is thus to use this and selected companies to define what is a healthy company. About 10 companies where selected: DIOD EVRI FWRD GRBK HCKT HDSN IDCC JBI KAI MATX MCRI METCB MHO MTH NRC SHLS TH UHG XPEL. The approach to chosing these companies was by means of stability in their earnings, retained earnings, low debt, positive operating earnings and operating cashflow. The following table show the type of comparative tables that were calculated. all the values have beeing divided by its corresponding revenue for each company. This type of analysis is more interesting when considering two companies from the same industry. 

### Cosine Distance calculations


Table 2. Consine distance calculations between pairs of companies. Units ranging from -100 to +100
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


#### Cosine Distance correlations

The following is a simple method to look for companies with simmilar financials. Comparing by glancing all financials, is complicated, thus the first step is to identify companies with strong correlation, then after, check both companies financials one next the other. Notice this is an interesting metric to check this company accross different years. It can be seeng that MSFT is estable accross years.

Fig. 3 Cosine Distance calculations for Microsoft (Wide MOAT by Morningstar). Values close to 1 or -1 indicate high correlation

| subjid | fidtc     | afidtc                      | aval        |
|--------|-----------|-----------------------------|-------------|
| MSFT   | 6/30/2021 | MSFT_2021-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2021 | MSFT_2022-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2021 | MSFT_2023-06-30 00:00:00    | 0.983124175 |
| MSFT   | 6/30/2021 | MSFT_2022-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2021 | MSFT_2022-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2021 | MSFT_2023-06-30 00:00:00    | 0.983124175 |
| MSFT   | 6/30/2021 | MSFT_2021-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2021 | MSFT_2023-06-30 00:00:00    | 0.983124175 |
| MSFT   | 6/30/2021 | MSFT_2022-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2021 | MSFT_2021-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2021 | MSFT_2022-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2021 | MSFT_2023-06-30 00:00:00    | 0.983124175 |
| MSFT   | 6/30/2021 | MSFT_2022-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2021 | MSFT_2021-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2021 | MSFT_2022-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2021 | MSFT_2021-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2022 | CSCO_2021-07-31 00:00:00    | 0.923528878 |
| MSFT   | 6/30/2022 | CSCO_2022-07-31 00:00:00    | 0.919733387 |
| MSFT   | 6/30/2022 | CSCO_2023-07-31 00:00:00    | 0.929876097 |
| MSFT   | 6/30/2022 | MSFT_2023-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2022 | 0HAU.IL_2023-12-31 00:00:00 | 0.909507882 |
| MSFT   | 6/30/2023 | MSFT_2021-06-30 00:00:00    | 0.983124175 |
| MSFT   | 6/30/2023 | MSFT_2022-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2023 | MSFT_2023-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2023 | MSFT_2024-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2023 | MSFT_2022-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2023 | MSFT_2023-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2023 | MSFT_2024-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2023 | MSFT_2022-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2023 | WST_2020-12-31 00:00:00     | 0.91001617  |
| MSFT   | 6/30/2023 | WST_2021-12-31 00:00:00     | 0.915011788 |
| MSFT   | 6/30/2023 | WST_2022-12-31 00:00:00     | 0.903896986 |
| MSFT   | 6/30/2023 | WNS_2021-03-31 00:00:00     | 0.907749207 |
| MSFT   | 6/30/2023 | MSFT_2023-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2023 | MSFT_2024-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2023 | MSFT_2024-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2023 | VACNY_2021-12-31 00:00:00   | 0.902788832 |
| MSFT   | 6/30/2023 | VACNY_2022-12-31 00:00:00   | 0.909853358 |
| MSFT   | 6/30/2023 | MSFT_2024-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2023 | MSFT_2023-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2023 | TCEHY_2021-12-31 00:00:00   | 0.901678819 |
| MSFT   | 6/30/2023 | TCEHY_2022-12-31 00:00:00   | 0.902072643 |
| MSFT   | 6/30/2023 | TCEHY_2023-12-31 00:00:00   | 0.902082047 |
| MSFT   | 6/30/2023 | SPXSF_2020-12-31 00:00:00   | 0.909236593 |
| MSFT   | 6/30/2023 | SPXSF_2021-12-31 00:00:00   | 0.929186577 |
| MSFT   | 6/30/2023 | MSFT_2024-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2023 | SPXCY_2024-06-30 00:00:00   | 0.904743534 |
| MSFT   | 6/30/2023 | MSFT_2024-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2023 | SNPS_2021-10-31 00:00:00    | 0.905166832 |
| MSFT   | 6/30/2023 | SNPS_2022-10-31 00:00:00    | 0.9067381   |
| MSFT   | 6/30/2023 | SNPS_2023-10-31 00:00:00    | 0.918874162 |
| MSFT   | 6/30/2023 | MSFT_2023-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2023 | MSFT_2024-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2023 | SDMHF_2021-12-31 00:00:00   | 0.906549333 |
| MSFT   | 6/30/2023 | SDMHF_2022-12-31 00:00:00   | 0.909336094 |
| MSFT   | 6/30/2023 | SAUHF_2021-12-31 00:00:00   | 0.924538649 |
| MSFT   | 6/30/2023 | SAUHF_2022-12-31 00:00:00   | 0.920335422 |
| MSFT   | 6/30/2023 | SAUHF_2023-12-31 00:00:00   | 0.900769631 |
| MSFT   | 6/30/2024 | ALFVY_2021-12-31 00:00:00   | 0.907530382 |
| MSFT   | 6/30/2024 | 0HAU.IL_2022-12-31 00:00:00 | 0.907854378 |
| MSFT   | 6/30/2024 | 0HAU.IL_2023-12-31 00:00:00 | 0.922742729 |
| MSFT   | 9/30/2024 | MSFT_2024-09-30 00:00:00    | 1           |
| MSFT   | 9/30/2024 | MSFT_2024-09-30 00:00:00    | 1           |
| MSFT   | 9/30/2024 | MSFT_2024-09-30 00:00:00    | 1           |
| MSFT   | 9/30/2024 | MSFT_2024-09-30 00:00:00    | 1           |
| MSFT   | 6/30/2021 | MSFT_2021-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2021 | MSFT_2022-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2021 | MSFT_2023-06-30 00:00:00    | 0.983124175 |
| MSFT   | 6/30/2021 | MSFT_2024-06-30 00:00:00    | 0.95183581  |
| MSFT   | 6/30/2021 | MSFT_2022-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2021 | MSFT_2024-06-30 00:00:00    | 0.95183581  |
| MSFT   | 6/30/2021 | MSFT_2024-06-30 00:00:00    | 0.95183581  |
| MSFT   | 6/30/2022 | SDMHF_2021-12-31 00:00:00   | 0.90473477  |
| MSFT   | 6/30/2022 | SDMHF_2022-12-31 00:00:00   | 0.908587358 |
| MSFT   | 6/30/2022 | SAUHF_2021-12-31 00:00:00   | 0.907654234 |
| MSFT   | 6/30/2022 | SAUHF_2022-12-31 00:00:00   | 0.902080065 |
| MSFT   | 6/30/2022 | MSFT_2021-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2022 | MSFT_2022-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2022 | MSFT_2023-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2022 | MSFT_2021-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2022 | MSFT_2023-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2022 | MSFT_2023-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2022 | MSFT_2021-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2022 | MSFT_2023-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2022 | MSFT_2022-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2022 | MSFT_2021-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2022 | MSFT_2021-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2022 | MSFT_2021-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2022 | MSFT_2022-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2022 | MSFT_2021-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2022 | MSFT_2023-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2022 | GOOGL_2020-12-31 00:00:00   | 0.901503196 |
| MSFT   | 6/30/2022 | GOOGL_2021-12-31 00:00:00   | 0.923634822 |
| MSFT   | 6/30/2022 | GOOGL_2022-12-31 00:00:00   | 0.920059409 |
| MSFT   | 6/30/2022 | GOOGL_2023-12-31 00:00:00   | 0.924739929 |
| MSFT   | 6/30/2023 | MSFT_2022-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2023 | 0HAU.IL_2023-12-31 00:00:00 | 0.912476676 |
| MSFT   | 6/30/2024 | MSFT_2021-06-30 00:00:00    | 0.95183581  |
| MSFT   | 6/30/2024 | MSFT_2022-06-30 00:00:00    | 0.977242401 |
| MSFT   | 6/30/2024 | MSFT_2023-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2024 | MSFT_2024-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2024 | MSFT_2021-06-30 00:00:00    | 0.95183581  |
| MSFT   | 6/30/2024 | MSFT_2023-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2024 | MSFT_2022-06-30 00:00:00    | 0.977242401 |
| MSFT   | 6/30/2024 | WNS_2023-03-31 00:00:00     | 0.901181378 |
| MSFT   | 6/30/2024 | MSFT_2023-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2024 | MSFT_2024-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2024 | MSFT_2021-06-30 00:00:00    | 0.95183581  |
| MSFT   | 6/30/2024 | MSFT_2022-06-30 00:00:00    | 0.977242401 |
| MSFT   | 6/30/2024 | MSFT_2023-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2024 | VACNY_2021-12-31 00:00:00   | 0.908758226 |
| MSFT   | 6/30/2024 | VACNY_2022-12-31 00:00:00   | 0.907756874 |
| MSFT   | 6/30/2024 | MSFT_2024-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2024 | TROW_2021-12-31 00:00:00    | 0.904754999 |
| MSFT   | 6/30/2024 | TROW_2022-12-31 00:00:00    | 0.901110338 |
| MSFT   | 6/30/2024 | MSFT_2023-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2024 | MSFT_2024-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2024 | MSFT_2024-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2024 | TCEHY_2020-12-31 00:00:00   | 0.901032449 |
| MSFT   | 6/30/2024 | TCEHY_2021-12-31 00:00:00   | 0.901260928 |
| MSFT   | 6/30/2024 | SPXSF_2020-12-31 00:00:00   | 0.910361131 |
| MSFT   | 6/30/2024 | SPXSF_2021-12-31 00:00:00   | 0.92600078  |
| MSFT   | 6/30/2024 | MSFT_2023-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2024 | MSFT_2023-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2024 | SNPS_2021-10-31 00:00:00    | 0.918509602 |
| MSFT   | 6/30/2024 | SNPS_2022-10-31 00:00:00    | 0.922752901 |
| MSFT   | 6/30/2024 | SNPS_2023-10-31 00:00:00    | 0.927098313 |
| MSFT   | 6/30/2024 | MSFT_2023-06-30 00:00:00    | 0.97960211  |
| MSFT   | 6/30/2024 | MSFT_2024-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2024 | SDMHF_2020-12-31 00:00:00   | 0.926290643 |
| MSFT   | 6/30/2024 | SDMHF_2021-12-31 00:00:00   | 0.916633088 |
| MSFT   | 6/30/2024 | SDMHF_2022-12-31 00:00:00   | 0.932074912 |
| MSFT   | 6/30/2024 | SAUHF_2021-12-31 00:00:00   | 0.901106016 |
| MSFT   | 6/30/2024 | SAUHF_2022-12-31 00:00:00   | 0.914796755 |
| MSFT   | 6/30/2024 | SAUHF_2023-12-31 00:00:00   | 0.901997354 |
| MSFT   | 6/30/2024 | SAP_2020-12-31 00:00:00     | 0.904005671 |
| MSFT   | 6/30/2024 | SAP_2021-12-31 00:00:00     | 0.90516251  |
| MSFT   | 6/30/2024 | SAP_2023-12-31 00:00:00     | 0.900639503 |
| MSFT   | 9/30/2024 | MSCI_2024-09-30 00:00:00    | 0.960457342 |
| MSFT   | 6/30/2021 | GOOGL_2020-12-31 00:00:00   | 0.91158297  |
| MSFT   | 6/30/2021 | GOOGL_2021-12-31 00:00:00   | 0.924261543 |
| MSFT   | 6/30/2021 | GOOGL_2022-12-31 00:00:00   | 0.910456037 |
| MSFT   | 6/30/2021 | GOOGL_2023-12-31 00:00:00   | 0.912229815 |
| MSFT   | 6/30/2021 | CSCO_2021-07-31 00:00:00    | 0.918503062 |
| MSFT   | 6/30/2021 | CSCO_2022-07-31 00:00:00    | 0.910786938 |
| MSFT   | 6/30/2021 | CSCO_2023-07-31 00:00:00    | 0.92415394  |
| MSFT   | 6/30/2022 | MSFT_2021-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2022 | MSFT_2022-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2022 | MSFT_2023-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2022 | MSFT_2024-06-30 00:00:00    | 0.977242401 |
| MSFT   | 6/30/2022 | MSFT_2021-06-30 00:00:00    | 0.99165834  |
| MSFT   | 6/30/2022 | MSFT_2023-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2022 | MSFT_2022-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2022 | MSFT_2023-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2022 | MSFT_2024-06-30 00:00:00    | 0.977242401 |
| MSFT   | 6/30/2022 | MSFT_2024-06-30 00:00:00    | 0.977242401 |
| MSFT   | 6/30/2022 | SPXSF_2020-12-31 00:00:00   | 0.903450438 |
| MSFT   | 6/30/2022 | SPXSF_2021-12-31 00:00:00   | 0.918380057 |
| MSFT   | 6/30/2022 | SNPS_2023-10-31 00:00:00    | 0.902597962 |
| MSFT   | 6/30/2023 | RMD_2022-06-30 00:00:00     | 0.900370632 |
| MSFT   | 6/30/2023 | RMD_2024-06-30 00:00:00     | 0.90193908  |
| MSFT   | 6/30/2023 | NVZMY_2022-12-31 00:00:00   | 0.905946827 |
| MSFT   | 6/30/2023 | MSFT_2023-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2023 | MSFT_2021-06-30 00:00:00    | 0.983124175 |
| MSFT   | 6/30/2023 | MSFT_2022-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2023 | MSFT_2023-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2023 | MSFT_2022-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2023 | MSFT_2022-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2023 | MSFT_2022-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2023 | MSFT_2021-06-30 00:00:00    | 0.983124175 |
| MSFT   | 6/30/2023 | MSFT_2023-06-30 00:00:00    | 1           |
| MSFT   | 6/30/2023 | MSFT_2021-06-30 00:00:00    | 0.983124175 |
| MSFT   | 6/30/2023 | MSFT_2021-06-30 00:00:00    | 0.983124175 |
| MSFT   | 6/30/2023 | MSFT_2022-06-30 00:00:00    | 0.992611034 |
| MSFT   | 6/30/2023 | GOOGL_2020-12-31 00:00:00   | 0.924283774 |
| MSFT   | 6/30/2023 | GOOGL_2021-12-31 00:00:00   | 0.937720786 |
| MSFT   | 6/30/2023 | GOOGL_2022-12-31 00:00:00   | 0.936384212 |
| MSFT   | 6/30/2023 | GOOGL_2023-12-31 00:00:00   | 0.942875197 |
| MSFT   | 6/30/2023 | DIOD_2022-12-31 00:00:00    | 0.900222413 |
| MSFT   | 6/30/2023 | CSCO_2021-07-31 00:00:00    | 0.910000719 |
| MSFT   | 6/30/2023 | CSCO_2022-07-31 00:00:00    | 0.905681498 |
| MSFT   | 6/30/2023 | CSCO_2023-07-31 00:00:00    | 0.920824988 |
| MSFT   | 6/30/2024 | RMD_2021-06-30 00:00:00     | 0.912972474 |
| MSFT   | 6/30/2024 | RMD_2022-06-30 00:00:00     | 0.909564433 |
| MSFT   | 6/30/2024 | RMD_2023-06-30 00:00:00     | 0.914244502 |
| MSFT   | 6/30/2024 | RMD_2024-06-30 00:00:00     | 0.916089475 |
| MSFT   | 6/30/2024 | NVZMY_2021-12-31 00:00:00   | 0.903976544 |
| MSFT   | 6/30/2024 | NVZMY_2022-12-31 00:00:00   | 0.911266024 |
| MSFT   | 6/30/2024 | NVZMY_2023-12-31 00:00:00   | 0.904759531 |
| MSFT   | 6/30/2024 | MATX_2022-12-31 00:00:00    | 0.900810993 |
| MSFT   | 6/30/2024 | KAI_2022-12-31 00:00:00     | 0.90412923  |
| MSFT   | 6/30/2024 | KAI_2023-12-31 00:00:00     | 0.904817081 |
| MSFT   | 6/30/2024 | GOOGL_2021-12-31 00:00:00   | 0.906209496 |
| MSFT   | 6/30/2024 | GOOGL_2022-12-31 00:00:00   | 0.914206678 |
| MSFT   | 6/30/2024 | GOOGL_2023-12-31 00:00:00   | 0.919846395 |
| MSFT   | 6/30/2024 | CSCO_2021-07-31 00:00:00    | 0.906108349 |
| MSFT   | 6/30/2024 | CSCO_2023-07-31 00:00:00    | 0.907932684 |

This is the Cosine distance for MSFT with other companies. The companies with economics simmilar to MSFT are GOOGL, CSCO, RMD, NVZMY, VACNY, TCEHY, SPXSF, SPXCY, SNPS, SAUHF, RMD, DIOD, MATX, KAI, SAP, TROW, 0HAU.IL. To have a better overview, take a look at the following table indicating the number of counts acros the years.

Fig. 4 Table of frequencies of counts on which Cosine Distance > 0.8 or < -0.8 for MSFT

| subjid1     | 6/30/2021 0:00 | 6/30/2022 0:00 | 6/30/2023 0:00 | 6/30/2024 0:00 | 9/30/2024 0:00 |
|-------------|----------------|----------------|----------------|----------------|----------------|
|             |                |                |                |                |                |
| 0HAU.IL     | 4              | 4              | 4              | 4              |                |
| 0NWV.IL     | 4              | 4              | 4              | 4              |                |
| 6268.T      | 3              | 4              | 4              | 4              |                |
| AAPL        | 4              | 4              | 4              | 2              |                |
| ALFVY       | 4              | 4              | 4              | 4              |                |
| AME         | 1              | 4              | 4              | 4              | 1              |
| ANSS        |                | 4              | 4              | 4              |                |
| APH         | 4              | 4              | 4              | 4              |                |
| BABA        | 4              | 4              | 4              | 4              |                |
| CBCFF       | 3              | 3              | 4              | 4              |                |
| CSCO        | 4              | 4              | 4              | 4              |                |
| DANOY       | 4              | 4              | 4              | 4              |                |
| DEO         | 4              | 4              | 3              | 4              |                |
| DIOD        | 4              | 4              | 4              | 4              |                |
| EKTAY       | 4              | 4              | 4              | 4              |                |
| GMWKF       | 4              | 4              | 4              | 4              |                |
| GOOGL       | 4              | 4              | 4              | 4              | 1              |
| GVDBF       | 3              | 4              | 4              | 4              |                |
| HDSN        | 2              | 2              | 2              | 2              |                |
| HSY         | 4              | 4              | 4              | 4              | 1              |
| INFY        | 4              | 4              | 4              | 3              |                |
| IVU.DE      | 4              | 4              | 4              | 2              |                |
| KAI         | 4              | 4              | 4              | 4              |                |
| KAO.F       | 4              | 4              | 4              | 4              |                |
| LANC        |                |                | 1              |                |                |
| LGRVF       | 4              | 4              | 4              | 4              |                |
| LRLCF       | 4              | 4              | 4              | 4              |                |
| LTOUF       | 4              | 4              | 4              |                |                |
| MANH        | 4              | 4              | 4              | 1              | 1              |
| MASI        | 3              | 3              | 3              | 4              |                |
| MATX        | 3              | 3              | 3              | 4              |                |
| MCRI        |                | 1              | 4              | 4              |                |
| MKC         |                | 1              |                | 4              |                |
| MKTX        | 4              | 4              | 4              | 4              | 1              |
| MNST        | 2              | 3              | 4              | 3              |                |
| MPWR        | 4              | 4              | 4              | 4              |                |
| MRK         | 2              | 4              | 4              | 4              | 1              |
| MSFT        | 23             | 26             | 30             | 20             | 4              |
| NDSN        | 2              | 3              | 3              | 4              |                |
| NJDCY       | 3              | 4              | 4              | 4              |                |
| NKE         | 4              | 4              | 4              |                |                |
| NOC         | 2              | 4              | 3              | 3              |                |
| NOW         | 4              | 4              | 4              | 3              |                |
| NVDA        | 3              | 3              | 3              | 2              | 1              |
| NVS         | 4              | 4              | 4              | 4              |                |
| NVZMY       | 4              | 4              | 4              | 4              |                |
| OLCLY       | 1              | 1              | 2              | 2              |                |
| OLTH.AT     | 4              | 4              | 4              | 4              |                |
| PAYX        | 2              | 2              | 2              |                |                |
| PGPHF       | 4              | 4              | 4              | 2              |                |
| PLZL.ME     | 3              | 3              | 3              | 3              | 1              |
| PUODY       | 4              | 4              | 4              | 4              |                |
| QLYS        | 4              | 3              | 3              | 2              | 1              |
| RCRRF       | 2              | 3              | 4              | 3              |                |
| REA.AX      |                | 1              | 3              | 4              |                |
| REC.MI      | 2              | 3              | 2              | 4              | 1              |
| RELIANCE.NS | 4              | 4              | 4              | 4              |                |
| RMD         | 4              | 4              | 4              | 4              | 1              |
| ROK         | 1              | 1              | 1              | 3              |                |
| ROL         | 3              | 4              | 4              | 4              |                |
| SAFRY       | 3              | 3              | 3              | 3              |                |
| SAP         | 4              | 4              | 4              | 4              |                |
| SAUHF       | 4              | 4              | 4              | 4              |                |
| SBGSY       | 4              | 4              | 4              | 4              |                |
| SCCO        | 4              | 4              | 4              | 4              | 1              |
| SDMHF       | 3              | 3              | 3              | 3              |                |
| SEIC        | 4              | 4              | 4              | 4              | 1              |
| SGIOY       | 2              | 1              | 4              | 2              |                |
| SHLS        | 1              | 1              | 1              | 1              |                |
| SHZHY       | 4              | 4              | 4              | 4              |                |
| SKFOF       | 3              | 4              | 4              | 4              |                |
| SNPS        | 4              | 4              | 4              | 4              |                |
| SONVY       | 4              | 4              | 4              | 4              |                |
| SPXCY       | 4              | 4              | 4              | 4              |                |
| SPXSF       | 4              | 4              | 4              | 4              |                |
| SSDOY       | 2              | 4              | 4              | 4              |                |
| SYIEY       | 4              | 4              | 4              | 4              |                |
| SYK         | 4              | 4              | 4              | 4              |                |
| TCEHY       | 4              | 4              | 4              | 4              |                |
| TGYM.MI     | 4              | 4              | 4              | 4              |                |
| TH          | 1              | 2              | 2              | 2              | 1              |
| TROW        | 4              | 4              | 4              | 4              | 1              |
| TTC         | 4              | 4              | 4              | 4              |                |
| UNICY       | 4              | 4              | 4              | 4              |                |
| V           | 4              | 4              | 4              | 4              |                |
| VACNY       | 4              | 4              | 4              | 4              |                |
| VEEV        | 4              | 3              | 4              | 2              |                |
| WCN         |                | 3              | 3              | 4              |                |
| WDFC        | 1              | 2              | 2              | 1              |                |
| WEGE3.SA    | 4              | 4              | 4              | 4              |                |
| WNS         | 4              | 4              | 4              | 4              |                |
| WST         | 4              | 4              | 4              | 4              | 1              |
| XPEL        |                | 1              | 1              | 1              |                |
| ZTS         | 4              | 4              | 4              | 4              | 1              |



Many companies with financials close to MSFT.If you look at the financials, they are really close to each other in general (capital structure, debt ...). Notice that the Cosine do not weight any individual financial values, therefore each value has the same importance. In reality this is not true in the context of investing, one example is for instance than MSFT is more profitable and is more efficient in terms of expending. Further analysis might be weighting the financials according to imporance and growth, this is not done here, but this is an important exercise. If you have had this information 10 years ago and you had bought the cheper CSCO you would underperform notorously compared to MSFT. Aplhabet (GOOGL) is a good software company, as MSFT both companies have very similar financials, MSFT more profitable.

### Filtering data on highest ROI

Hereunder we present an approach to Free cash flow after controlling by stock based compensation. The reason to do this is that we believe compensating through stocks dilute the investor, thus it is a real cash expense. The problem by doing this is that we are penalizing high growth young companies that pay stock based in order to reduce employee costs. Additionally, we benefit companies with strong free cash flows, this is normally the case of already mature companies. 
Free Cash Flow = fcf
Stock Based Compensation = sbc
Total Assets = tas
Total Debt =  tde
Total Revenue = tre

Fig. 5 Table of Free Cash Flow after controlling by stock based compensation. Units in Millions

| subjid    | fidtc      | fiorresu | fcf     | sbc  | tas      | tde     | roi | tre      |
|-----------|------------|----------|---------|------|----------|---------|-----|----------|
| 600519.SS | 12/31/2020 | CNY      | 49579   | 0    | 213932   | 536     | 23  | 97993    |
| 600519.SS | 12/31/2021 | CNY      | 60620   | 0    | 255168   | 401     | 24  | 109464   |
| 600519.SS | 12/31/2023 | CNY      | 63973   | 0    | 272700   | 324     | 23  | 150560   |
| 603288.SS | 12/31/2020 | CNY      | 6043    | 0    | 29628    | 187     | 20  | 22792    |
| 603288.SS | 12/31/2021 | CNY      | 5293    | 0    | 33338    | 180     | 16  | 25004    |
| AAPL      | 9/30/2021  | USD      | 92953   | 791  | 351002   | 136522  | 26  | 365817   |
| AAPL      | 9/30/2023  | USD      | 99584   | 1083 | 352583   | 111088  | 28  | 383285   |
| AAPL      | 9/30/2024  | USD      | 108807  | 1169 | 364980   | 106629  | 29  | 391035   |
| AAPL      | 9/30/2022  | USD      | 111443  | 904  | 352755   | 132480  | 31  | 394328   |
| ABBV      | 12/31/2023 | USD      | 22062   | 75   | 134711   | 59385   | 16  | 54318    |
| ABBV      | 12/31/2022 | USD      | 24248   | 67   | 138805   | 63271   | 17  | 58054    |
| AMGN      | 12/31/2020 | USD      | 9889    | 33   | 62948    | 32986   | 16  | 25424    |
| AVGO      | 10/31/2021 | USD      | 13321   | 170  | 75570    | 39730   | 17  | 27450    |
| AVGO      | 10/31/2022 | USD      | 16312   | 153  | 73249    | 39515   | 22  | 33203    |
| AVGO      | 10/31/2023 | USD      | 17633   | 217  | 72861    | 39229   | 24  | 35819    |
| BKNG      | 12/31/2022 | USD      | 6186    | 40   | 25361    | 13037   | 24  | 17090    |
| BKNG      | 12/31/2023 | USD      | 6999    | 53   | 24342    | 14783   | 29  | 21365    |
| CHH       | 12/31/2021 | USD      | 306     | 4    | 1932     | 1108    | 16  | 1069     |
| CSCO      | 7/31/2023  | USD      | 19037   | 235  | 101852   | 8391    | 18  | 56998    |
| EXPD      | 12/31/2023 | USD      | 1014    | 6    | 4524     | 528     | 22  | 9300     |
| EXPD      | 12/31/2022 | USD      | 2043    | 6    | 5590     | 518     | 36  | 17071    |
| FWRD      | 12/31/2022 | USD      | 220     | 1    | 1208     | 267     | 18  | 1680     |
| GMKN.ME   | 12/31/2020 | USD      | 6380    | 0    | 20556    | 9826    | 31  | 15012    |
| GMKN.ME   | 12/31/2021 | USD      | 4278    | 0    | 23435    | 10461   | 18  | 17852    |
| GMWKF     | 5/31/2021  | GBP      | 103     | 0    | 282      | 47      | 36  | 370      |
| GMWKF     | 5/31/2022  | GBP      | 89      | 0    | 321      | 49      | 28  | 415      |
| GMWKF     | 5/31/2023  | GBP      | 164     | 0    | 327      | 50      | 50  | 471      |
| GMWKF     | 5/31/2024  | GBP      | 164     | 0    | 351      | 47      | 47  | 526      |
| GOOGL     | 12/31/2021 | USD      | 67012   | 1538 | 359268   | 28395   | 18  | 257637   |
| GOOGL     | 12/31/2022 | USD      | 60010   | 1936 | 365264   | 29679   | 16  | 282836   |
| GOOGL     | 12/31/2023 | USD      | 69495   | 2246 | 402392   | 28504   | 17  | 307394   |
| HD        | 1/31/2021  | USD      | 16376   | 31   | 70581    | 43422   | 23  | 132110   |
| HD        | 1/31/2022  | USD      | 14005   | 40   | 71876    | 46269   | 19  | 151157   |
| HD        | 1/31/2024  | USD      | 17946   | 38   | 76530    | 52243   | 23  | 152669   |
| HDSN      | 12/31/2023 | USD      | 55      | 0    | 297      | 7       | 18  | 289      |
| HDSN      | 12/31/2022 | USD      | 59      | 0    | 272      | 51      | 22  | 325      |
| HSY       | 12/31/2021 | USD      | 1587    | 7    | 10412    | 5376    | 15  | 8971     |
| HSY       | 12/31/2022 | USD      | 1808    | 7    | 10949    | 5118    | 16  | 10419    |
| IDXX      | 12/31/2020 | USD      | 540     | 3    | 2295     | 1003    | 23  | 2707     |
| IDXX      | 12/31/2021 | USD      | 636     | 4    | 2437     | 1031    | 26  | 3215     |
| IDXX      | 12/31/2023 | USD      | 773     | 6    | 3260     | 1067    | 24  | 3661     |
| INFY      | 3/31/2021  | USD      | 2973    | 4    | 14825    | 728     | 20  | 13561    |
| INFY      | 3/31/2022  | USD      | 3055    | 6    | 15555    | 722     | 20  | 16311    |
| INFY      | 3/31/2023  | USD      | 2534    | 6    | 15312    | 1010    | 17  | 18212    |
| INFY      | 3/31/2024  | USD      | 2882    | 8    | 16523    | 1002    | 17  | 18562    |
| IVU.DE    | 12/31/2020 | EUR      | 31      | 0    | 125      | 10      | 25  | 98       |
| LANC      | 6/30/2024  | USD      | 184     | 1    | 1207     | 58      | 15  | 1872     |
| LMT       | 12/31/2021 | USD      | 7699    | 23   | 50873    | 11670   | 15  | 67044    |
| LOW       | 1/31/2021  | USD      | 9258    | 16   | 46735    | 26211   | 20  | 89597    |
| LOW       | 1/31/2022  | USD      | 8260    | 23   | 44640    | 29384   | 18  | 96250    |
| LOW       | 1/31/2023  | USD      | 6760    | 22   | 43708    | 37994   | 15  | 97059    |
| LSTR      | 12/31/2023 | USD      | 368     | 0    | 1802     | 133     | 20  | 5303     |
| LSTR      | 12/31/2022 | USD      | 597     | 1    | 1932     | 196     | 31  | 7437     |
| MA        | 12/31/2020 | USD      | 6516    | 25   | 33584    | 12672   | 19  | 15301    |
| MA        | 12/31/2021 | USD      | 8649    | 27   | 37669    | 13901   | 23  | 18884    |
| MA        | 12/31/2022 | USD      | 10098   | 30   | 38724    | 14023   | 26  | 22237    |
| MA        | 12/31/2023 | USD      | 10892   | 46   | 42448    | 15681   | 26  | 25098    |
| MANH      | 12/31/2020 | USD      | 138     | 3    | 465      | 28      | 29  | 586      |
| MANH      | 12/31/2021 | USD      | 181     | 4    | 540      | 23      | 33  | 664      |
| MANH      | 12/31/2022 | USD      | 173     | 6    | 570      | 14      | 29  | 767      |
| MANH      | 12/31/2023 | USD      | 241     | 7    | 673      | 18      | 35  | 929      |
| MATX      | 12/31/2021 | USD      | 659     | 2    | 3693     | 1060    | 18  | 3925     |
| MATX      | 12/31/2022 | USD      | 1060    | 2    | 4330     | 911     | 24  | 4343     |
| MCO       | 12/31/2020 | USD      | 2043    | 15   | 12409    | 6943    | 16  | 5371     |
| MCRI      | 12/31/2023 | USD      | 124     | 1    | 681      | 20      | 18  | 501      |
| MELI      | 12/31/2022 | USD      | 2485    | 0    | 13736    | 5414    | 18  | 10537    |
| MELI      | 12/31/2023 | USD      | 4631    | 17   | 17646    | 5333    | 26  | 14473    |
| MKTX      | 12/31/2020 | USD      | 359     | 3    | 1331     | 94      | 27  | 689      |
| MNST      | 12/31/2020 | USD      | 1297    | 7    | 6203     |         | 21  | 4599     |
| MNST      | 12/31/2023 | USD      | 1483    | 7    | 9687     |         | 15  | 7140     |
| MPWR      | 12/31/2020 | USD      | 212     | 9    | 1208     | 3       | 17  | 844      |
| MPWR      | 12/31/2023 | USD      | 581     | 15   | 2434     | 6       | 23  | 1821     |
| MSCI      | 12/31/2020 | USD      | 760     | 5    | 4199     | 3519    | 18  | 1695     |
| MSCI      | 12/31/2021 | USD      | 883     | 5    | 5507     | 4311    | 16  | 2044     |
| MSCI      | 12/31/2022 | USD      | 1022    | 6    | 4998     | 4644    | 20  | 2249     |
| MSCI      | 12/31/2023 | USD      | 1145    | 7    | 5518     | 4628    | 21  | 2529     |
| MSFT      | 6/30/2021  | USD      | 56118   | 612  | 333779   | 67775   | 17  | 168088   |
| MSFT      | 6/30/2022  | USD      | 65149   | 750  | 364840   | 61270   | 18  | 198270   |
| NKE       | 5/31/2021  | USD      | 5962    | 61   | 37740    | 12813   | 16  | 44538    |
| NKE       | 5/31/2024  | USD      | 6617    | 80   | 38110    | 11952   | 17  | 51362    |
| NOW       | 12/31/2021 | USD      | 1799    | 113  | 10798    | 2214    | 16  | 5896     |
| NOW       | 12/31/2022 | USD      | 2173    | 140  | 13299    | 2232    | 15  | 7245     |
| NVDA      | 1/31/2021  | USD      | 4694    | 140  | 28791    | 7597    | 16  | 16675    |
| NVDA      | 1/31/2022  | USD      | 8132    | 200  | 44187    | 11831   | 18  | 26914    |
| NVDA      | 1/31/2024  | USD      | 27021   | 355  | 65728    | 11056   | 41  | 60922    |
| NVO       | 12/31/2020 | DKK      | 29870   | 82   | 144922   | 10356   | 21  | 126946   |
| NVO       | 12/31/2021 | DKK      | 47615   | 104  | 194508   | 26645   | 24  | 140800   |
| NVO       | 12/31/2022 | DKK      | 64134   | 154  | 241257   | 25784   | 27  | 176954   |
| NVO       | 12/31/2023 | DKK      | 70012   | 215  | 314486   | 27006   | 22  | 232261   |
| NVZMY     | 12/31/2020 | DKK      | 3415    | 5    | 20510    | 522     | 17  | 14012    |
| PAYX      | 5/31/2022  | USD      | 1456    | 5    | 9635     | 881     | 15  | 4612     |
| PAYX      | 5/31/2024  | USD      | 1736    | 6    | 10383    | 866     | 17  | 5278     |
| PGPHF     | 12/31/2020 | CHF      | 1124    | 6    | 4032     | 866     | 28  | 1382     |
| PGPHF     | 12/31/2022 | CHF      | 975     | 6    | 4576     | 1147    | 21  | 1814     |
| PII       | 12/31/2020 | USD      | 805     | 7    | 4633     | 1578    | 17  | 7028     |
| PLZL.ME   | 12/31/2021 | USD      | 1806    | 0    | 8011     | 3272    | 23  | 4966     |
| PLZL.ME   | 12/31/2020 | USD      | 2246    | 0    | 7295     | 3554    | 31  | 4998     |
| PLZL.ME   | 12/31/2023 | USD      | 1708    | 0    | 9284     | 8653    | 18  | 5436     |
| POOL      | 12/31/2020 | USD      | 376     | 1    | 1740     | 624     | 22  | 3937     |
| POOL      | 12/31/2023 | USD      | 828     | 2    | 3428     | 1364    | 24  | 5542     |
| QLYS      | 12/31/2020 | USD      | 149     | 4    | 737      | 57      | 20  | 363      |
| QLYS      | 12/31/2021 | USD      | 175     | 7    | 815      | 49      | 21  | 411      |
| QLYS      | 12/31/2022 | USD      | 175     | 5    | 701      | 42      | 24  | 490      |
| QLYS      | 12/31/2023 | USD      | 236     | 7    | 813      | 29      | 28  | 554      |
| RCRRF     | 3/31/2022  | JPY      | 375225  | 3245 | 2423542  | 271424  | 15  | 2871705  |
| REA.AX    | 6/30/2022  | AUD      | 393     | 0    | 2569     | 487     | 15  | 1427     |
| REA.AX    | 6/30/2024  | AUD      | 464     | 0    | 2655     | 281     | 17  | 1700     |
| RMD       | 6/30/2024  | USD      | 1286    | 8    | 6872     | 874     | 19  | 4685     |
| ROL       | 12/31/2020 | USD      | 413     | 2    | 1846     | 417     | 22  | 2161     |
| ROL       | 12/31/2021 | USD      | 375     | 1    | 2022     | 403     | 18  | 2424     |
| ROL       | 12/31/2022 | USD      | 435     | 2    | 2122     | 336     | 20  | 2696     |
| ROL       | 12/31/2023 | USD      | 496     | 2    | 2595     | 816     | 19  | 3073     |
| RTMVY     | 12/31/2020 | GBP      | 93      | 0    | 160      | 12      | 58  | 206      |
| RTMVY     | 12/31/2021 | GBP      | 194     | 0    | 108      | 11      | 180 | 305      |
| RTMVY     | 12/31/2022 | GBP      | 195     | 0    | 102      | 10      | 191 | 333      |
| RTMVY     | 12/31/2023 | GBP      | 203     | 1    | 105      | 7       | 193 | 364      |
| SCCO      | 12/31/2023 | USD      | 2564    | 0    | 16725    | 7030    | 15  | 9896     |
| SCCO      | 12/31/2021 | USD      | 3400    | 0    | 18298    | 7464    | 19  | 10934    |
| SCHYF     | 12/31/2023 | USD      | 2078    | 0    | 10258    | 8328    | 20  | 6534     |
| SEIC      | 12/31/2020 | USD      | 410     | 3    | 2167     | 43      | 19  | 1684     |
| SEIC      | 12/31/2021 | USD      | 581     | 4    | 2355     | 79      | 24  | 1918     |
| SEIC      | 12/31/2023 | USD      | 388     | 3    | 2520     | 25      | 15  | 1920     |
| SEIC      | 12/31/2022 | USD      | 492     | 4    | 2384     | 29      | 20  | 1991     |
| SHLS      | 12/31/2020 | USD      | 51      | 1    | 195      | 359     | 26  | 176      |
| SHW       | 12/31/2020 | USD      | 3105    | 10   | 20402    | 10114   | 15  | 18362    |
| SIRI      | 12/31/2020 | USD      | 1668    | 22   | 10333    | 8967    | 16  | 8040     |
| SIRI      | 12/31/2021 | USD      | 1610    | 20   | 10274    | 9243    | 15  | 8696     |
| SIRI      | 12/31/2022 | USD      | 1550    | 20   | 10022    | 9822    | 15  | 9003     |
| SNPS      | 10/31/2021 | USD      | 1397    | 35   | 8752     | 667     | 16  | 4204     |
| SNPS      | 10/31/2022 | USD      | 1600    | 46   | 9418     | 656     | 16  | 4616     |
| SPGI      | 12/31/2020 | USD      | 3491    | 9    | 12537    | 4754    | 28  | 7442     |
| SPGI      | 12/31/2021 | USD      | 3563    | 12   | 15026    | 4702    | 24  | 8297     |
| SPXCY     | 6/30/2021  | SGD      | 508     | 2    | 3023     | 539     | 17  | 1056     |
| TGR.BE    | 12/31/2020 | USD      | 1145    | 10   | 5852     | 11645   | 19  | 5652     |
| TGR.BE    | 12/31/2021 | USD      | 1476    | 8    | 5966     | 12127   | 25  | 6584     |
| TGR.BE    | 12/31/2022 | USD      | 1148    | 8    | 5846     | 12661   | 19  | 6842     |
| TGR.BE    | 12/31/2023 | USD      | 1318    | 10   | 6231     | 12031   | 21  | 7076     |
| TH        | 12/31/2022 | USD      | 165     | 2    | 772      | 355     | 21  | 502      |
| TMSNY     | 12/31/2021 | USD      | 358     | 4    | 2234     | 960     | 16  | 967      |
| TROW      | 12/31/2020 | USD      | 1704    | 25   | 10659    | 154     | 16  | 6207     |
| TROW      | 12/31/2022 | USD      | 2122    | 29   | 11643    | 330     | 18  | 6488     |
| TROW      | 12/31/2021 | USD      | 3213    | 27   | 12509    | 249     | 25  | 7672     |
| TTC       | 10/31/2021 | USD      | 452     | 2    | 2936     | 761     | 15  | 3960     |
| TXN       | 12/31/2020 | USD      | 5490    | 22   | 19351    | 7047    | 28  | 14461    |
| TXN       | 12/31/2021 | USD      | 6294    | 23   | 24676    | 8124    | 25  | 18344    |
| TXN       | 12/31/2022 | USD      | 5923    | 29   | 27207    | 8735    | 22  | 20028    |
| ULTA      | 1/31/2022  | USD      | 887     | 5    | 4764     | 1847    | 19  | 8631     |
| ULTA      | 1/31/2023  | USD      | 1170    | 4    | 5370     | 1903    | 22  | 10209    |
| ULTA      | 1/31/2024  | USD      | 1041    | 5    | 5707     | 1911    | 18  | 11207    |
| UNLRF     | 12/31/2023 | IDR      | 6283060 | 0    | 16664086 | 750783  | 38  | 38611401 |
| UNLRF     | 12/31/2021 | IDR      | 7215364 | 0    | 19068532 | 2736866 | 38  | 39545959 |
| UNLRF     | 12/31/2022 | IDR      | 7422951 | 0    | 18318114 | 1284026 | 41  | 41218881 |
| UNLRF     | 12/31/2020 | IDR      | 7672043 | 0    | 20534632 | 3974990 | 37  | 42972474 |
| UPS       | 12/31/2021 | USD      | 10813   | 88   | 69405    | 25528   | 15  | 97287    |
| V         | 9/30/2021  | USD      | 14522   | 54   | 82896    | 20977   | 17  | 24105    |
| V         | 9/30/2022  | USD      | 17879   | 60   | 85501    | 22450   | 21  | 29310    |
| V         | 9/30/2023  | USD      | 19696   | 76   | 90499    | 20463   | 22  | 32653    |
| V         | 9/30/2024  | USD      | 18693   | 85   | 94511    | 20836   | 20  | 35926    |
| VACNY     | 12/31/2023 | CHF      | 187     | 0    | 1168     | 207     | 16  | 885      |
| VACNY     | 12/31/2021 | CHF      | 197     | 0    | 1065     | 207     | 18  | 901      |
| VACNY     | 12/31/2022 | CHF      | 228     | 0    | 1275     | 211     | 18  | 1145     |
| VEEV      | 1/31/2021  | USD      | 551     | 19   | 3046     | 63      | 17  | 1465     |
| VEEV      | 1/31/2022  | USD      | 764     | 23   | 3816     | 55      | 19  | 1851     |
| VEEV      | 1/31/2023  | USD      | 780     | 35   | 4804     | 61      | 16  | 2155     |
| VRSK      | 12/31/2023 | USD      | 831     | 5    | 4366     | 3095    | 19  | 2681     |
| VRSN      | 12/31/2020 | USD      | 687     | 5    | 1767     | 1795    | 39  | 1265     |
| VRSN      | 12/31/2021 | USD      | 754     | 5    | 1984     | 1788    | 38  | 1328     |
| VRSN      | 12/31/2022 | USD      | 804     | 6    | 1733     | 1795    | 46  | 1425     |
| VRSN      | 12/31/2023 | USD      | 808     | 6    | 1749     | 1798    | 46  | 1493     |
| WAT       | 12/31/2020 | USD      | 618     | 4    | 2840     | 1452    | 22  | 2365     |
| WAT       | 12/31/2021 | USD      | 579     | 3    | 3095     | 1601    | 19  | 2786     |
| WDFC      | 8/31/2021  | USD      | 70      | 1    | 430      | 125     | 16  | 488      |
| WDFC      | 8/31/2023  | USD      | 92      | 1    | 438      | 129     | 21  | 537      |
| WDFC      | 8/31/2024  | USD      | 88      | 1    | 449      | 103     | 19  | 591      |
| WEGE3.SA  | 12/31/2020 | BRL      | 3371    | 1    | 19928    | 1974    | 17  | 17470    |
| WEGE3.SA  | 12/31/2023 | BRL      | 5363    | 1    | 31496    | 3392    | 17  | 32504    |
| WNS       | 3/31/2021  | USD      | 187     | 4    | 1106     | 209     | 17  | 913      |
| XPEL      | 12/31/2020 | USD      | 16      | 0    | 84       | 12      | 19  | 159      |

  