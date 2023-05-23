"""
figure 모듈은 도형의 넓이 함수와 클래스를 제공하는 모듈입니다.
line class에서 도형의 길이를 설정,수정하고
area_square, area_circle, area_regular_triangle 함수에서 
정사각형, 원, 정삼각형 모양의 도형 넓이를 반환합니다.
"""
import math

class line:
    __length=0
    def __init__(self,length):
        """
        초기 length값은 받습니다
        """
        self.__length=length
    def set_length(self,length):
        """
        length의 값을 수정합니다.
        """
        self._length=length
    def get_length(self):
        """
        저장된 length 값은 반환합니다.
        """
        return self.__length
    def area_square(length):
        """
        정사각형의 넓이를 구하는 함수
        """
        return length*length
    def area_circle(length):
        """
        정삼각형의 넓이를 구하는 함수
        """
        return length*length*math.pi
    def area_regular_triangle(length):
        """
        원의 넓이를 구하는 함수
        """
        return length*length*math.sqrt(3)/4
    