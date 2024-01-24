# InvestorAdviser

Stock investment adviser for beginners. This code uses LLM (OpenAI) and yahoo finance api to get realtime stock price and recommendations

This code use, LLM tools, agents.

### Without tools

```javascript
{'input': 'what is the latest price of Amazon stock',
 'output': 'To provide you with the latest price of Amazon stock, I need to access real-time data. However, I can guide you on how to check the current stock price yourself.\n\nYou can check the latest price of Amazon stock by visiting a financial website or using a stock market app. Some popular options include:\n\n1. Google Finance: Go to the Google Finance website and search for "Amazon stock price."\n2. Yahoo Finance: Visit the Yahoo Finance website and search for "Amazon stock price."\n3. Bloomberg: Access the Bloomberg website or app and search for "AMZN" (Amazon\'s stock ticker symbol) to find the current price.\n\nPlease note that stock prices can fluctuate throughout the trading day, so the price you see may not be the most up-to-date.',
 'intermediate_steps': []}
 ```

 ### With support of tools

 ```javascript
 {'input': 'what is the latest price of Amazon stock',
 'output': 'The latest price of Amazon stock is $155.34.',
 'intermediate_steps': [(AgentActionMessageLog(tool='StockPriceTool', tool_input={'stock_ticker': 'AMZN'}, log="\nInvoking: `StockPriceTool` with `{'stock_ticker': 'AMZN'}`\n\n\n", message_log=[AIMessage(content='', additional_kwargs={'function_call': {'name': 'StockPriceTool', 'arguments': '{\n  "stock_ticker": "AMZN"\n}'}})]),
   155.34)]}
```

### Useful Commands to run api service on docker
```
  $docker-compose up -d --build
  $docker-compose down
```



### Access API service through prox
URI : http://localhost:8080/fintech/stock