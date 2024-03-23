# Slide Detector

Usually instructors only upload their lecture videos online but possibly not their original PPT files, and this application helps to transform lecture videos into PPT slides. Hope you would like it!

Also if you are not familiar with code execution, [Drive](https://drive.google.com/drive/folders/10TZ7bD07nOKC8GSoc_x7Di2dTThquMer?usp=sharing) here provides a .dmg file for MacOS users.

# Usage
```
pip install requirements.txt
python app.py
```
Then you should be able to launch the app.

## Slide Detection

<img width="799" alt="image" src="https://github.com/altis5526/slide_detector/assets/40194798/d4036cc2-a458-44be-9151-dd42830a3549"> 

* The threshold bar can be adjusted to define the sensitivity of our detector (Higher number means higher sensitivity). We recommend sensitivity between 0.90~0.95.
* If the detector falsely detects slides not intented to be saved, you can select the unsaved images by simply mouse click on the detected slide.

## Youtube download
<img width="799" alt="image" src="https://github.com/altis5526/slide_detector/assets/40194798/55b0960b-6f64-48b0-829a-8f42c3dd7bd9"> 

* In most scenario, the lecture video may be uploaded on Youtube. This widget provides a fast way to download your desired videos.

# Reference
[slide-transition-detector](https://github.com/renebrandel/slide-transition-detector)
