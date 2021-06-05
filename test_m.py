import pytest

#sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'IE221_Nhom9[ZaloPC_Folder] (1)'))
from main import menu as n
from myprogram.menu.interface_menu import menu as m
from myprogram.option1.point import Point

def test_answer():
    assert id(n)==id(m)

def test_distance():
    point2=Point(4,5)
    point1=Point(7,6)
    assert int(point1.distance(point2))==3

def test_update_coordinates():
    point1=Point(7,8)
    point1.update_coordinates(5, 6)
    assert point1.x==5,point1.y==6
    
def test_update_label():
    point1=Point(7,8)
    point1.update_label(1)
    assert point1.label==1

def test_return_coordinates():
    point1=Point(7,8)
    point1.return_coordinates()
    assert point1.x==7,point1.y==8
    
def test_return_label():
    point1=Point(7,8)
    point1.update_label(1)
    assert point1.return_label()==1
    

