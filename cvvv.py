import cv2


img = cv2.imread("C:\\Users\\visha\\Desktop\\IMG_1450.jpg",1)

# cv2.imshow("vishav",img)
# show image


# print(img)
# print matrix


# print(img.shape)
# print rows and columns and rgb

# to resize
resize = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Vishav",resize)

cv2.waitKey(2000)
cv2.destroyAllWindows()
