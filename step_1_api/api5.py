import requests

def create_work(api_key, work_data):
    api_url = "https://api.devrev.ai/works.create"
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(api_url, headers=headers, json=work_data)
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print("Connection error:", e)
        return None

def main():
    api_key = "eyJhbGciOiJSUzI1NiIsImlzcyI6Imh0dHBzOi8vYXV0aC10b2tlbi5kZXZyZXYuYWkvIiwia2lkIjoic3RzX2tpZF9yc2EiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOlsiamFudXMiXSwiYXpwIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFtMGVtMlVBdnY6ZGV2dS8xIiwiZXhwIjoxODA3Mjc3OTg2LCJodHRwOi8vZGV2cmV2LmFpL2F1dGgwX3VpZCI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by9zdXBlcjphdXRoMF91c2VyL29pZGN8cGFzc3dvcmRsZXNzfGVtYWlsfDY2MTUyOWZkYWUzNGQ1MDRjZmE4ODQ1MyIsImh0dHA6Ly9kZXZyZXYuYWkvYXV0aDBfdXNlcl9pZCI6Im9pZGN8cGFzc3dvcmRsZXNzfGVtYWlsfDY2MTUyOWZkYWUzNGQ1MDRjZmE4ODQ1MyIsImh0dHA6Ly9kZXZyZXYuYWkvZGV2b19kb24iOiJkb246aWRlbnRpdHk6ZHZydi11cy0xOmRldm8vMW0wZW0yVUF2diIsImh0dHA6Ly9kZXZyZXYuYWkvZGV2b2lkIjoiREVWLTFtMGVtMlVBdnYiLCJodHRwOi8vZGV2cmV2LmFpL2RldnVpZCI6IkRFVlUtMSIsImh0dHA6Ly9kZXZyZXYuYWkvZGlzcGxheW5hbWUiOiI0bm0yMGlzMTM2IiwiaHR0cDovL2RldnJldi5haS9lbWFpbCI6IjRubTIwaXMxMzZAbm1hbWl0LmluIiwiaHR0cDovL2RldnJldi5haS9mdWxsbmFtZSI6IjRubTIwaXMxMzZAbm1hbWl0LmluIiwiaHR0cDovL2RldnJldi5haS9pc192ZXJpZmllZCI6dHJ1ZSwiaHR0cDovL2RldnJldi5haS90b2tlbnR5cGUiOiJ1cm46ZGV2cmV2OnBhcmFtczpvYXV0aDp0b2tlbi10eXBlOnBhdCIsImlhdCI6MTcxMjY2OTk4NiwiaXNzIjoiaHR0cHM6Ly9hdXRoLXRva2VuLmRldnJldi5haS8iLCJqdGkiOiJkb246aWRlbnRpdHk6ZHZydi11cy0xOmRldm8vMW0wZW0yVUF2djp0b2tlbi8yaDNvMFZrUCIsIm9yZ19pZCI6Im9yZ19FTXhTSXZMTGNCTlZJcDd0Iiwic3ViIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFtMGVtMlVBdnY6ZGV2dS8xIn0.Ii-Wv7VDUhnrl8sFJnAYMS0F-LDiiQAa4rDDcHNg_D4YOlk0N7a8GBgJkHqsDdYRdFMIBl_20diK8QwRCJ3fy0k_JWMMlWKLKvodX5eb4HNakVnDbDidKQaM4mCI5uW1k1ID7dHconnAkAxX4jn1nicCJ3qAZT0rV7chwpAy20VxMFpi8nZEwqIEL1M8t3JUCtRUVxmH7eaOCqMjkPTTPdKxYV6NOYzaun96IleisUmoqrcjnUXFJK0MBoZi9faMU1IxPhqUfMXwuwMzC17vCm5OMmloCwGRgVWe8-_aWahoyXYc8kaK07Whha2r-tsdikYMJBDqZ3uOcfVgBpbgtQ"  

    # Creating an issue
    issue_title = "Ritesh Shetty CREATED a New Issue"
    issue_payload = {
        "type": "issue",
        "applies_to_part": "CAPL-1", 
        "owned_by": ["don:identity:dvrv-us-1:devo/1m0em2UAvv:devu/1"],       
        "title": issue_title
    }
    issue_result = create_work(api_key, issue_payload)
    if issue_result:
        print("Issue created successfully.")
        print("Issue Details:", issue_result)
    else:
        print("Failed to create issue")

    # Creating a ticket
    ticket_title = "Ritesh Shetty CREATED a New Ticket"
    ticket_payload = {
        "type": "ticket",
        "applies_to_part": "PROD-1", 
        "owned_by": ["don:identity:dvrv-us-1:devo/1m0em2UAvv:devu/1"],       
        "title": ticket_title
    }
    ticket_result = create_work(api_key, ticket_payload)
    if ticket_result:
        print("Ticket created successfully.")
        print("Ticket Details:", ticket_result)
    else:
        print("Failed to create ticket")

if __name__ == "__main__":
    main()
