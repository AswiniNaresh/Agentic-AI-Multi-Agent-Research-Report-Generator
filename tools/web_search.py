import requests
from config import TAVILY_API_KEY

def tavily_search(query):
    try:
        res = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": TAVILY_API_KEY,
                "query": query,
                "max_results": 3
            },
            timeout=10
        )
        
        if res.status_code != 200:
            print(f"⚠ Tavily API error: {res.status_code} - {res.text}")
            return []
        
        data = res.json()
        results = data.get("results", [])
        print(f"✓ Web search found {len(results)} results for: {query}")
        return results
    except Exception as e:
        print(f"⚠ Web search error: {e}")
        return []