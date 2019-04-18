import requests
email='greedyboy@163.com'
url = "https://workflowy.com/accounts/password_reset/"
d={'email':email}
r = requests.post(url, data=d)
if 'There is no user registered with the specified email address' in r.text:
  isok = True
  print(email + ' can reg')
else:
  print(email + ' can not reg because of be regested')