# Scraping

Compilation of various code snippets used to scrape data from different sources for various purposes in the last year. 

## Code Snippets

### 1. Walt Disney Investor Relations Data

Grabs annual or quarterly reports from Walt Disney investor relations reports and downloads them. Iterates through the pdfs in directory and converts all tabled numbers into 1 csv file for the report. (Winter 2024)

#### Notebook
[Walt Disney Notebook](waltDisney.ipynb)

#### Output
[PDF Example](outputs/2023-Annual-Report.pdf)
[CSV Example](outputs/2023-Annual-Report.csv)

### 2. Scraping Chess.com Computer Games Database

Simulates browser use through selenium, selecting and downloading games played in the computer chess championship. (Summer 2023)

#### Notebook
[Chess.com Notebook](scrapingCompChess.ipynb)

#### Output
[Chess Games Example](outputs/chessGames.pgn)

### 3. API calls to EIA API for Petroleum Prices

Examples of calls made to Energy Information Administration API for gathering energy related pricing data over various time periods. (Fall 2023)

#### Notebook
[EIA API Calls Notebook](EIA_API_Interaction.ipynb)

#### Output
[Petroleum Example](outputs/petroleumOuput.json)

### 4. YahooFinance Library - Stock Price Data

Snippet of use of yfinance library in python to gather data on stock prices to be used in a time series analysis of the S&P500. (Summer 2023)

#### Notebook 
[yFinance Notebook](yfinancelibrary.ipynb)

#### Output
[S&P 500 Example](outputs/s_and_p_data.csv)

### 5. Miscellaneous Browser-Console Code Examples to Fetch Graph/Table/Article Data

Examples of js code run in console on chrome to get well formatted currency, commodities, etc. data. Third code snippet fetches a dictionary with key-value pairs of article title and link to allow for further filtering, information gathering, or language processing. (Working as of 02/29/2024)

#### Code Snippet Examples
[Trading Economics Graph Data](BrowserBased/highchars.js) \
[Bloomberg Tables](BrowserBased/bloombergTableDataAny.js) \
[Bloomberg Articles](BrowserBased/bloombergArticle.js)

#### Output
Browser based, outputs either a clickable link to console or a js object



