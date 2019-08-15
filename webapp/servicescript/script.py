# -*- coding: utf-8 -*-
# 服务器执行脚本
import argparse

def script_argv():
    pass


if __name__ == '__main__':
    # 小程序变量传递测试
    parser = argparse.ArgumentParser()
    parser.add_argument_group()
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    parser.add_argument('-gpu', type=str, default=None)
    parser.add_argument('-batch-size', type=int, default=32)
    args = parser.parse_args()
    answer = args.x ** args.y
    if args.verbosity >= 2:
        print("Running '{}'".format(__file__))
    if args.verbosity >= 1:
        print("{}^{} == ".format(args.x, args.y), end="")
    print(answer)
    print(args.gpu)
    # 位置变量以及 键值对变量 调用方法
    # python script.py  -gpu=[1,2]  2 4  -batch-size=10

