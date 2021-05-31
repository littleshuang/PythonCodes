#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import shutil
import re                           # 正则表达式库
import jieba                        # 结巴分词
import jieba.posseg                 # 词性获取
import collections                  # 词频统计库
import numpy                        # numpy数据处理库
from PIL import Image               # 图像处理库
import wordcloud                    # 词云展示库
import matplotlib.pyplot as plt     # 图像展示库（这里以plt代表库的全称）


sys.path.append("../..")
sys.path.append("..")

# 相关变量
UserDict = 'file/用户词典.txt'             # 用户词典
StopWords = 'file/停用词库.txt'            # 停用词库
CountNumber = 100                        # 统计个数
Output = '词频.txt'                       # 输出文件
Background = 'file/background.jpg'       # 词频背景


def read_and_cut_word(file):
    """
    读取file文件并进行分词，返回分词后的有效词汇列表
    """
    # 读取文件
    string_data = ''
    try:
        with open(file, 'r', encoding='UTF-8') as fn:
            string_data = fn.read()                     # 读出整个文件
    except IOError:
        print('Open file %s meets IOError' % file)

    # 文本预处理
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')  # 定义正则表达式匹配模式（空格等）
    string_data = re.sub(pattern, '', string_data)      # 将符合模式的字符去除

    # 动态调整词典
    # jieba.suggest_freq('小小花', True)                 # True表示该词不能被分割，False表示该词能被分割

    # 添加用户词典
    jieba.load_userdict(UserDict)

    # 文本分词
    seg_list_exact = jieba.cut(string_data, cut_all=False, HMM=True)  # 精确模式分词+HMM

    object_list = []
    # 去除停用词,即去掉一些意义不大的词，如标点符号、嗯、啊等
    with open(StopWords, 'r', encoding='UTF-8') as meaninglessFile:
        stopwords = set(meaninglessFile.read().split('\n'))
    stopwords.add(' ')
    for word in seg_list_exact:         # 循环读出每个分词
        if word not in stopwords:       # 如果不在去除词库中
            object_list.append(word)    # 分词追加到列表
    return object_list


def word_frequency_count_and_output(word_list, number, output_file_name):
    """
    从给定词语列表object_list中统计前number个最高频的词汇写入name文件中
    """
    word_counts = collections.Counter(word_list)      # 对分词做词频统计
    word_counts_top = word_counts.most_common(number)   # 获取前number个最高频的词

    # 输出至工作台，并导出“词频.txt”文件
    print('\n词语\t词频')
    print('——————————')

    with open(output_file_name, 'w', encoding='UTF-8') as file_out:
        # 创建文本文件；若已存在，则进行覆盖
        file_out.write('词语\t词频\n')
        file_out.write('——————————\n')
        count = 0
        for TopWord, Frequency in word_counts_top:      # 获取词语和词频
            for POS in jieba.posseg.cut(TopWord):       # 获取词性
                if count == number:
                    break
                if Frequency < 2:
                    break
                print(TopWord + '\t', str(Frequency))  # 逐行输出数据
                file_out.write(TopWord + '\t' + str(Frequency) + '\n')  # 逐行写入str格式数据
                count += 1


def make_word_cloud(word_list, output_file_name):
    # 词频展示
    print('\n开始制作词云……')                         # 提示当前状态
    word_counts = collections.Counter(word_list)
    mask = numpy.array(Image.open(Background))      # 定义词频背景
    wc = wordcloud.WordCloud(
        font_path='file/simfang.ttf',               # 设置字体（这里选择“仿宋”）
        background_color='white',                   # 背景颜色
        mask=mask,                                  # 文字颜色+形状（有mask参数再设定宽高是无效的）
        max_words=CountNumber,                      # 显示词数
        max_font_size=150                           # 最大字号
    )

    wc.generate_from_frequencies(word_counts)       # 从字典生成词云
    wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))  # 将词云颜色设置为背景图方案
    plt.figure('词云')                               # 弹框名称与大小
    plt.subplots_adjust(top=0.99, bottom=0.01, right=0.99, left=0.01, hspace=0, wspace=0)  # 调整边距
    plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')  # 处理词云
    plt.axis('off')                                 # 关闭坐标轴
    print('制作完成！')                               # 提示当前状态
    # plt.show()
    plt.savefig(output_file_name)


def main():
    cur_dir = os.getcwd()
    file_dir = os.path.join(cur_dir, 'file')
    result_dir = os.path.join(cur_dir, 'result')
    files = ['在那儿.txt', '我的物品.txt', '收哪儿.txt', '收纳盒子.txt', '整理猫儿.txt',
             '有物.txt', '红线.txt', 'where.txt', 'all.txt']

    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
    os.mkdir(result_dir)

    for file in files:
        word_lists = read_and_cut_word(os.path.join(file_dir, file))
        word_frequency_count_and_output(word_lists, CountNumber, os.path.join(result_dir, file))
        make_word_cloud(word_lists, os.path.join(result_dir, file.replace('.txt', '.png')))


if __name__ == '__main__':
    main()
