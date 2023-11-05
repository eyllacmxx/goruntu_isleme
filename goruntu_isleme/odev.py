import numpy as np
import cv2
from matplotlib import pyplot as plt
def histogram_computation(resim):
    resim_height = resim.shape[0]
    resim_width = resim.shape[1]
    resim_channels = resim.shape[2]
    histogram = np.zeros([256,resim_channels],np.int32)
    for x in  range (0,resim_height):
        for  y in range(0,resim_width):
            for c in range(0,resim_channels):
                histogram[resim[x,y,c],c] +=1
    return histogram
def plot_histogram(histogram):
    plt.figure()
    plt.title("renkli gorunumlu histogram")
    plt.xlabel("yogunluk seviyesi")
    plt.ylabel("yogunluk frekansi")
    plt.xlim([0, 256])
    plt.plot(histogram[:,0],'b') #plot mavi renkli kanalda rengi mavi
    plt.plot(histogram[:,1],'g') #plot yesil renkli kanalda rengi yesil
    plt.plot(histogram[:, 2], 'r')  # plot kirmizi renkli kanalda rengi kirmizi
    plt.savefig("Color_Histogram.jpg")
def main():
    resim=cv2.imread("manzara.jpeg")
    histogram = histogram_computation(resim)
    for i in range(0,histogram.shape[0]):
        for c in range(0,histogram.shape[1]):
            print("histogram[",i,",",c,"]:",histogram[i,c])
    plot_histogram(histogram)
if __name__== '__main__':
  main()
