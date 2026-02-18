from typing import Optional, Dict
import logging
import requests

class MarketDataCollector:
    def __init__(self, data_sources: List[str]):
        self.data_sources = data_sources
        
    def fetch_data(self) -> Dict:
        try:
            data = {}
            
            for source in self.data_sources:
                response = requests.get(source)
                if response.status_code == 200:
                    market_data = response.json()
                    data.update(market_data)
                    
            return data
            
        except Exception as e:
            logging.error(f"Failed to fetch market data: {str(e)}")
            raise