# Numpy : array
# Pandas : ตาราง
"""
-คำนวณ array (vector & matrix)
-เก็บข้อมูลได้ประเภทเดียว ขึ้นกับ datatype
-dtype
('unint8 - จน.เต็ม'
'float32 - จน.ทศนิยม'
bool - True, False)
"""
# 0D Vector
"""
[v]
dim([v]) = 1
"""
# 1D Vector
"""
v = [v1,v2,v3,...,vn]
dim([v]) = n
"""
# 2D Vector (matrix)
"""
v = [1 2 3
    a b c] #2แถว 3คอลัมน์
dim([v]) = (2,3)
"""
# 3D Vector
"""
v = [[[1 2 3]
    [a b c]
    [d e f]]
     
    [[1 2 3]
    [a b c]
    [d e f]]] #3แถว 3คอลัมน์ ลึก2
dim([v]) = (2,3,3)
"""
# image - [[R][G][B]] - dim(I) = (3,24,20) -> (RGB,แถว(สูง),คอลัมน์(กว้าง))

import numpy as np

# 0D array
a0 = np.array([5])
print(a0) #not list = numpy array

# 1D array
a1 = np.array([1,2,3])
print(a1)

# 2D array
a2 = np.array([[1,2,3],
              [4,5,6]])
print(a2)

# arrange
d = np.arange(2,10,2) #2 4 6 8
print(d)

# zero
e = np.zeros(3) #1D
print(e)
e = np.zeros((2,3)) #2D
print(e)

# one
f = np.ones((3,4,5)) #3D
print(f)

# random
g = np.random.rand(5) #0-1 *only array 1D vector*
print(g)

# using dtype
h = np.ones((3,4,5)) #float64
h = np.ones((3,4,5), dtype=np.uint8)
print(h)
print(h.dtype) #uint8

h_128bit = np.array(h, dtype=np.uint16)
print(h_128bit.dtype) #uint16

# check shape
print(h.shape) #(3, 4, 5)