# Nest Rates
A simple app that renests a json.
## Example
Sample request
```python
import requests

url = "127.0.0.1:5000?nkeys=country,city,currency"

payload = "[\r\n  {\r\n    \"country\": \"US\",\r\n    \"city\": \"Boston\",\r\n    \"currency\": \"USD\",\r\n    \"amount\": 100\r\n  },\r\n  {\r\n    \"country\": \"FR\",\r\n    \"city\": \"Paris\",\r\n    \"currency\": \"EUR\",\r\n    \"amount\": 20\r\n  },\r\n  {\r\n    \"country\": \"FR\",\r\n    \"city\": \"Lyon\",\r\n    \"currency\": \"EUR\",\r\n    \"amount\": 11.4\r\n  },\r\n  {\r\n    \"country\": \"ES\",\r\n    \"city\": \"Madrid\",\r\n    \"currency\": \"EUR\",\r\n    \"amount\": 8.9\r\n  },\r\n  {\r\n    \"country\": \"UK\",\r\n    \"city\": \"London\",\r\n    \"currency\": \"GBP\",\r\n    \"amount\": 12.2\r\n  },\r\n  {\r\n    \"country\": \"UK\",\r\n    \"city\": \"London\",\r\n    \"currency\": \"FBP\",\r\n    \"amount\": 10.9\r\n  }\r\n]"
headers = {
  'Authorization': 'Basic dXNlcjp1c2Vy',
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
```
```javascript
[
  {
    "country": "US",
    "city": "Boston",
    "currency": "USD",
    "amount": 100
  },
  {
    "country": "FR",
    "city": "Paris",
    "currency": "EUR",
    "amount": 20
  },
  {
    "country": "FR",
    "city": "Lyon",
    "currency": "EUR",
    "amount": 11.4
  },
  {
    "country": "ES",
    "city": "Madrid",
    "currency": "EUR",
    "amount": 8.9
  },
  {
    "country": "UK",
    "city": "London",
    "currency": "GBP",
    "amount": 12.2
  },
  {
    "country": "UK",
    "city": "London",
    "currency": "FBP",
    "amount": 10.9
  }
]
```
Sample output:
```javascript
{
  "EUR": {
    "ES": {
      "Madrid": [
        {
          "amount": 8.9
        }
      ]
    },
    "FR": {
      "Lyon": [
        {
          "amount": 11.4
        }
      ],
      "Paris": [
        {
          "amount": 20
        }
      ]
    }
  },
  "FBP": {
    "UK": {
      "London": [
        {
          "amount": 10.9
        }
      ]
    }
  },
  "GBP": {
    "UK": {
      "London": [
        {
          "amount": 12.2
        }
      ]
    }
  },
  "USD": {
    "US": {
      "Boston": [
        {
          "amount": 100
        }
      ]
    }
  }
}
```
