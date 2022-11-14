# -*- coding = utf-8 -*-
# @Time : 2022/11/12 13:45
# @Author : CZJ
# @File  :   myModel.py
# @software : PyCharm
import torch.nn as nn
import lib as li

class Mymodel(nn.Module):

    def __init__(self) -> None:
        super(Mymodel, self).__init__()
        #   词嵌入层
        #self.embedding = nn.Embedding(len(li.ws), embedding_dim=li.embedding_dim)  # 输入字典大小、产出向量大小

        #   gru的输入: [batch, squence , embedding]
        self.salary_gru = nn.GRU(input_size=li.embedding_dim, batch_first=True, hidden_size=li.hidden_size, dropout=li.dropout, bidirectional=li.bidirectional, num_layers=li.num_layers)
        self.dense2 = nn.Linear(li.hidden_size, li.hidden_size)

