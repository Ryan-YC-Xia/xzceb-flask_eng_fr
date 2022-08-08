import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-08-08',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    if english_text is None:
        return None
    result = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    return result['translations'][0]['translation']

def french_to_english(french_text):
    if french_text is None:
        return None
    result = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    return result['translations'][0]['translation']
