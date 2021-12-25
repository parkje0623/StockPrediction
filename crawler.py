import pandas as pd
import numpy as np
import os

from datetime import date
import FinanceDataReader as fdr


def get_all_ticker(symbol):
    if symbol == 1:
        df_NYSDAQ = fdr.StockListing("NASDAQ")
        return df_NYSDAQ
    elif symbol == 2:
        df_NYSE = fdr.StockListing("NYSE")
        return df_NYSE
    elif symbol == 3:
        df_AMEX = fdr.StockListing("AMEX")
        return df_AMEX
    elif symbol == 4:
        df_SP500 = fdr.StockListing("SP500")
        return df_SP500



def get_stock_price(ticker, start_date=None, end_date=None):
    stock = fdr.DataReader(ticker, start_date, end_date)
    df_stock_price = pd.DataFrame(stock)
    df_stock_price = df_stock_price.drop('Change', axis=1)
    return df_stock_price

def main():
    ans_type = int(input("All stock data from specific market => Press 1 , specific stock data => Press 2, Indices => Press 3:     "))
    
    if not os.path.exists("data/US_price"):
        os.makedirs("data/US_price")
    
    elif not os.path.exists("data/Indices"):
        os.makedirs("data/Indices")
            
            
    if ans_type == 1:
        try:
            market_Type = int(input("NASDAQ = 1, NYSE = 2, AMEX = 3, S&P500 = 4:    "))
            all_tickers = get_all_ticker(market_Type)
            ticker_list= []
                
            for ticker in all_tickers["Symbol"]:
                ticker_list.append(ticker)
            
            start_date = input("Type the start date, if you don't want to start with the specific date, JUST Press Enter  ")
            end_date = input("Type the end date, if you don't want to start with the specific date, JUST Press Enter ")
                
            for stock in ticker_list:
                if (start_date or end_date) == "":
                    df = get_stock_price(stock)
                    df.to_csv('data/US_price/'+ stock +'_price.csv')
                else:
                    df = get_stock_price(stock, start_date, end_date)
                    df.to_csv('data/US_price/'+ ticker +'_price.csv')
            print("Done")
                
        except Exception as e:
            print("Error is " + str(e))
        
            
        
    elif ans_type == 2:
        ticker = input("Type the ticker that you want to get the stock price(Ex apple = AAPL, AMAZON = AMZN....)     ")
        start_date = input("Type the start date, if you don't want to start with the specific date, JUST Press Enter  ")
        end_date = input("Type the end date, if you don't want to start with the specific date, JUST Press Enter ")
        
        

        try: 
            if (start_date or end_date) == "":
                df = get_stock_price(ticker)
                df.to_csv('data/US_price/'+ ticker +'_price.csv')
            else:
                df = get_stock_price(ticker, start_date, end_date)
                df.to_csv('data/US_price/'+ ticker +'_price.csv')
            print("Done")
        except Exception as e:
            print("Error is " + str(e))
            
    elif ans_type == 3:
        indices_Type = input("Indices[Dow] = DJI, Indices[Nasdaq] = IXIC, Indices[US500] = 7: US500  ")
        start_date = input("Type the start date, if you don't want to start with the specific date, JUST Press Enter  ")
        end_date = input("Type the end date, if you don't want to start with the specific date, JUST Press Enter ")
        if (start_date or end_date) == "":
            df = get_stock_price(indices_Type)
            df.to_csv('data/Indices/'+ indices_Type +'_price.csv')
        else:
            df = get_stock_price(indices_Type, start_date, end_date)
            df.to_csv('data/Indices/'+ indices_Type +'_price.csv')
        print("done")
    else:
        print("Press either 1 or 2 or 3")
        


        
if __name__ == '__main__':
    main()