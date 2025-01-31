from Backend.src.config import settings
from Backend.src.http_client import CMCHTTPClient

cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMC_API_KEY
)