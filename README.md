USE: AAPL_call_options, and AAPL_put_options seperately. 
REASON: They are very different. 

We focus more on call options: The trader buys call options at the "ask" price. It gives her the option (but not the obligation) 
to buy the stock at any time before expiration date at the "strike" price. 

Assume she buys a call option at time 0. Then her payoff at time t < expiration date is 
```
Payoff at time t = UnderlyingPrice at time t - (Ask Price at time 0 + Strike Price at time 0). 
```
Assume she buys a put option at time 0. Then her payoff at time t < expiration date is 
```
Payoff at time t = - UnderlyingPrice at time t + (Ask Price at time 0 + Strike Price at time 0). 
```
The put options are often being used as more of a defensive measure. 
