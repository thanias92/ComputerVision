# Computer Vision Project Progress Report (25%)

**Project Name**: Pendeteksi Jenis Motor (Motorcycle Type Detection)  
**Student Name**: Bethania Simangunsong  
**Course/Institution**: Computer Vision/Politeknik Caltex Riau  
**Date**: 5/1/2025  
**Progress**: 25% Complete  

## Table of Contents
- [Project Description](#project-description)
- [25% Progress Summary](#25-progress-summary)
- [Data Pipeline](#data-pipeline)
- [Model Experiments](#model-experiments)
- [Next Steps](#next-steps)

## Project Overview
A computer vision system to detect potholes in real-time using YOLO for road maintenance. 

**Key Features Target**:
- Accuracy >70% on motorcycle type

## 25% Progress Summary
✅ **Completed** | ⏳ **In Progress** | ❌ **Pending**

| Task                | Status | Details                          |
|---------------------|--------|----------------------------------|
| Dataset Collection  | ✅     | 640 images from https://universe.roboflow.com/bethaniaworkspace/motorcycledetection-plboa        |
| Annotation          | ⏳     | 640 images labeled (VGG format)  |
| Baseline Model      | ✅     | YOLOv8    |
| Preprocessing       | ⏳     | CLAHE + Gamma correction         |

## Data Pipeline
```python```
## Data Preparation
### Dataset Source
```Roboflow```
https://universe.roboflow.com/bethaniaworkspace/motorcycledetection-plboa
### Dataset Structure
    Pothole-Dataset/
    ├── test/         # Raw road images
    ├── train/        # Enhanced images
    ├── valid/        # Pothole annotations
    └── data.yaml

### Annotation Example
    train: ../train/images
    val: ../valid/images
    test: ../test/images
    names: ['motorBebek', 'motorMatic', 'motorSport', 'motorTrail']
## Model Experiment
### Framework Model 
```YOLOv8``` **Optimal for pothole detection** due to:
| Feature               | Benefit for Pothole Detection       |
|-----------------------|-------------------------------------|
| 🚀 **High Speed**     | 30-50 FPS on mid-range GPUs (crucial for real-time road analysis) |
| 🎯 **Improved Accuracy** | 5-10% higher mAP than YOLOv5 on small objects like potholes |
| 📱 **Multiple Sizes** | Nano (for edge devices) to XLarge (for server processing) |
| 🔧 **Simplified API** | Fewer lines of code for training compared to previous versions |

## Next Step
- Data augmentation (mosaic, rotation)
- Hyperparameter tuning (optimizer, LR)
- Training Model YOLOv8
