#include <stdio.h>

#include <opencv2/core/core.hpp>

#include <opencv2/highgui/highgui.hpp>

#include <opencv2/highgui/highgui_c.h>

#include <opencv2/imgcodecs/imgcodecs.hpp>

#include <opencv2/imgproc/imgproc.hpp>

#include <iostream>

#include <string>

#include <fstream>


using namespace cv;
using namespace std;

int threshold_value = 0;
int threshold_type = 0;;
int
const max_value = 255;
int
const max_type = 8;
int
const max_BINARY_value = 255;

string src_name, src_path, dst_path;
string desktop_path = "C:/Users/vanag/Desktop/";
string src_window_name = "Source image";
string src_gray_window_name = "Gray image";
string dst_window_name = "Tresholded image";
Mat src, src_gray, dst;
void Threshold_Demo(int, void*);

int main() {
    cout << "\n";
    printf("Enter the name of the image with the extension: ");
    getline(cin, src_name);
    src_path = desktop_path.append(src_name);
    dst_path = src_path + ("_tresh.png");
    ifstream ifile;
    ifile.open(src_path);
    if (ifile) {
        cout << "File exists at " << src_path << "\n";
        src = imread(src_path, IMREAD_UNCHANGED);
        if (src.empty()) {
            cout << "... but CV is unable to read it.";
            return 0;
        }
        //resize(src, src, cv::Size(), 0.5, 0.5);
        namedWindow(src_window_name, CV_WINDOW_AUTOSIZE);
        imshow(src_window_name, src);
        waitKey(0);
        cvtColor(src, src_gray, COLOR_BGR2GRAY, 0);
        Threshold_Demo(0, 0);
        namedWindow(dst_window_name, CV_WINDOW_AUTOSIZE);
        createTrackbar("Type", dst_window_name, &threshold_type, max_type, Threshold_Demo);
        createTrackbar("Value:", dst_window_name, &threshold_value, max_value, Threshold_Demo);
        waitKey(0);
        imwrite(dst_path, dst);
        return 0;
    }
    else {
        cout << "File does not exist at " << src_path << "\n";
        return 0;
    }
}
void Threshold_Demo(int, void*) {
    /*
      cv::THRESH_BINARY = 0,
      cv::THRESH_BINARY_INV = 1,
      cv::THRESH_TRUNC = 2,
      cv::THRESH_TOZERO = 3,
      cv::THRESH_TOZERO_INV = 4,
      cv::THRESH_MASK = 7,
      cv::THRESH_OTSU = 8,
     */

    threshold(src_gray, dst, threshold_value, max_BINARY_value, threshold_type);

    imshow(dst_window_name, dst);
}