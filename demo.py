from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

#绘画模型
def draw():
    global angle
    # 设置渲染背景
    glClearColor(0.2,0.3,0.3,1.0)
    #
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    # 绘制立方体
    glBegin(GL_QUADS)
    # 绘制前面
    glColor3f(1,0,0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    # 绘制后面
    glColor3f(1, 1, 1)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    # 绘制顶面
    glColor3f(0, 0, 1)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    # 绘制顶面
    glColor3f(0, 1, 0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    # 绘制右面
    glColor3f(1, 0, 0.5)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    # 绘制左面
    glColor3f(0, 1, 0.5)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    # 结束绘制
    glEnd()

    #设置相机位置
    z = -5 * np.cos(angle * 3.14 / 180)
    x = 5 * np.sin(angle * 3.14 / 180)
    y = 0
    angle += 0.05
    while angle > 360:
        angle -= 360
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        x, y, z,
        0, 0, 0,
        0, 1, 0,
    )
    # 刷新缓存
    glFlush()



#关闭窗口
def close(key,x,y):
    if key==b'\x1b':
        glutDestroyWindow(win_id)

# 初始化相机
def init_camera():
    # 设置相机位置
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        0,0,-5,
        0,0,0,
        0,1,0,
    )
    # 设置透视投影
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(100,1,0.5,100)

if __name__=='__main__':
    angle=0
    # 初始化glut窗口
    glutInit()
    # 设置窗口显示模式：RGBA四通道|单缓存|深度
    glutInitDisplayMode( GLUT_RGBA| GLUT_SINGLE |GLUT_DEPTH)
    # 初始化窗口大小
    glutInitWindowSize(1000, 800)
    # 创建窗口
    win_id=glutCreateWindow("CUBE")
    # 注册键盘事件
    glutKeyboardFunc(close)
    # 初始化相机
    init_camera()
    # 设置渲染函数
    glutDisplayFunc(draw)
    # 设置窗口空闲时函数
    glutIdleFunc(draw)
    # 开启深度测试
    glEnable(GL_DEPTH_TEST)
    # 开启窗口主循环
    glutMainLoop()