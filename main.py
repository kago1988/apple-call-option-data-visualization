import pandas as pd
import plot 
from create_data_arrays import CreateDataArrays 
from calculate_greeks import Greeks 








AAPL_stock = pd.read_csv('AAPL_stock.csv')
AAPL_options = pd.read_csv('AAPL_options.csv')
AAPL_stock_vol = AAPL_stock['Volume']
AAPL_stock_spread = AAPL_stock['High'] - AAPL_stock['Low']
AAPL_stock_date = AAPL_stock['Date'] 
AAPL_call_options = AAPL_options.loc[AAPL_options['Type'] == 'call'].reset_index(drop=True)
AAPL_put_options = AAPL_options.loc[AAPL_options['Type'] == 'put'].reset_index(drop=True)

C = CreateDataArrays(AAPL_call_options)
# based on: Taking every trading day once. And searching for the underlying price. 
trading_days_series = C.get_buying_dates()
underlying_price_series = C.get_underlying_prices()
# based on scattered "expiration date days"
scattered_expiration_days_series = C.get_scattered_overlap_dates()
scattered_strike_price_plus_ask_price_series = C.get_scattered_strike_price_plus_ask_price() 
# Calculating the "Greeks". We need an array, that contains for every row of AAPL_call_options the interest rate. See './interest_rate.jpg' 
# We also need an array, that contains for every row of AAPL_call_options the number of days until expiration. 
call_option_interest_rate_series = C.get_option_interest_rate_series()
time_until_expiration_series = C.get_time_until_expiration_series()




# THESIS I: AT EXPIRATION DATE: IS AVE(STRIKE PRICES + ASK PRICES) A GOOD PREDICTOR FOR THE STOCK PRICES? 
# ANSWER: YES: LOOK AT './results/thesis_1.png' YOU CAN RUN A LINEAR REGRESSION OVER THE RED DOTS. 
plot.show_finance('stock_price_dates', 'stock price', 'CALL: ave(strike prices + ask prices) at expiration', trading_days_series, underlying_price_series, 
                    scattered_expiration_days_series, scattered_strike_price_plus_ask_price_series)

# THESIS II: LOOK FOR CORRELATION BETWEEN a) TRADING VOLUME AND b) SPREAD BETWEEN HIGH AND LOW STOCK VALUE 
# ANSWER: YES: LOOK AT './results/thesis_2.png' THEY ARE VERY CORRELATED. 
plot.show_correlation('Stock Trading Volume', 'Stock: SPREAD Between high and low stock value', AAPL_stock_vol, AAPL_stock_spread)

# THESIS III: RIGHT AT THE DATE WHEN THE CALL OPTION IS BID: IS ARE INDIVIDUAL (STRIKE PRICE + ASK PRICE) CORRELATED TO THE TRADING VOLUME? 
# ANSWER: LOOK AT './results/thesis_3a.png' AND './results/thesis_3b.png'. I CANNOT SEE THAT (STRIKE PRICE + ASK PRICE) AND TRADING VOL ARE CORRELLATED. 
plot.show_correlation_2('Time', 'Trading Volume', 'CALL: (Strike + Ask) at Bid Date', AAPL_stock_date, AAPL_stock_vol, 
                AAPL_call_options['DataDate'], (AAPL_call_options['Strike']+AAPL_call_options['Ask']))

# CALCULATE GREEKS 
# Implied volatility and interest rate: see "./implied_volatility.jpg" and "./interest_rate.jpg". 
G = Greeks('c', AAPL_call_options, call_option_interest_rate_series, time_until_expiration_series)
G.return_greeks() 
