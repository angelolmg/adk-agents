import os
from dotenv import load_dotenv
from google.genai import Client

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Agora o Client() consegue achar a GEMINI_API_KEY automaticamente!
client = Client()

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Explique CNN em 5 linhas.'
)

print(response.text)