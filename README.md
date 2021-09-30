How to use this:
`git clone https://github.com/Pythonic456/ImagePredict_ClassicalAI`
Now you need to train it, have at least 1 PNG greyscale image (8 bit preferred), 100x100 pixels:
```
pi@raspberrypi4b:~ $ python3 main.py
User input (a) or data input (b) or drive (c): b
Full file location please: /home/pi/Pictures/test.jpg  # < insert filename to image here
pi@raspberrypi4b:~ $
```
Now to "drive" the program:
```
pi@raspberrypi4b:~ $ python3 main.py
User input (a) or data input (b) or drive (c): c
What filename to save as?test.png
10000
pi@raspberrypi4b:~ $
```

This is nowhere near working well yet, I need some help on a this:

The program already predicts one pixel after one pixel,
can someone help with predicting the next pixel based on what the
previous pixel was and the pixel above it (100 pixels before it in this case).

`test.png` is as far as I have got at the moment.
