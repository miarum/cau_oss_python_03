import math

class line:
    """
    line은 길이에 대한 정보를 저장하는 클래스입니다.
    변수로 __width와 __height가 있고 
    접근하기 위해 set_length,get_length 메소드를 제공합니다.
    """
    __width=0
    __height=0
    def __init__(self,width,height):
        """
        생산자를 통해 초기 __width값과 __height값을 지정합니다.
        """
        self.__width=width
        self.__height=height

    def set_length(self,width,height):
        """
        width,height 값을 수정하는 메소드
        """
        self.__width=width
        self.__height=height

    def get_length(self):
        """
        저장하고 있는 width,height 값을 반환하는 메소드
        """
        return self.__width, self.__height
    
    def area_rectangle(width,height):
        """
        입력받은 width와 height로
        직사각형의 넓이를 구하는 함수
        0이하의 수를 입력 받으면 ValueError
        """
        if width<=0 or height<=0: raise ValueError
        return width*height
    
    def area_ellipse(width,height):
        """
        입력받은 width와 height로 타원의 넓이를 구하는 함수
        0이하의 수를 입력 받으면 ValueError
        """
        if width<=0 or height<=0: raise ValueError
        return width*height*math.pi
    
    def area_right_triangle(width,height):
        """
        입력받은 widght와 height로 정삼각형의 넓이를 구하는 함수
        0이하의 수를 입력 받으면 ValueError
        """
        if width<=0 or height<=0: raise ValueError
        return width*height/2