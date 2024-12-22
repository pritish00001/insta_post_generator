from langchain_community.utilities import GoogleSerperAPIWrapper
from crewai.tools import tool

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access an environment variable
serper_api_key = os.getenv('SERPER_API_KEY')

class SearchTools():

  @tool("Search internet")
  def search_internet(query:str):
    """Useful to search the internet about a given topic and return relevant
    results."""
    return SearchTools.search(query)

  @tool("Search instagram")
  def search_instagram(query:str):
    """Useful to search for instagram post about a given topic and return relevant
    results."""
    query = f"site:instagram.com {query}"
    return SearchTools.search(query)
  
  @tool("Search trends")
  def search_trends(query:str):
    """Useful to search trends about a given topic and return relevant
    results."""
    query = f"site:trends.google.com/trends/explore {query}"
    return SearchTools.search(query)

  def search(query:str, n_results=5):
    wrapper = GoogleSerperAPIWrapper(serper_api_key=serper_api_key)
    result = wrapper.run(query)
    return f"\nSearch result: {result}\n"