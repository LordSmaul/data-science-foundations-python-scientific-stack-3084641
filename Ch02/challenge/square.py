# %%
import matplotlib.pyplot as plt

img = plt.imread('flower.png')
img = img.copy()  # make img writable
plt.imshow(img)

#%%
type(img)
# %%
img.shape

# %%
# Draw a blue square around the flower
# Top-left: 190x350
# Bottom-right: 680x850
# Line width: 5

color = [0,0, 0xFF]

img[350:350+5, 190:680] = color
img[850:850+5, 190:680] = color
img[350:850, 190:190+5] = color
img[350:850, 680-5:680] = color

plt.imshow(img)