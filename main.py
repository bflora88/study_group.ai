import cv2
import numpy as np
import argparse


# given a path, returns an image into a numpy array in BGR format 
def read_img(img_path):
    img = cv2.imread(img_path)
    return img


# displays the given image in a window    
def show_img(img):
    cv2.imshow("test img", img)
    # keeps the window open until any key is pressed, or after 20 secs
    cv2.waitKey(10000)

    
# transform the input image from BGR format to L
def bgr_to_gray(bgr_img):
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)/255.0
    return gray_img

def edge_det(img):
	mat_1=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
	mat_2 = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
	image_transformed= np.zeros(shape=(img.shape))
	for i in range(1,img.shape[0]-1):
		for j in range(1,img.shape[1]-1):
			img_tmp=img[i-1:i+2,j-1:j+2]
			val1 = ((img_tmp*mat_1).sum())**2
			val2 = ((img_tmp*mat_2).sum())**2
			val = (val1+val2)**(1/2)
			if val>0.8:
				image_transformed[i,j] = 1
	return image_transformed
			

def main(args):
    print('img path: {}'.format(args.img_path))
    img = read_img(args.img_path)
    img_grey = bgr_to_gray(img)
    print(img.shape) 
    print(img_grey.shape)
    image_transformed = edge_det(img_grey)
    show_img(image_transformed)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Playground for implementing old school computer vision algos")
    parser.add_argument("--img_path", type=str, default="./imgs/lena.png", help="Path to the test img")
    
    args = parser.parse_args()
    main(args)
