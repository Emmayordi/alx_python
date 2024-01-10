"""
 the module for request
"""
import requests

response = requests.get("https://alu-intranet.hbtn.io/status")
body = response.text
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))