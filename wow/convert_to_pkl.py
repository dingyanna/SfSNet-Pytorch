# coding=utf8
from __future__ import absolute_import, division, print_function

import sys
import os
import numpy as np
import pickle as pkl
import traceback


CAFFE_ROOT = "/home/creator/Apps/caffe"
sys.path.insert(0, os.path.join(CAFFE_ROOT, 'python'))
import caffe

# deploy文件
MODEL_FILE = 'SfSNet_deploy.prototxt'
# 预先训练好的caffe模型
PRETRAIN_FILE = 'SfSNet.caffemodel.h5'


if __name__ == '__main__':
    # 让caffe以测试模式读取网络参数
    net = caffe.Net(MODEL_FILE, PRETRAIN_FILE, caffe.TEST)
    name_weights = {}
    print(len(net.params.keys()))
    # 遍历每一层
    for param_name in net.params.keys():
        name_weights[param_name] = {}
        # 权重参数
        weight = net.params[param_name][0].data
        name_weights[param_name]['weight'] = weight
        print(param_name, weight.shape)
        try:
            # 偏置参数
            bias = net.params[param_name][1].data
            print(param_name, bias.shape)
            name_weights[param_name]['bias'] = bias
        except:
            traceback.print_stack()
            pass
    with open('weights.pkl', 'wb') as f:
        pkl.dump(name_weights, f, protocol=2)
