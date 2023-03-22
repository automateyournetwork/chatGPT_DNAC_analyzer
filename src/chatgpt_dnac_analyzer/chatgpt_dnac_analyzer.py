import os
import json
import base64
import openai
import rich_click as click
import urllib3
import requests
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings()

webexToken = os.getenv("WEBEX_TOKEN")
webexRoomId = os.getenv("WEBEX_ROOMID")
openai.api_key = os.getenv("OPENAI_KEY")

class ChatGPT_DNAC_Analyzer():
    def __init__(self,
                url,
                username,
                password):
        self.dnac = url
        self.username = username
        self.password = password

    def chatgpt_dnac_analyzer(self):
        self.get_token()
        self.analyze_issues()
   
    def get_token(self):
        encodedCredentials=base64.b64encode(bytes(f'{ self.username }:{ self.password }', 'utf-8')).decode()
        
        auth_headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Basic { encodedCredentials }'
            }

        # -------------------------
        # Get OAuth Token
        # -------------------------

        oAuthTokenRAW = requests.request("POST", f"{ self.dnac }/dna/system/api/v1/auth/token", headers=auth_headers, verify=False)
        oAuthTokenJSON = oAuthTokenRAW.json()
        self.token = oAuthTokenJSON['Token']

    def analyze_issues(self):
        headers = {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'X-Auth-Token': self.token,
        }
    
        issuesRAW = requests.request("GET", f"{ self.dnac }/dna/intent/api/v1/issues", headers=headers, verify=False)
        issuesJSON = issuesRAW.json()
        for issue in issuesJSON['response']:
            print("|---------------------------------------------------------------------------------------------------------------------------------------------------|")                
            print(f"There was a DNAC Issue { issue['name'] } ")
            print("|---------------------------------------------------------------------------------------------------------------------------------------------------|")                
            print(f"I'm asking chatGPT about the event { issue['name'] }")
            print("|---------------------------------------------------------------------------------------------------------------------------------------------------|")
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "You are a network troubleshooting tool"},
                    {"role": "user", "content": f"Please describe the following Cisco Digital Network Architecture Center issue { issue['name'] }"},
                ]
            )

            result = ''
            for choice in response.choices:
                result += choice.message.content

            print(f"We asked chatGPT Please describe the following Cisco Digital Network Architecture Center issue { issue['name'] } - here was there response:")
            print("|---------------------------------------------------------------------------------------------------------------------------------------------------|")
            print(result)
            print("|---------------------------------------------------------------------------------------------------------------------------------------------------|")

            if webexToken:
                url = "https://webexapis.com/v1/messages"
            
                payload = json.dumps({
                  "roomId": f"{ webexRoomId }",
                  "text": f"We asked chatGPT Please describe the following Cisco Digital Network Architecture Center issue { issue['name'] } - here was there response:"
                })
                headers = {
                  'Authorization': f'Bearer { webexToken }',
                  'Content-Type': 'application/json'
                }
            
                response = requests.request("POST", url, headers=headers, data=payload)

                payload = json.dumps({
                  "roomId": f"{ webexRoomId }",
                  "text": f"{ result }"
                })

                response = requests.request("POST", url, headers=headers, data=payload)

            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "You are a chatbot"},
                    {"role": "user", "content": f"Please describe the following Cisco Digital Network Architecture Center issue { issue['name'] } and explain it like I'm 5"},
                ]
            )

            result = ''
            for choice in response.choices:
                result += choice.message.content

            print(f"We asked chatGPT Please describe the following Cisco Digital Network Architecture Center issue { issue['name'] } and explain it like I'm 5 - here was there response:")
            print("|---------------------------------------------------------------------------------------------------------------------------------------------------|")                    
            print(result)
            print("|---------------------------------------------------------------------------------------------------------------------------------------------------|")

            if webexToken:
                url = "https://webexapis.com/v1/messages"
            
                payload = json.dumps({
                  "roomId": f"{ webexRoomId }",
                  "text": f"We asked chatGPT Please describe the following Cisco Digital Network Architecture Center issue { issue['name'] } and explain it like I'm 5 - here was there response:"
                })
                headers = {
                  'Authorization': f'Bearer { webexToken }',
                  'Content-Type': 'application/json'
                }
            
                response = requests.request("POST", url, headers=headers, data=payload)

                payload = json.dumps({
                  "roomId": f"{ webexRoomId }",
                  "text": f"{ result }"
                })

                response = requests.request("POST", url, headers=headers, data=payload)

            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "You are a network troubleshooting tool"},
                    {"role": "user", "content": f"Is the Cisco Digital Network Architecture Center Issue { issue['name'] } a problem?"},
                ]
            )

            result = ''
            for choice in response.choices:
                result += choice.message.content

            print(f"We asked chatGPT Is the Cisco Digital Network Architecture Center Issue { issue['name'] } a problem? - here was there response:")
            print("|---------------------------------------------------------------------------------------------------------------------------------------------------|")                    
            print(result)
            print("|---------------------------------------------------------------------------------------------------------------------------------------------------|")                    

            if webexToken:
                url = "https://webexapis.com/v1/messages"
            
                payload = json.dumps({
                  "roomId": f"{ webexRoomId }",
                  "text": f"We asked chatGPT Is the Cisco Digital Network Architecture Center Issue { issue['name'] } a problem? - here was there response:"
                })
                headers = {
                  'Authorization': f'Bearer { webexToken }',
                  'Content-Type': 'application/json'
                }
            
                response = requests.request("POST", url, headers=headers, data=payload)

                payload = json.dumps({
                  "roomId": f"{ webexRoomId }",
                  "text": f"{ result }"
                })

                response = requests.request("POST", url, headers=headers, data=payload)

            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "You are a network troubleshooting tool"},
                    {"role": "user", "content": f"How do I troubleshoot a { issue['name'] } issue with Cisco Digital Network Architecture?"},
                ]
            )

            result = ''
            for choice in response.choices:
                result += choice.message.content

            print(f"We asked chatGPT How do I troubleshoot a { issue['name'] } issue with Cisco Digital Network Architecture? - here was there response:")
            print("|---------------------------------------------------------------------------------------------------------------------------------------------------|")                    
            print(result)
            print("|---------------------------------------------------------------------------------------------------------------------------------------------------|")                    

            if webexToken:
                url = "https://webexapis.com/v1/messages"
            
                payload = json.dumps({
                  "roomId": f"{ webexRoomId }",
                  "text": f"We asked chatGPT How do I troubleshoot a { issue['name'] } issue with Cisco Digital Network Architecture? - here was there response:"
                })
                headers = {
                  'Authorization': f'Bearer { webexToken }',
                  'Content-Type': 'application/json'
                }
            
                response = requests.request("POST", url, headers=headers, data=payload)

                payload = json.dumps({
                  "roomId": f"{ webexRoomId }",
                  "text": f"{ result }"
                })

                response = requests.request("POST", url, headers=headers, data=payload)

@click.command()
@click.option('--url',
    prompt="DNAC URL",
    help="DNAC URL",
    required=True,envvar="URL")
@click.option('--username',
    prompt="DNAC Username",
    help="DNAC Username",
    required=True,envvar="USERNAME")
@click.option('--password',
    prompt="DNAC Password",
    help="DANC Password",
    required=True, hide_input=True,envvar="PASSWORD")

def cli(url,username,password):
    invoke_class = ChatGPT_DNAC_Analyzer(url,username,password)
    invoke_class.chatgpt_dnac_analyzer()

if __name__ == "__main__":
    cli()