from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
apikey =os.getenv('OPENAI_API_KEY')

def img_gen(prompt):   
    client  = OpenAI(api_key=apikey)
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    quality="standard",
    n=1,
    response_format="url"
    )
    image_url = response.data[0].url
    return (image_url)




