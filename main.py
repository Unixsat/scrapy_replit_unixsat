import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_temp_tag(tag):
  return tag.has_attr('class') and any(
      "CurrentConditions--tempValue--" in str(i) for i in tag['class'])

def fetch_weather(city):
  url = f"https://weather.com/weather/today/l/{city}"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  element = soup.find(get_temp_tag)
  temperature = element.text if element else "not available"
  return temperature

st.title("Temperatura em São Paulo")

city_code = "BRSP0001:1:BR"  # Código de São Paulo

current_temperature = fetch_weather(city_code)

st.write(f"Temperatura atual em São Paulo: {current_temperature}")