# 🛡️ PriceGuard AI

An AI-powered product price analysis assistant that helps users decide whether a product deal is worth buying.

PriceGuard AI uses:

- Google Gemini 3.1 Flash lite for AI reasoning
- LangGraph for agent workflow orchestration
- FastAPI for backend APIs
- React for frontend UI
- DuckDuckGo search for product information
- Automated price extraction and comparison

The system analyzes:

- Current market prices
- User offered price
- Possible discount
- Risk level
- Product sentiment
- AI recommendation


---

# ✨ Features

## AI Product Analysis

Enter:

```
Product name
Your offered price
```

Example:

```
Product:
Samsung Galaxy Z Fold7

Price:
40000
```

The system returns:

- Buy / Don't Buy decision
- Market price range
- Deal rating
- Risk level
- Discount percentage
- AI explanation
- Confidence score


---

# 🏗️ Project Architecture


```
User
 |
 |
React Frontend
 |
 |
FastAPI Backend
 |
 |
LangGraph Agent Workflow
 |
 ├── Product Resolver Agent
 |
 ├── Search Agent
 |
 ├── Price Extraction Agent
 |
 ├── Price Analysis Engine
 |
 ├── Sentiment Agent
 |
 └── Gemini Explanation Agent
 |
 |
Final Recommendation
```


---

# 📁 Project Structure


```
price-guard-ai/

│
├── backend/
│
│   ├── main.py
│   ├── graph.py
│   ├── resolver.py
│   ├── search.py
│   ├── extractor.py
│   ├── agents.py
│   ├── price_engine.py
│   ├── schemas.py
│   ├── requirements.txt
│   └── .env
│
│
├── frontend/
│
│   ├── src/
│   │    └── App.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
│
└── README.md
```


---

# ⚙️ Requirements


Install:

- Python 3.10+
- Node.js 18+
- npm


Check versions:

```bash
python --version

node --version

npm --version
```


---

# 🔑 Backend Setup


## 1. Open backend folder


```bash
cd backend
```


---

## 2. Create virtual environment


Windows:

```bash
python -m venv venv
```


Activate:

```bash
venv\Scripts\activate
```


Linux / Mac:

```bash
source venv/bin/activate
```


---

## 3. Install dependencies


```bash
pip install -r requirements.txt
```


---

# 🔐 Gemini API Setup


PriceGuard AI uses Google Gemini API.

Create an API key:

https://aistudio.google.com/app/apikey


Create:

```
backend/.env
```


Add:


```env
GOOGLE_API_KEY=your_gemini_api_key_here
```


Replace:

```
your_gemini_api_key_here
```

with your actual Gemini API key.


---

# 🚀 Start Backend


Inside:

```
backend/
```


Run:


```bash
uvicorn main:app --reload
```


Successful output:


```
Application startup complete
```


Backend runs at:


```
http://localhost:8000
```


API documentation:


```
http://localhost:8000/docs
```


---

# 🎨 Frontend Setup


Open a new terminal.


Go to frontend:


```bash
cd frontend
```


Install packages:


```bash
npm install
```


---

# ▶️ Start Frontend


Run:


```bash
npm run dev
```


You will see:


```
Local:
http://localhost:5173
```


Open this URL in your browser.


---

# 🧪 Testing


Example:


Product:

```
iPhone 17
```


Price:

```
5000
```


Possible output:


```
Decision:
BUY WITH CAUTION


Market Average:
₹90000+


Risk:
Medium


Explanation:
The price is significantly below market value.
Verify seller authenticity before purchasing.
```


---

# 🔄 How The AI Works


## 1. Product Resolver

Converts user input:

```
Samsung Galaxy Z
```

into:

```
Samsung Galaxy Z Fold7
```

so searches are more accurate.


---

## 2. Search Agent

Collects:

- Official product pages
- Retail listings
- Market information


---

## 3. Price Extractor

Finds valid prices and removes:

- Years
- Model numbers
- Battery sizes
- Random numbers


---

## 4. Price Engine

Calculates:

- Average market price
- Discount percentage
- Risk level
- Deal rating


---

## 5. Gemini AI

Gemini does not calculate prices.

It explains:

- Why the deal is good
- Possible risks
- Buying recommendation


---

# 🛠️ Troubleshooting


## Backend not starting


Check:

```bash
pip install -r requirements.txt
```


Make sure:

```
.env
```

exists.


---

## Gemini API Error


Check:

```
GOOGLE_API_KEY
```

is correct.


---

## Frontend cannot connect


Verify backend is running:


```
http://localhost:8000
```


Check frontend API URL:

```
src/App.jsx
```


It should contain:


```javascript
http://localhost:8000/analyze
```


---

## Wrong price analysis


The system depends on available online information.

For best results use:

Good:

```
Samsung Galaxy Z Fold7
```

Less accurate:

```
Samsung Galaxy Z
```


---

# 🚧 Future Improvements

Possible upgrades:

- Real-time retailer APIs
- User accounts
- Price history charts
- Browser extension
- Product image recognition
- More shopping sources
- Better fraud detection


---

# 📜 License

This project is for educational and research purposes.
