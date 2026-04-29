# 📰 NewsExtractor — AI Signal Aggregator

A Flask web application that extracts, cleans, and "elaborates" news signals from multiple APIs and social platforms (Reddit) into a unified intelligence dashboard.

✨ Features

- **Multi-Source Extraction:** Pulls data from NewsData.io and Reddit (PRAW) simultaneously.
- **AI Elaboration:** Custom Python logic to sanitize raw JSON and handle API "trap" errors.
- **Asynchronous Search:** Real-time results without page reloads using JS Fetch.
- **Language Filtering:** Multi-language support (English, Tamil, Hindi, Malayalam, Telugu).
- **Responsive Dark UI:** Clean, card-based interface built with Bootstrap 5.

📂 Project Structure

NewsExtractor/
├── app.py              ← Flask routes & API orchestration
├── .env                ← 🔌 API KEYS GO HERE (Private)
├── requirements.txt    ← Python dependencies
├── README.md           ← Project documentation
├── static/
│   ├── css/style.css   ← Custom card & hover effects
│   └── js/main.js      ← Event listeners & Fetch logic
└── templates/
    └── home.html       ← Main dashboard UI

🚀 Quick Start

1. Install dependencies

pip install flask requests praw python-dotenv

2. Plug in your API Keys → .env

Create a `.env` file in the project root and add your credentials:

# NewsData.io API Key
API_KEY=your_newsdata_key_here

# Reddit API Credentials (Script type)
REDDIT_CLIENT_ID=your_id_here
REDDIT_CLIENT_SECRET=your_secret_here

3. The "Safety Shield" Logic → app.py

The app includes a custom `elaborate_news` function to handle API inconsistencies and prevent common crashes:

def elaborate_news(raw_data):
    articles = raw_data.get('results', [])
    processed_list = []
    
    for item in articles:
        # Check if item is a dictionary (Safety against 'str' objects)
        if isinstance(item, dict):
            processed_list.append({
                'title': item.get('title', 'No Title'),
                'desc': item.get('description', 'No Description'),
                'source': item.get('source_name', 'Unknown Source'),
                'img': item.get('image_url', 'https://via.placeholder.com/300'),
                'url': item.get('link', '#')
            })
    return processed_list

4. Run the app

python app.py

Open http://127.0.0.1:5000 in your browser, enter a topic like "AI" or "Space", and watch the signals aggregate!

🔌 Integration Details

| Component | Function | Responsibility |
| :--- | :--- | :--- |
| **NewsData API** | `requests.get()` | Fetches global news articles based on keywords. |
| **Reddit PRAW** | `reddit.search()` | Scrapes real-time social sentiment and trending posts. |
| **Backend** | `elaborate_news()` | Cleans raw JSON and enforces "crash-proof" data types. |
| **Frontend** | `fetch()` | Sends async requests to Flask and renders news cards. |

⚙️ Configuration

| Setting | Location | Description |
| :--- | :--- | :--- |
| **API_KEY** | `.env` | Required for traditional news data. |
| **REDDIT_ID** | `.env` | Required for social signal extraction. |
| **DEBUG_MODE** | `app.py` | Set to `True` for development/error logs. |
| **PORT** | `app.py` | Default is 5000 (Flask standard). |

📋 Requirements

- **Python 3.8+**
- **Flask** (Web Framework)
- **Requests** (HTTP Library)
- **PRAW** (Reddit API Wrapper)
- **Dotenv** (Environment Management)

---
**Developed for Corporate Technical Placement Portfolios**
