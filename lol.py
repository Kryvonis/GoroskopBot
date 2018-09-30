import json
from xml.etree import ElementTree as ET
from app.settings import Config


advice = ET.parse(f'{Config.BASE_PATH}/app/storage/daily.xml')
text = advice.find('gemini/today').text
text = ' '.join(text.split())
print(text)