# Gender  prediction fine tuning


[Source Blog](https://deeplearningsandbox.com/how-to-use-transfer-learning-and-fine-tuning-in-keras-and-tensorflow-to-build-an-image-recognition-94b0b02444f2)

### Requiremnets

look at requirements.txt
```
opencv
```
```
keras
```
```
tensorflow
```
### To Train

**to train**  = python fine-tune.py --train_dir "data/images/train" --val_dir "data/images/test"

**to test with certain pics** = python predict.py --model "model/vggface-ft_gender.h5" --image "a.jpg"

**to test with web-cam** = python cam.py




### [Current Work](https://gitlab.com/Israel777/age_and_gender_experements)
