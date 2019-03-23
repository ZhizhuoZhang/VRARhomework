## 利用pyopengl和freeglut实现相机模型

### 运行环境
ubuntu16.04

python:3.5.2:
* numpy库
* 3.7版本在下载PyOpenGL_accelerate时报错


### 安装pyopengl
    $ pip install PyOpenGL PyOpenGL_accelerate
更多下载细节参考[pyopengl官网](http://pyopengl.sourceforge.net/)

### 安装freeglut
* demo中使用的是freeglut窗口工具包，pyopengl官网貌似只支持glut和freeglut,有兴趣的同学可以尝试使用其他的窗口工具包,例如glfw
* 如果同学你的系统是windows，那么你不需要再去安装freeglut，win32和win64的pyopengl安装包含了glut

安装freeglut

    $ apt-get install freeglut3-dev
    
### 关于demo
* 主要的两个函数gluLookAt和gluPerspective,gluLookAt用来设置视图变换,gluPerspective设置投影变换
* demo中只是画了一个简单的立方体，有兴趣的同学可以利用着色器和纹理来创建更加美观的模型
相关函数请参考[pyopengl文档](http://pyopengl.sourceforge.net/documentation/manual-3.0/index.html)

如果在安装环境和运行demo的过程中有问题，请在issues中提出





