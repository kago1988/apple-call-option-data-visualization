import pandas as pd 
from datetime import datetime




class CreateDataArrays():
    def __init__(self, AAPL_call_options):
        self.df_DataDate = AAPL_call_options['DataDate']
        self.df_Expiration = AAPL_call_options['Expiration']
        self.df_UnderlyingPrice = AAPL_call_options['UnderlyingPrice']
        self.df_Strike = AAPL_call_options['Strike']
        self.df_Ask = AAPL_call_options['Ask']
        self.expiration_days_array = [] 
        self.trading_days_array = self.get_date_array(AAPL_call_options['DataDate'])

    def get_date_array(self, series):
        date_array = []
        for i in range(len(series)):
            if series[i] not in date_array:
                date_array.append(series[i])
        return date_array  

    def get_buying_dates(self):
        return_array = pd.Series( (x for x in self.trading_days_array) )
        return return_array 

    def get_underlying_prices(self):
        underlying_prices_array = [] 
        for i in range(len(self.trading_days_array)):
            idx = self.df_DataDate.loc[self.df_DataDate == self.trading_days_array[i]].index[0]
            underlying_prices_array.append(self.df_UnderlyingPrice[idx])
        return_array = pd.Series( (x for x in underlying_prices_array) )
        return return_array 

    def make_expiration_date_array(self, overlap_array):
        self.expiration_days_array = overlap_array 

    def get_scattered_overlap_dates(self): 
        overlap_array = [] 
        for i in range(len(self.df_Expiration)):
            if self.df_Expiration[i] in self.trading_days_array and self.df_Expiration[i] not in overlap_array:
                overlap_array.append(self.df_Expiration[i])
        if self.expiration_days_array == []: self.make_expiration_date_array(overlap_array)
        return_array = pd.Series( (x for x in overlap_array) )
        return return_array 

    def get_scattered_strike_price_plus_ask_price(self): 
        scattered_strike_price_plus_ask_price = [] 
        for i in range(len(self.expiration_days_array)):
            mean_strike_entries = self.df_Strike.loc[self.df_DataDate == self.expiration_days_array[i]].mean()
            mean_ask_entries = self.df_Ask.loc[self.df_DataDate == self.expiration_days_array[i]].mean()
            scattered_strike_price_plus_ask_price.append(mean_strike_entries + mean_ask_entries)
        return_array = pd.Series( (x for x in scattered_strike_price_plus_ask_price) )
        return return_array 

    def get_option_interest_rate_series(self): 
        interest_rates = [] 
        interest_rate_jump_days = ['02/01/2021', '02/15/2022', '04/01/2022', '05/01/2022']
        interest_rate_jump_values = [0.25, 0.5, 1, 1.75]

        for i in range(len(self.df_DataDate)): 
            interest_rates.append(interest_rate_jump_values[0])
        k = 0 
        for i in range(len(self.df_DataDate)): 
            if k != 0 or self.df_DataDate[i] == interest_rate_jump_days[1]: 
                interest_rates.append(interest_rate_jump_values[1])
                k = i 
        k = 0 
        for i in range(len(self.df_DataDate)): 
            if k != 0 or self.df_DataDate[i] == interest_rate_jump_days[2]: 
                interest_rates.append(interest_rate_jump_values[2])
                k = i 
        k = 0 
        for i in range(len(self.df_DataDate)): 
            if k != 0 or self.df_DataDate[i] == interest_rate_jump_days[3]: 
                interest_rates.append(interest_rate_jump_values[3])
                k = i 

        return_array = pd.Series( (x for x in interest_rates) )
        return return_array 

    def get_time_until_expiration_series(self): 
        date_format = "%m/%d/%Y"
        time_until_expiration = [] 
        for i in range(len(self.df_DataDate)): 
            a = datetime.strptime(self.df_DataDate[i], date_format)
            b = datetime.strptime(self.df_Expiration[i], date_format)
            delta = b - a
            time_until_expiration.append(delta.days )

        return_array = pd.Series( (x for x in time_until_expiration) )
        return return_array 
