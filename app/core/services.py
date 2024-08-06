# 외부 데이터 처리 파일
import requests
from json.decoder import JSONDecodeError

def fetch_data_from_api():
    url = 'https://apis.data.go.kr/B553748/CertImgListServiceV3/getCertImgListServiceV3?ServiceKey=j60V6KWnaSxrnblnCkKEEooTQdW9Jx4Ayh%2FmxhV46yPIDI5Lmk6mPKbVKPcTz757jswtGniYg%2BAH%2FgZPCnglUA%3D%3D&returnType=json'
    params = {
        'ServiceKey': 'j60V6KWnaSxrnblnCkKEEooTQdW9Jx4Ayh/mxhV46yPIDI5Lmk6mPKbVKPcTz757jswtGniYg+AH/gZPCnglUA==',
        'type': 'json',
        'numOfRows': '100',
        'pageNo': '50',

    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except JSONDecodeError:
        print("JSON Decode Error")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        return None