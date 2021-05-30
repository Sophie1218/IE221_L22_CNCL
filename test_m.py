# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:11:42 2021

@author: LENOVO
"""
import pytest

#sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'IE221_Nhom9[ZaloPC_Folder] (1)'))
from main import menu as n
from Kmeans.menu.interface_menu import menu as m

# =============================================================================
# def test_answer():
#     assert n==m
# =============================================================================

def test_answer():
    assert id(n)==id(m)

