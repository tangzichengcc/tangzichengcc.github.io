from cv2 import cv2
import  time

# imgName='bigPhoto.jpg'
imgName=input("请输入图片名称：\n")
imgs = cv2.imread(imgName)

#图片缩放至原图的1/4,最邻近插值
resize_img = cv2.resize(imgs, (0, 0), fx=0.20, fy=0.20, interpolation=cv2.INTER_NEAREST)
#resize(InputArray src, OutputArray dst, Size dsize,double fx=0, double fy=0, int interpolation=INTER_LINEAR )
# InputArray src ：输入，原图像，即待改变大小的图像；
# OutputArray dst： 输出，改变后的图像。这个图像和原图像具有相同的内容，只是大小和原图像不一样而已；
# dsize：输出图像的大小，如上面例子（300，300）。
# fx和fy是图像width方向和height方向的缩放比例。
# fx：width方向的缩放比例,fy：height方向的缩放比例
# interpolation（插值）：这个是指定插值的方式，图像缩放之后，肯定像素要进行重新计算的，就靠这个参数来指定重新计算像素的方式，有以下几种：
# INTER_NEAREST - 最邻近插值
# INTER_LINEAR - 双线性插值，如果最后一个参数你不指定，默认使用这种方法
# INTER_CUBIC - 4x4像素邻域内的双立方插值
# INTER_LANCZOS4 - 8x8像素邻域内的Lanczos插值

#重写图片并保存
timeNow=time.strftime("%Y-%m-%d-%H-%M-%S-",time.localtime(int(time.time())))#获取当前时间
print(timeNow+imgName)#生成图片的名字
cv2.imwrite("cv2-"+timeNow+imgName, resize_img)
print("图片保存成功")


