import cv2
import numpy as np

cmDeepGreen = 21;
cmOcean = 5;
cmHot = 11;
imagePath = "D:\\Dundee OneDrive\\OneDrive - University of Dundee\\PhD\\Code\\20180228_EVLP8\\Imaging Data\\2018-02-28_13-59-53\\"

imageGreen = cv2.imread(imagePath + "2018-02-28_13-59-53_00160.tif", 0);
imageRed = cv2.imread(imagePath + "2018-02-28_13-59-53_00161.tif", 0);
imageNIR = cv2.imread(imagePath + "2018-02-28_13-59-53_00162.tif", 0);

#THIS WORKS!!!!
#H = np.zeros((256,1),np.uint8);
#S = np.zeros((256,1),np.uint8);
#V = np.zeros((256,1),np.uint8);

#for i in range(0,256):
#    H[i,:] = 180;

#    if i > 127:
#        S[i,:] = S[i-1,:]-2;
#    else:
#        S[i,:] = 255;


#    if i < 127:
#        V[i,:] = i*2;
#    else:
#        V[i,:] = 255;

#hsv = cv2.merge((H,S,V))
#colourMap = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
#cv2.imshow("BGR", colourMap)

#finalImage = cv2.applyColorMap(imageGreen, colourMap);
#cv2.imshow("Final image", finalImage)



#Colour wheel code!
H = np.zeros((256,180),np.uint8);
S = np.zeros((256,180),np.uint8);
V = np.zeros((256,180),np.uint8);

for h in range(0,180,1):
    start = h;
    end = h + h;
    for i in range(0,256):
        H[i,start:end] = h;

        if i > 128:
            S[i,start:end] = S[i-1,start:end]-2;
        else:
            S[i,start:end] = 255;

        if i < 128:
            V[i,start:end] = i*2;
        else:
            V[i,start:end] = 255;

hsv = cv2.merge((H,S,V))
colourWheel = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("Colour Wheel", colourWheel)








#zeros = np.zeros(imageGreen.shape[:2], dtype="uint8");

#smooth images
#imageGreenSmooth = cv2.GaussianBlur(imageGreen, (31,31), 0);
#cv2.imshow("Smoothed", imageGreenSmooth)

#cv2.imshow("Red", cv2.merge([zeros,zeros,imageRed]))

#Display standard image
#cv2.imshow("Image Green", imageGreen);
#cv2.imshow("Image Red", imageRed);
#cv2.imshow("Image NIR", imageNIR);

#Apply colour map to images
#imageGreenColourmap = cv2.applyColorMap(imageGreen, cmDeepGreen);
#imageRedColourmap = cv2.applyColorMap(imageRed, cmHot);
#imageNIRColourmap = cv2.applyColorMap(imageNIR, cmOcean);

#merge colour map image
#Uses BRG colour space
#imageChannels = [imageNIR2d, imageGreen2d, imageRed2d]
#autoMerged = cv2.merge(imageChannels);


#manualMerged = (imageNIRColourmap + imageGreenColourmap + imageRedColourmap)
#manualMerged = cv2.addWeighted(imageGreenColourmap, 0.5, imageRedColourmap, 0.5, 0.0)
#manualMergedNew = cv2.addWeighted(manualMerged, 0.5, imageNIRColourmap,0.5, 0.0)

#cv2.imshow("Auto Merged", autoMerged);
#cv2.imshow("Manual Merged", manualMergedNew);

#Display colour map images and merged image
#cv2.imshow("Green Colourmap", imageGreenColourmap);
#cv2.imshow("Red Colourmap", imageRedColourmap);
#cv2.imshow("NIR Colourmap", imageNIRColourmap);
#cv2.imshow("Red Image", imageRed);
#cv2.imshow("NIR Image", imageNIR);



cv2.waitKey(0);
