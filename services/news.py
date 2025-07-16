import os
from dotenv import load_dotenv
import httpx

# Load environment variables
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

async def get_news(ticker):
    url = f"https://newsapi.org/v2/everything?q={ticker}&pageSize=5&apiKey={NEWS_API_KEY}"

    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        articles = res.json().get("articles", [])

    return [
        {
            "title": a["title"],
            "description": a["description"],
            "url": a["url"]
        } for a in articles
    ]
