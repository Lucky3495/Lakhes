import os
from google.cloud import texttospeech_v1
import http.client
import ssl
import urllib
from elevenlabs import set_api_key, generate
from elevenlabs.api import History

def create_voice(text):
    # Setting the api key
    set_api_key("3ce297e5906ec8788eaefd43be38a346")

    # Generating the audio with the given text
    # For the text you write the text that you want to be said
    # For the voice you write the name is the voice you want (you can get the names from the command below)
    # For the model Leave it as is no need to change it (it used the beta multi language one)
    audio = generate(
        text=text,
        voice='Dave',
        model='eleven_multilingual_v1'
    )
    print(type(audio))
    # Play the audio
    with open('initial.wav', mode='bw') as f:
        f.write(audio)

# def create_voice(text):
#     print("***VOICE_INPUT***")
#     print(text)
#     print("***VOICE_INPUT***")
#     text = get_tashkeel(text)
#     # print(text)
#     print(os.getcwd())
#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../speech-api/aqueous-depth-395918-38d24c14cd13.json'
#     client = texttospeech_v1.TextToSpeechClient()

#     synthesis_input = texttospeech_v1.SynthesisInput(text = text)

#     voiceOne  = texttospeech_v1.VoiceSelectionParams(
#         language_code = "ar-XA",
#         ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE,
#         name = "ar-XA-Standard-B"
#     )

#     """
#     # output file config
#     """
#     ##https://cloud.google.com/text-to-speech/docs/reference/rest/v1/VoiceSelectionParams

#     audio_config = texttospeech_v1.AudioConfig(
#         audio_encoding = texttospeech_v1.AudioEncoding.MP3,
#         pitch =  0
#     )

#     response = client.synthesize_speech(
#         input=synthesis_input,
#         voice= voiceOne,
#         audio_config= audio_config
#     )

#     with open('initial.wav','wb') as output:
#         output.write(response.audio_content)

# def get_tashkeel(text):
#     context = ssl.create_default_context()
#     context.check_hostname = False
#     context.verify_mode = ssl.CERT_NONE

#     conn = http.client.HTTPSConnection("www.7koko.com", context=context)
#     payload = f"textArabic={urllib.parse.quote(text, encoding='utf-8')}"
#     headers = {
#     'Accept': '*/*',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Cookie': '_gid=GA1.2.437484269.1692111263; _gat_gtag_UA_154385641_2=1; _tccl_visitor=3e7d0355-d875-55a0-b5c6-0c10d6b7a83e; _tccl_visit=3e7d0355-d875-55a0-b5c6-0c10d6b7a83e; _ga_WNHWFV5ER8=GS1.1.1692111262.1.0.1692111262.0.0.0; _ga=GA1.1.660410126.1692111263; _ga_X6H4SPSJ35=GS1.1.1692111262.1.0.1692111262.0.0.0',
#     'Origin': 'http://www.7koko.com',
#     'Referer': 'http://www.7koko.com/apps/tashkil/index.php',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
#     }
#     conn.request("POST", "/api/tashkil/index.php", payload, headers)
#     res = conn.getresponse()
#     data = res.read()
#     return data.decode("utf-8").replace('\n','')