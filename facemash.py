import requests
from skimage import io
import matplotlib.pyplot as plt

num = 450
url = "https://api.disneyapi.dev/character/"
response = requests.get(url+f"{num}")
data = response.json()
imageUrl = data['data']['imageUrl']

image = io.imread(imageUrl)
plt.imshow(image)
plt.show()