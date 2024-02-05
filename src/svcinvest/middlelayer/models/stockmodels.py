from pydantic import BaseModel, Field
import yfinance as yf
from typing import Any, Type

class StockPriceCheckInput(BaseModel):
    """Input to check Stock price."""

    stock_ticker: str = Field(description="Ticker symbol for stock")


class RecommendationStockInput(BaseModel):
    """Input to the stock recommendations"""
    recommend_stock_ticker: str = Field(description="Ticker symbol for stock")
    
