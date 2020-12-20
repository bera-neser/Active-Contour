import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plot
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour
import requests

img = mpimg.imread('image.jpg')
img = rgb2gray(img)

s = np.linspace(0, 2 * np.pi, 119)
y = 62 + 30 * np.sin(s)
x = 106 + 30 * np.cos(s)
init = np.array([y, x]).T

r = requests.get
snake = active_contour(gaussian(img, 3), init, alpha=0.015, beta=10, gamma=0.001)

fig, ax = plot.subplots(figsize=(5, 5))
ax.imshow(img, cmap=plot.get_cmap('gray'))
ax.plot(snake[:, 1], snake[:, 0], '-r', lw=2)
ax.set_xticks([]), ax.set_yticks([])
ax.axis([0, img.shape[1], img.shape[0], 0])

plot.show()
