from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cachetools import TTLCache
from services.stock import get_price_momentum
from services.news import get_news
from services.llm import get_pulse_analysis
from datetime import datetime

app = FastAPI()

# Allow frontend CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cache setup
cache = TTLCache(maxsize=100, ttl=600)

@app.get("/api/v1/market-pulse")
async def market_pulse(ticker: str):
    if ticker in cache:
        return cache[ticker]

    momentum = await get_price_momentum(ticker)
    news = await get_news(ticker)
    pulse, explanation = await get_pulse_analysis(ticker, momentum, news)

    result = {
        "ticker": ticker.upper(),
        "as_of": datetime.now().strftime("%Y-%m-%d"),
        "momentum": momentum,
        "news": news,
        "pulse": pulse,
        "llm_explanation": explanation
    }

    cache[ticker] = result
    return result
