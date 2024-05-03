import requests

class API:

    def sentiment_analysis(self,text):
        url = "https://api.symanto.net/sentiment"
        payload = text
        headers = {
            "x-api-key": "opensesame",
            "Content-Type": "application/json"
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response
