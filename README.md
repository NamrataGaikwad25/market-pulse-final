📈 Market Pulse — AI-Powered Stock Pulse Microservice
Predicts whether a stock is bullish, bearish, or neutral for tomorrow based on momentum and recent news. Built with FastAPI, React, and OpenAI GPT-3.5.

📂 Project Structure
market-pulse/
├── backend/
│   └── venv/
│       ├── Include/
│       ├── Lib/
│       ├── Scripts/
│       └── pyvenv.cfg
├── frontend/
│   ├── node_modules/
│   ├── public/
│   │   ├── favicon.ico
│   │   ├── index.html
│   │   ├── logo192.png
│   │   ├── logo512.png
│   │   ├── manifest.json
│   │   └── robots.txt
│   └── src/
│       ├── services/
│       │   ├── llm.py
│       │   ├── news.py
│       │   └── stock.py
│       ├── main.py
│       ├── README.md
│       └── requirements.txt
├── .gitignore
├── package-lock.json
├── package.json
└── README.md


⚙️ Technologies Used
Backend: FastAPI, HTTPX, CacheTools, OpenAI API

Frontend: ReactJS + Axios

AI: GPT-3.5 Turbo (OpenAI)

APIs: NewsAPI, Alpha Vantage

Deployment-ready: Docker and .env support

🚀 How to Run Locally
Prerequisites
Python 3.9+

Node.js and npm

API keys (OpenAI, NewsAPI, Alpha Vantage)

🛠 Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

# Add keys to .env
OPENAI_API_KEY=sk-...
NEWS_API_KEY=...
ALPHA_VANTAGE_API_KEY=...

# Run FastAPI
python -m uvicorn main:app --reload
Visit: http://127.0.0.1:8000/api/v1/market-pulse?ticker=AAPL

💻 Frontend Setup
cd frontend
npm install
npm start
Visit: http://localhost:3000 and enter stock ticker like AAPL, MSFT, etc.

✅ API Example
Endpoint:
GET /api/v1/market-pulse?ticker=AAPL

Sample response:
{
  "ticker": "AAPL",
  "as_of": "2025-07-17",
  "momentum": { "returns": [0.2, -0.1, 0.3, 0.0, -0.05], "score": 0.07 },
  "news": [ ... ],
  "pulse": "neutral",
  "llm_explanation": "The returns are mildly positive and news headlines are mixed."
}
🔐 .env File Example
OPENAI_API_KEY=sk-...
NEWS_API_KEY=your_newsapi_key
ALPHA_VANTAGE_API_KEY=your_alpha_key

Make sure .env is in .gitignore.

✅ Features
Momentum-based scoring
News analysis
GPT-powered prediction
In-memory caching
React-based frontend UI
Modular and clean code

🔧 Future Improvements
Add chart sparkline (Recharts)
Docker container setup
Unit testing
Deploy on Vercel, Render, or Railway

👩‍💻 Developer
Namrata Gaikwad
GitHub: @NamrataGaikwad25
