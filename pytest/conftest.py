# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/24 21:36
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
import pytest


@pytest.fixture(scope="function", params=None, autouse=False,
                ids=None, name=None)
def test():
    print("fixture初始化的参数列表")


@pytest.fixture(scope="module")
def open_51(login):

    name, token = login
    print(f"###用户 {name} 打开51job网站###")


@pytest.fixture(scope="function")
def open_weibo(login):
    name, token = login
    print(f"&&& 用户 {name} 返回微博首页 &&&")
