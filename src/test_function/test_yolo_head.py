from network_function import *
from detect_function import *
from config import anchors
# TEST BUILD NETWORK
import matplotlib.pyplot as plt
import numpy as np
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


def test():
    input1 = tf.random_normal([1, 13, 13, 255], mean=1, stddev=4, seed=1)

    mask = [[6, 7, 8], [3, 4, 5], [0, 1, 2]]
    input_shape = np.array([416, 416])
    a, b, c, d = yolo_head(input1, anchors[mask[0]], 80, input_shape)

    # x = tf.shape(a)
    writer = tf.summary.FileWriter('./graphs', tf.get_default_graph())
    # python network_function.py
    # tensorboard --logdir="./graphs" --port 6006
    # these log file is saved in graphs folder, can delete these older log file
    # porte 6006 may be change
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    with tf.Session(config=config) as sess:
        sess.run(tf.global_variables_initializer())
        print(sess.run(tf.shape(input1)))
        print(sess.run(tf.shape(a)))
        print(sess.run(a[0][0][0][0][:]))
        print(sess.run(tf.shape(b)))
        print(sess.run(b[0][0][0][0][:]))
        print(sess.run(tf.shape(c)))
        print(sess.run(c[0][0][0][0][:]))
        print(sess.run(tf.shape(d)))
        print(sess.run((d[0][0][0][0][:])))
    writer.close()
    sess.close()
    return 0


test()