# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/25 23:08
# @version: 1.0.2
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
import pytest


@pytest.mark.parametrize("open")
class TestWeibo:
    def test_case1_01(self, open_weibo):
        print("查看最近微博热搜")
