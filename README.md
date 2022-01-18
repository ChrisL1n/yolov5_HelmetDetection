# yolov5_HelmetDetection

## Discription

This repository aims to predict whether workers wear helmets or not while working on a detect GUI. 

As a detection problem, we use the outstanding framework: yolov5, to make prediction on high accuracy.

Our input files are consist of pictures on size 416x416, each image contains workers with and without helmet. The type of label format is .xml file. To adapt label type with framework yolov5, we do transformation work which you can see in file xml_transfer.py . Also, to reach the goal of productization, we desigh a simple GUI to realize the function of outputing a predict image which contains the detected helmet(face) and the accuracy of prediction according to the chosen input image. After decection, GUI will output a caption to indicate whether anyone in the picture is not wearing a helmet.

This repository is an initial edition, and we think of it as an introductory project for yolov5. Instead of doing refactor or breakthrough on the framework, we focus on the work of making input adaption and the inplementation of detect GUI. Maybe we will fullfill more function in the future.

## Datasets

You can download datasets from Kaggle:
https://www.kaggle.com/andrewmvd/hard-hat-detection

After downloading dataset, you can run this command to transfer xml file to txt file, which adapt to the input format of yolov5 framework:
```bash
python xml_transfer.py
```

## Train

You can follow the [tutorial](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data) of yolov5 repository to train model. For this repository, you can run command:
```bash
# Train on model yolov5s
python train.py --img 416 --batch 16 --epochs 3 --data HelmetDetection.yaml --weights yolov5s.pt
```
Train result will be saved in directory: ./runs/train/exp, and you can get your best train model by accessing ./runs/train/exp/weights/best.pt .

## Detection

* Use bash command

Framework provide a method to make detection on your test picture, you can run command:
```bash
python detect.py --weights [Path to your weight file] --source [Path to your image or directory] --save-txt
```
When using argument save-txt, the detect process will save the predict probabilty and label into output directory: ./runs/detect/exp .

You can also run script file by command:
```bash
bash make_detection.sh [Path to your image or directory]
```
(It contains a line of bash command which is the same as last command, we do this tricky work to help us run detect command inside python file, never mind!)

* Use GUI

We design a GUI to show the result more intuitive, you can run command:
```bash
python detect_gui.py
```
And then a clear and simple GUI will be displayed on your desktop.(No tutorial! It won't be difficult to use, just relax!)

It is worth mentioning that the detect process will cost a lot of time, and we're to lazy to wait for detection(Especially when we are displaying our product to our teacher). Actually, when you click the "detect" button, our code will load the result from existing directory, which indicates that we need to run bash command to detect before clicking this button. To experience the full functionality, you can cancel the comment in function detect() of detect_gui.py:

```python
if os.path.exists(result_dir):
  os.system("rm -r {}".format(result_dir))
file_path = os.path.join(self.input_dir, self.filename)
os.system("bash make_detect.sh {}".format(file_path))
result_file = os.listdir(result_dir)
result_file.remove('labels')
```
