import numpy as np
import tensorflow as tf

text = np.loadtxt("d:/data/prac/xy.txt", dtype=np.str, delimiter=" ", skiprows=0)
x_data = text[1:,0]
y_data = text[1:,1]

xxy2 = np.loadtxt("d:/data/prac/xxy.csv", dtype=np.str, delimiter=",", unpack=True)
xxy = np.loadtxt("d:/data/prac/xxy.csv", dtype=np.str, delimiter=",")

car = np.loadtxt("d:/data/prac/cars.csv", dtype=np.float32, delimiter=",")

xx, yy = [], []

for i in range(car.shape[0]):
    item=car[i]
    xx.append(item[0])
    yy.append(item[1])

cars = np.loadtxt("d:/data/prac/cars.csv", delimiter=",", unpack=True)
cars = cars.T
