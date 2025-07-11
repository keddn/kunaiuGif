import requests, uuid, os
#Read the README file :)
headers = {
  'User-Agent': "okhttp/3.12.13",
  'Client-Id': "kunaiu-android",
  'Client-Secret': "b7022a16e0c896575g2d82c33a8h2d9d36781g33"
}

res = requests.post("https://api.kunaiu.com/anime-social/api/email/login", data={
  'email': input(" [+] Email : "),
  'password': input(" [+] Password : "),
  'device_id': uuid.uuid4().hex
}, headers=headers).json()

d, u = res['data'], res['data']['data']
headers['Authorization'] = f"Bearer {d['access_token']}"


img = "profile.jpg"
if not os.path.exists(img): exit(" The image is not found, Make sure it is in the same path")

data = {k: u[k] for k in ['user_full_name', 'user_handle', 'bio', 'location', 'birthdate']} | {'sensitive_image': 'No'}
files = [('user_image_file', (img, open(img, 'rb'), 'application/octet-stream'))]

r = requests.post("https://api.kunaiu.com/anime-social/api/user/update", data=data, files=files, headers=headers)
print("[✓] updated successfully" if r.ok else r.text)
