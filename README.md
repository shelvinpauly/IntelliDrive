# IntelliDrive

This project develops an end-to-end pipeline for detecting and classifying traffic signs, lights, and lane markings from dashboard camera feeds. The integrated system consists of:

## Traffic Sign Detection

- Implements region of interest algorithm to identify potential sign locations  
- YOLOv5 model trained on LISA traffic sign dataset
- Model inference on ROI patches for real-time sign detection and classification

## Traffic Light Detection 

- Color segmentation generates ROI patches for potential light locations
- CNN model trained and run on ROI patches to classify light colors

## Lane Detection

- Perspective transform to bird's eye view for detecting lane markings   
- Hough transform to identify lane lines and boundaries
- Radius of curvature analysis to predict upcoming turns

## Integrated Pipeline

- ROI algorithms reduce search space and enable real-time performance
- Shared CNN models for traffic lights and signs classification  
- Homography for lane marking detection in original view

## Performance Metrics

- Latency of ~20ms per frame for traffic sign and light detection
- Successful lane marking detection under challenging conditions

## Discussion 

- Integrated system combines algorithms optimized for different tasks
- Modular design allows swapping components like models and algorithms
- Further work needed for optimal real-time performance and accuracy  

## References

[1] Kulkarni et al., Traffic Light Detection using CNNs
[2] Lopez-Montiel et al., Traffic Sign Detection Evaluation  
[3] Lane Detection Project Report

Let me know if you would like me to modify or expand this integrated traffic detection system README further.
