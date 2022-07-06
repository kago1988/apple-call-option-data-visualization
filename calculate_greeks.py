import numpy as np
from scipy.stats import norm




class Greeks(): 
    def __init__(self, type, AAPL_call_options, r, T): 
        self.option_type = type # option type is either 'c' or 'p' 
        self.S = AAPL_call_options['UnderlyingPrice'] # Underlying price 
        self.K = AAPL_call_options['Strike'] # Strike Price 
        self.r = r # interest rate. I created this pd.Series from tradingeconomics.com. See 'interest_rate.jpg'
        self.T = T # time until expiration. I created this array from the main, delegating it to "create_data_arrays.py"
        self.sigma = 0.3457 # standard deviation. I took this parameter from alphaquery.com. See 'implied_volatility.jpg' 




    def calc_black_scholes(self, r, S, K, T, sigma, type="c"):
        "Calculate BS price of call/put"
        d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        try:
            if type == "c":
                price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
            elif type == "p":
                price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
            return price 
        except:
            print("Please confirm option type, either 'c' for Call or 'p' for Put!")

    def calc_delta(self, r, S, K, T, sigma, type="c"):
        "Calculate delta of an option"
        d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
        try:
            if type == "c":
                delta_calc = norm.cdf(d1, 0, 1)
            elif type == "p":
                delta_calc = -norm.cdf(-d1, 0, 1)
            return delta_calc 
        except:
            print("Please confirm option type, either 'c' for Call or 'p' for Put!")

    def calc_gamma(self, r, S, K, T, sigma, type="c"):
        "Calculate gamma of a option"
        d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        try:
            gamma_calc = norm.pdf(d1, 0, 1)/(S*sigma*np.sqrt(T))
            return gamma_calc 
        except:
            print("Please confirm option type, either 'c' for Call or 'p' for Put!")

    def calc_vega(self, r, S, K, T, sigma, type="c"):
        "Calculate BS price of call/put"
        d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        try:
            vega_calc = S*norm.pdf(d1, 0, 1)*np.sqrt(T)
            return vega_calc*0.01 
        except:
            print("Please confirm option type, either 'c' for Call or 'p' for Put!")

    def calc_theta(self, r, S, K, T, sigma, type="c"):
        "Calculate BS price of call/put"
        d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        try:
            if type == "c":
                theta_calc = -S*norm.pdf(d1, 0, 1)*sigma/(2*np.sqrt(T)) - r*K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
            elif type == "p":
                theta_calc = -S*norm.pdf(d1, 0, 1)*sigma/(2*np.sqrt(T)) + r*K*np.exp(-r*T)*norm.cdf(-d2, 0, 1)
            return theta_calc/365 
        except:
            print("Please confirm option type, either 'c' for Call or 'p' for Put!")

    def calc_rho(self, r, S, K, T, sigma, type="c"):
        "Calculate BS price of call/put"
        d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        try:
            if type == "c":
                rho_calc = K*T*np.exp(-r*T)*norm.cdf(d2, 0, 1)
            elif type == "p":
                rho_calc = -K*T*np.exp(-r*T)*norm.cdf(-d2, 0, 1)
            return rho_calc*0.01 
        except:
            print("Please confirm option type, either 'c' for Call or 'p' for Put!")

    def return_greeks(self): 
        for i in range(len(self.r)):
            print("Black Scholes: ", self.calc_black_scholes(self.r[i], self.S[i], self.K[i], self.T[i], self.sigma, self.option_type))
            print("       Delta: ", self.calc_delta(self.r[i], self.S[i], self.K[i], self.T[i], self.sigma, self.option_type))
            print("       Gamma: ", self.calc_gamma(self.r[i], self.S[i], self.K[i], self.T[i], self.sigma, self.option_type))
            print("       Vega : ", self.calc_vega(self.r[i], self.S[i], self.K[i], self.T[i], self.sigma, self.option_type))
            print("       Theta: ", self.calc_theta(self.r[i], self.S[i], self.K[i], self.T[i], self.sigma, self.option_type))
            print("       Rho  : ", self.calc_rho(self.r[i], self.S[i], self.K[i], self.T[i], self.sigma, self.option_type))
