# -*- coding = utf-8 -*-
# @Time : 2022/11/12 15:50
# @Author : CZJ
# @File  :   testLstm.py
# @software : PyCharm
# -*- coding = utf-8 -*-
import torch
from torch.nn import Embedding, LSTM
import pickle
import myModel
import numpy
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.preprocessing import LabelEncoder as LE
import pandas as pd
from sklearn.model_selection import cross_val_predict, train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np


def lstmModel():
    batch_size = 10        # 一组几个
    seq_len = 20           # 每个样本的长度
    num_embedding = 100    # 字典的长度？？
    embedding_dim = 30     # 扩展的长度也是每一次LSTM单元输入的大小
    hidden_size =8         # 隐藏层数量
    num_layers = 1

    # [10, 20] 10表示把总数据分成几个batch，20指阅读多少数字。
    input = torch.ones([batch_size, seq_len], dtype=torch.long)
    print("input size: ", input.size())
    print("class", type(input))

    # 创建embedding 词嵌入层
    embed = Embedding(num_embeddings=num_embedding, embedding_dim=embedding_dim)
    input_embed = embed(input)#[batch_size,seg_len,embedding_dim]  #[10,20,30]

    #lstm
    rnn = LSTM(input_size=embedding_dim, hidden_size=hidden_size, num_layers=num_layers, bias=True, batch_first=True, bidirectional=True)
    output, (hn, cn) = rnn(input_embed)

    print(output.size())  # [batch, sequence, hidden_size] output每一次循环都有一次输出
    print(hn.size())    # [num_layer,batch,hidden_size] 贯穿始终，和层数有关
    print(cn.size())

    # 单向LSTM
    # 当t等于最后时刻得到的输出是最上层输出，一个t传入一个batch 。Batch_First = true
    # lastoutput = output[:, -1, :]   # -1代表是最后一个序列
    # lasthn = hn[-1, :, :]   # 因为只有一层，所以layout无所谓
    # print(lastoutput.eq(lasthn))


    # 双向LSTM
    # Output是最后产生的输出， 最后的hidden_size需要乘2。   hidden ： [正向,反向]
    # o1 = output[:, -1, :8]  #正向的最后一个输出，在最底层 squence 最大
    # o2 = output[:, 0, 8:]  #反向的最后一个输出，在第一层  squence 最小
    # hidden在 layout上*2表示双向。
    # hidden在每一层都有进行输出
    # h1 = hn[-2, :, :]  # layout 第二层
    # h2 = hn[-1, :, :]  # layout 第一层
    # print(o1.eq(h1))


def dataSet():

    csv_path = '../ds_salaries.csv'
    df = pd.read_csv(csv_path)
    df.drop(columns=['Unnamed: 0', 'salary'], inplace=True)

    catcol = ["experience_level", "employment_type", "job_title", "employee_residence",
              "remote_ratio", "company_location", "company_size", 'work_year', 'salary_in_usd', 'salary_currency']
    encode = LE()
    for col in catcol:
        if col == 'experience_level' and 'company_size':
            continue
        df[col] = encode.fit_transform(df[col])  # 归一化
        str = 'pickle/'+col + '.pickle'
        doc = open(str, "wb")
        pickle.dump(encode, doc)  # 保存机型编码模型
        doc.close()

    df['experience_level'] = df['experience_level'].replace('EN', 0)
    df['experience_level'] = df['experience_level'].replace('MI', 1)
    df['experience_level'] = df['experience_level'].replace('SE', 2)
    df['experience_level'] = df['experience_level'].replace('EX', 3)

    df['company_size'] = df['company_size'].replace('S', 0)
    df['company_size'] = df['company_size'].replace('M', 1)
    df['company_size'] = df['company_size'].replace('L', 2)

    x = df[["experience_level", "employment_type", "job_title", "employee_residence",
             "remote_ratio", "company_location", "company_size", 'work_year',
            'salary_currency']]

    y = df['salary_in_usd']
    input_train, input_test, output_train, output_test = train_test_split(x, y, test_size=0.2, random_state=1)

    # 转换成tensor
    input_train = torch.from_numpy(input_train.values)
    input_test = torch.from_numpy(input_test.values)
    output_train = torch.from_numpy(output_train.values)
    output_test = torch.from_numpy(output_test.values)

    return input_train, input_test, output_train, output_test


if __name__ == '__main__':
    #input_train, input_test, output_train, output_test = dataSet()
    #lstmModel(input_train, input_test, output_train, output_test)
    lstmModel()