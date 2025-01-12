
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


  