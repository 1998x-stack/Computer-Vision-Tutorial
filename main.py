import os

# JSON对象
lectures = {
    "01_Course Introduction": ["Overview of computer vision"],
    "02_Image Filtering": ["Image transformations", "point image processing", "linear shift-invariant image filtering", "convolution", "image gradients"],
    "03_Image Pyramids and Frequency Domain": ["Image downsampling", "aliasing", "Gaussian image pyramid", "Laplacian image pyramid", "Fourier series", "frequency domain", "Fourier transform", "frequency-domain filtering", "sampling"],
    "04_Hough Transform": ["Finding boundaries", "line fitting", "line parameterization", "Hough transform", "Hough circles"],
    "05_Detecting Corners": ["Visualizing quadratics", "Harris corner detector", "multi-scale detection"],
    "06_Feature Detectors and Descriptors": ["Designing feature descriptors", "MOPS descriptor", "GIST descriptor", "Histogram of Textons descriptor", "HOG descriptor", "SIFT"],
    "07_2D Transformations": ["2D transformations", "projective geometry", "classification of 2D transformations", "determining unknown 2D transformations"],
    "08_Image Homographies": ["Panoramas", "Image homographies", "Computing with homographies", "direct linear transform (DLT)", "random sample consensus (RANSAC)"],
    "09_Geometric Camera Models": ["Pinhole camera", "accidental pinholes", "camera matrix"],
    "10_Geometric Camera Models (cont.)": ["Review of camera matrix", "perspective", "other camera models", "pose estimation"],
    "11_Two-View Geometry": ["Triangulation", "epipolar geometry", "essential matrix", "fundamental matrix", "8-point algorithm"],
    "12_Stereo": ["Revisiting triangulation", "disparity", "stereo rectification", "stereo matching", "improved stereo matching"],
    "13_14_Radiometry and Reflectance": ["Appearance phenomena", "measuring light and radiometry", "reflectance and BRDF"],
    "15_Photometric Stereo": ["Notes about radiometry", "the n-dot-l model", "photometric stereo", "uncalibrated photometric stereo", "generalized bas-relief ambiguity", "shape from shading"],
    "16_17_Digital Photography": ["Imaging sensor primer", "color sensing in cameras", "in-camera image processing pipeline", "radiometric calibration"],
    "18_19_Image Classification": ["Introduction to learning-based vision", "image classification", "bag-of-words", "K-means clustering", "classification", "K-nearest neighbors", "naive Bayes", "support vector machines"],
    "20_21_Neural Networks": ["Perceptron", "neural networks", "training perceptrons", "gradient descent", "backpropagation", "stochastic gradient descent"],
    "22_23_Convolutional Neural Networks": ["Some notes on optimization", "convolutional neural networks", "training ConvNets"],
    "24_Optical Flow": ["Intro to vision for video", "optical flow", "constant flow", "Horn-Schunck flow"],
    "25_26_Alignment and Tracking": ["Motion magnification using optical flow", "image alignment", "Lucas-Kanade alignment", "Baker-Matthews alignment", "inverse alignment", "KLT tracking", "mean-shift tracking", "modern trackers"],
    "27_Segmentation and Graph-based Techniques": ["Segmentation", "image as a graph", "shortest graph paths and intelligent scissors", "GrabCut"],
    "28_Wrap-up": []
}

# 创建目录和文件
for lecture_id_name, contents in lectures.items():
    lecture_id_name = lecture_id_name.replace(" ", "_").replace("-", "_").replace(",", "").replace("(", "").replace(")", "")
    # 创建目录
    os.makedirs(lecture_id_name, exist_ok=True)
    for content in contents:
        # 文件名不能有空格和特殊字符，替换为下划线
        file_name = content.replace(" ", "_").replace("-", "_").replace(",", "") + ".py"
        file_path = os.path.join(lecture_id_name, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"# {content}\n\n")
            file.write(f'"""\nLecture: {lecture_id_name}\nContent: {content}\n"""\n\n')
        
    readme_file_path = os.path.join(lecture_id_name, "README.md")
    with open(readme_file_path, 'w', encoding='utf-8') as file:
        file.write(f"# {lecture_id_name}\n\n")
        file.write(f'"""\nLecture: {lecture_id_name}\n"""\n\n')
        for content in contents:
            file.write(f"## {content}\n\n")



# 创建目录和文件并生成README.md
with open("README.md", 'w', encoding='utf-8') as readme_file:
    readme_file.write("# Computer Vision\n\n")
    readme_file.write("This is a repository for computer vision learning.\n\n")
    
    for lecture_id_name, contents in lectures.items():
        lecture_id_name = lecture_id_name.replace(" ", "_").replace("-", "_").replace(",", "").replace("(", "").replace(")", "")
        # 创建目录
        os.makedirs(lecture_id_name, exist_ok=True)
        
        # 在README中添加章节标题
        readme_file.write(f"## {lecture_id_name}\n\n")
        
        for content in contents:
            # 文件名不能有空格和特殊字符，替换为下划线
            file_name = content.replace(" ", "_").replace("-", "_").replace(",", "").replace("(", "").replace(")", "") + ".py"
            file_path = os.path.join(lecture_id_name, file_name)
            
            # 创建文件并写入初始内容
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {content}\n\n")
                file.write(f'"""\nLecture: {lecture_id_name}\nContent: {content}\n"""\n\n')
            
            # 在README中添加文件链接
            readme_file.write(f"- [{content}](./{lecture_id_name}/{file_name})\n")
        
        # 添加空行以分隔不同的lecture
        readme_file.write("\n")

print("目录和文件创建完成。")