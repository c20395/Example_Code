#Example 10.21 language detection and translation
#pip install googletrans==3.1.0a0
from googletrans import Translator

translator = Translator()
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

translator.detect('이 문장은 한글로 쓰여졌습니다.')


translator.translate('안녕하세요.')
# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
