def li_sort(li):
	'''插入排序：
        分成两个序列，假设第0个为有序序列，
	每次将后面无序的第0（整个列表从1开始）个比较，
	判断是否需要交换位置，以此类推
	'''
	l = len(li)
	for j in range(1, l):  #重复while循环对整个列表排序
	    i = j
	    while i>0:  #while循环排序一次
	        if li[i-1] > li[i]:
	            li[i-1], li[i] = li[i], li[i-1]
	            i -=1  #向前继续比较
	        else:
	            break  #没有发生交换，说明
	print(li)

if __name__ == '__main__':
	li = [10,8,9,7,6,5,3,2,1,4]
	li_sort(li)
	
