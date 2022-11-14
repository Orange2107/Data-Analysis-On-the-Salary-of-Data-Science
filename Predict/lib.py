# -*- coding = utf-8 -*-
# @Time : 2022/11/12 13:50
# @Author : CZJ
# @File  :   lib.py
# @software : PyCharm
import torch

embedding_dim = 1
hidden_size = 1
dropout = 0.5
bidirectional = True
num_layers = 1
batch_size = 3
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")