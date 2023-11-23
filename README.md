## Canny-edge-detector-and-Harris-corner-detection-using-Python
This work is completed as a part of Course assignment in 3D Computer Vision at IIT Gandhinagar

# Canny Edge Detector:
The code has been written on the basis of the Algorithm taught in the lectures of Computer Vision.

**Algorithm Step by Step:**
1) Sobel edge detection of the Gaussian Blurred image.
2) Magnitude and Direction of the Gradient obtained from the outputs of Step-1.
3) Non-minimal Suppression.
4) Hysterisis thresholding.
5) Edge linking

![edge_detection](https://github.com/vasavamsi/Canny-edge-detector-and-Harris-corner-detection-using-Python/assets/58003228/5e6ebc09-b98d-4769-bcac-d9c46cf35dbb)

# Harris Corner Detection:

The code has been written on the basis of the Algorithm taught in the lectures of Computer Vision.

**Algorithm Step by Step:**
1) Getting the filtered images.
2) Squaring the elements of the formed array.
3) Getting the box filtered images from the output of Step-2
4) Forming the 2x2 matrix from the elements of output of Step-3 to get the eigen values
5) Applying the following formula:
<p align="center">
R(x,y) = λ1λ2 – k(λ1 + λ2)2
</p>

Where λ1 and λ2 are the eigen values of matrix in Step-4 and k is constant (in code taken as 0.06) If R > 0, then it implies that there is a corner at that (x,y) location in the image. In the demo example the code was even able to detect the corners that were not been able to be detected by the inbuilt function. The results as a binary image is as shown below.

![corner detection](https://github.com/vasavamsi/Canny-edge-detector-and-Harris-corner-detection-using-Python/assets/58003228/8d9c485d-9613-488b-8ab8-b7b2e4f255a4)

**Instructions to run the code:**

_Step-1_- Run test_script.py in codes folder.

_Step-2_- Result images will be saved in the same folder itself.

_Step-3_- demo input images are already loaded.

_Step-4_- to test on other images please copy them to the same directory and change the image name in the test_script.py.

**Note:-** 
The output of the Harris_corner_detection would be the binary image showing the corners in white pixel and rest in black.

Thresholds can be changed manually in the edge_detection itself.

The filter sizes used for convolution are fixed.

References:
1) Classnotes
2) Open CV tutorial for the Canny edge detection - https://docs.opencv.org/trunk/da/d22/tutorial_py_canny.html

