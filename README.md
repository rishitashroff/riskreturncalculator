# DS 4420 - Spring 2025 - Final Project - Risk Return Calculator using Long Short-Term Memory and Bayesian Modeling 
Authors: Calvin Li, Rishita Shroff 

## High-Level Overview 
We hope to help investors make an informed decisions based on the predicted return and the volatility of a company, and study if advanced machine learning models can capture the changes in the sectors.

## DataSet
We downloaded stock return and S&P500 data using `yfinance`, resampling it for monthly data. We alse obtained Fama-French Factors such as risk-free rate via `pnadas_datareader`. CPI (Consumer Price Index) and inflation rate came from the FRED API `web`, and standard deviation and 30-day rolling average was derived from the returns. 

## Setup Instructions 
## Python Environment
- Your implementation should run with Python 3.11. To create a new conda environment with python 3.11, run the following:

```bash
conda create -n <new_env_name> python=3.11
```

Then activate the newly created python environment with: 
```bash
conda activate <new_env_name> 
```
Subsequently, install additional packages listed in the requirements.txt file with:

```bash
pip install -r requirements.txt
```

## LSTM Instructions (LSTM.ipynb)
Once all libraries are downloaded and you are in the appropriate conda environment you can simply run all the cells in the jupyter notebook. 

## Shiny App and Empirical Bayesian Instructions(EmpiricalBayesian.Rmd)
Install all packages needed and run all cells in the R Markdown file. To run this file, you can download the following files:
- result.csv
- filtered_sp500_stocks.csv
  
"Note: Downloading the 3 files and running the .rmd file would be faster if you want to see the app only."

## Short Reflection on Results
The LSTM perform poorly with macroeconomic indicators such as risk-free rate, inflation rate, and derived attribute such as 30-day rolling average, and standard deviation for stock return prediction.
The Bayesian Model performed well under the  assumptions that the stock’s variance depends on 
- the variance of all stocks within the same sector 
- the variance of a stock is within a similar price range of the same sector

## Future Work 
More qualitative and other quantitative sector-specific information and features are needed for increased accuracy. We can also get daily data rather than monthly data for an increased dataset size, to improve training. Lastly, we want to use advance techniques such as a supervised Bayesian machine learning to evaluate how other factors affect variance. 
