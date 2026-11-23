# # from distance_api import _geocode

# # addresses = [
# #     "Sector 42 Gurgaon",
# #     "Sector 45, Gurgaon, Haryana",
# #     "Sector 46, Gurgaon, Haryana",
# #     "Sector 47, Gurgaon, Haryana",
# #     "Sector 48, Gurgaon, Haryana",
# # ]

# # for addr in addresses:
# #     coords = _geocode(addr)
# #     print(f"{addr} -> {coords}  (map: https://www.google.com/maps?q={coords[1]},{coords[0]})")

# from distance_api import _geocode
# import time

# addresses = [
#     "Sector 42 Metro Station, Gurgaon, Haryana",
#     "Sector 45 Market, Gurgaon, Haryana",
#     "Sector 46 Market, Gurgaon, Haryana",
#     "Sector 44 DLF Phase 3, Gurgaon, Haryana",
#     "Sector 47 Vatika India Next, Gurgaon, Haryana",
#     "Sector 48 Sohna Road, Gurgaon, Haryana",
# ]

# for addr in addresses:
#     coords = _geocode(addr)
#     print(f"{addr} -> {coords}  (map: https://www.google.com/maps?q={coords[1]},{coords[0]})")
#     time.sleep(1.5)  # avoid hitting the rate limit that caused your 404s

# import json

# data = json.load(open('apartments.json'))

# print('Apartments with 0 or near-zero commute:')
# for a in data:
#     if a['commute_minutes'] is not None and a['commute_minutes'] < 2:
#         print(f"  {a['name']}: {a['commute_minutes']} min")

# print()
# print('All commute times:')
# for a in data:
#     print(f"  {a['name']}: {a['commute_minutes']} min")

# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")

# url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

# response = requests.get(url)

# print(response.status_code)
# print(response.text)


# import requests, os, urllib3
# urllib3.disable_warnings()
# from dotenv import load_dotenv
# load_dotenv()
# key = os.environ.get('GEMINI_API_KEY')
# r = requests.post(
#     f'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={key}',
#     headers={'Content-Type': 'application/json'},
#     json={
#         'contents': [{'role': 'user', 'parts': [{'text': 'say hello'}]}],
#         'generationConfig': {'maxOutputTokens': 50}
#     },
#     timeout=30,
#     verify=False
# )
# print(r.status_code)
# print(r.json())

# import theme; print(theme.__file__)
# print(theme.load_tracker)

# import theme, inspect; 
# print(inspect.signature(theme.load_tracker))



with open('landing.py', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if any(x in line for x in ['st.markdown(html', 'components', 'enterApp', 'query_params', 'import streamlit']):
            print(f'{i}: {line}', end='')

with open('landing.py', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines[744:765], 745):
    print(f'{i}: {line}', end='')

with open('landing.py', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines[13:19], 14):
    print(f'{i}: {line}', end='')
