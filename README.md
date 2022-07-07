USE: AAPL_call_options, and AAPL_put_options seperately. 
REASON: They are very different. 

We focus more on call options: The trader buys call options at the "ask" price. It gives her the option (but not the obligation) 
to buy the stock at any time before expiration date at the "strike" price. 

ASSUME SHE BUYS A CALL OPTION AT TIME 0 THEN HER PAYOFF AT TIME t < expiration date IS
```
Payoff at time t = UnderlyingPrice at time t - (Strike Price at time 0 + Ask Price at time 0). 

ASSUME SHE BUYS A PUT OPTION AT TIME 0 THEN HER PAYOFF AT TIME t < expiration date IS 
Payoff at time t = - UnderlyingPrice at time t + (Strike Price at time 0 + Ask Price at time 0). 

The put options are more of a defensive measure. They are also more abstract. 
