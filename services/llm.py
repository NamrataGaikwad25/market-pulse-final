import os
from dotenv import load_dotenv
import openai

# Load the API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def get_pulse_analysis(ticker, momentum, news):
    news_text = "\n".join([f"{n['title']} - {n['description']}" for n in news])
    
    prompt = f"""
You are a financial analyst. Based on the following data, decide if the stock {ticker} is bullish, bearish, or neutral for tomorrow. Also explain why in 1-2 sentences.

Momentum (last 5-day returns): {momentum['returns']}
Momentum score: {momentum['score']}
News:
{news_text}
"""

    response = openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    response_data = await response
    explanation = response_data['choices'][0]['message']['content']

    pulse = "neutral"
    if "bullish" in explanation.lower():
        pulse = "bullish"
    elif "bearish" in explanation.lower():
        pulse = "bearish"

    return pulse, explanation
