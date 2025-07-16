import os
from dotenv import load_dotenv
import httpx

# Load environment variables
load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

async def get_price_momentum(ticker):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={API_KEY}"

    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        data = res.json()

    try:
        closes = [float(v["4. close"]) for v in list(data["Time Series (Daily)"].values())[:6]]
        returns = [(closes[i] - closes[i+1]) / closes[i+1] for i in range(5)]
        score = round(sum(returns) / len(returns), 2)
        return {"returns": [round(r, 2) for r in returns], "score": score}
    except Exception:
        return {"returns": [], "score": 0.0}
