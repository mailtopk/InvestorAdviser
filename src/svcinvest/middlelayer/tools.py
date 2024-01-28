import yfinance as yf

from pydantic import BaseModel
from typing import Any, Type
from langchain.tools import BaseTool

from models.stockmodels import (
    StockPriceCheckInput, 
    RecommendationStockInput
)

class StockPriceTool(BaseTool):
    name = "StockPriceTool"
    description = """
    Useful to find the stock price.
    """
    def _run(self, stock_ticker: str):
        ticker = yf.Ticker(ticker=stock_ticker)
        current_price = ticker.history(period="1d")
        return round(current_price['Close'].iloc[-1], 2)

    def _arun(self, stock_ticker: str):
        raise NotImplementedError()  
    
    args_schema: Type[BaseModel] = StockPriceCheckInput   

class RecommendationStockTool(BaseTool):
    name = "RecommendationStockTool"
    description = "Useful to find recommendations to buy or hold if you have stocks,  if underperformed, not recommended. You should input the stock ticker which is used by yahoo finance API"
    
    def _run(self, recommend_stock_ticker: str):
     company = yf.Ticker(ticker=recommend_stock_ticker)
     return company.info['recommendationKey']

    def _arun(self, recommend_stock_ticker: str):
        raise NotImplementedError()  
    
    args_schema: Type[BaseModel] = RecommendationStockInput   

def get_stock_tools():
    return [StockPriceTool(), RecommendationStockTool()]