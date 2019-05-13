## N- Dimensional array
- Các thao tác cơ bản trên mảng nhiều chiều
```
scores = [[34, 56, 23, 89], [11, 45, 76, 34]]
first_arr = np.array(scores) # Tạo mảng
print('In ra array: \n', first_arr)
print('In ra kiểu của các phần tử trong array: ', first_arr.dtype)
print('In ra số dòng của array: ', first_arr.ndim)
print('In ra cấu trúc của dãy: ', first_arr.shape)
x = np.zeros(10)
print('In ra 1 array có 10 phần tử = 0: ', x) # tương tự với ones và twos
print('Ngoài ra còn có thể in ra 1 array có 4 dòng và 3 cột với phần tử toàn bằng 0: \n', np.zeros((4, 3)))

print('nhân 2 mảng với nhau: \n', first_arr * first_arr)
print('trừ 2 mảng với nhau: \n', first_arr - first_arr)
print('chia mảng: \n', 1/(first_arr))

```
![1](https://user-images.githubusercontent.com/45547213/57611937-18a10880-759e-11e9-8ac6-23cf75ac3b4f.PNG)

## Slicing and Indexing
- Slicing và Indexing
```
new_arr = np.arange(12)  # Tạo 1 mảng có 12 phần tử từ 0 đến 11
print('In ra array: \n', new_arr)
print('In ra phần tử thứ 6: ', new_arr[5])
print('In ra phần tử từ thứ 5 đến thứ 9: ', new_arr[4:9])
new_arr[4:9] = 99  # Gán giá trị từ phần tử thứ 5 đến thứ 9 = 99
print('In ra mảng mới: \n', new_arr)
```
![2](https://user-images.githubusercontent.com/45547213/57611976-2787bb00-759e-11e9-8730-7e0496e8f71e.PNG)

- Sự khác biệt giữa array và list
Nếu data trong phần tử của array không sử dụng hàm copy thì bất kì thay đổi nào đến các phần tử trong array sẽ liên quan trực tiếp đến source
```
new_arr = np.arange(12)  # Tạo 1 array có 12 phần tử từ 0 đến 11
print('Array: \n', new_arr)
modi_arr = new_arr[4:9]  # Tạo 1 array mới có các phần tử từ 5 đến 9 thuộc phần tử new_arr
print('In ra modi_arr: \n', modi_arr)
modi_arr[1] = 123456     # Gán giá trị cho phần tử 2 ở modi_arr
print('In ra modi_arr sau khi thay đổi phần tử: \n', modi_arr)
print('Array cũ sau khi phần tử ở array mới được thay đổi: \n', new_arr)
print('Bạn nhìn thấy sự thay đổi chứ')

print('\n \n')
# Còn đây là list

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print('In ra list: ', list1)
modi_list = list1[4:9]
print('In ra modi_list: ', modi_list)
modi_list[1] = 123456
print('In ra modi_list sau khi thay đổi phần tử: ', modi_list)
print('list cũ sau khi phần tử ở list mới được thay đổi: \n', list1)
print('đó là sự khác nhau')
```
![3](https://user-images.githubusercontent.com/45547213/57612222-a0871280-759e-11e9-91ac-5f5300e3696a.PNG)

- Array có thể đại diện cho ma trận
```
matrix_arr = np.array([[3, 4, 5], [6, 7, 8], [9, 5, 1]])
print('In ra ma trận: \n', matrix_arr)
print('In ra dòng 2 của ma trận: ', matrix_arr[1])
print('In ra phần tử ở dòng 1 cột 3: ', matrix_arr[0][2])
print('In ra phần tử ở dòng 1 cột 3: ', matrix_arr[0, 2])
```
![4](https://user-images.githubusercontent.com/45547213/57612227-a1b83f80-759e-11e9-8567-276bfb9bb362.PNG)

- Hàm copy
Khi bạn dùng hàm copy thì array sẽ không bị ảnh hưởng lẫn nhau như trước nữa
```
matrix_arr = np.array([[3, 4, 5], [6, 7, 8], [9, 5, 1]])
copied_values = matrix_arr[0].copy()  # dùng hàm copy để tạo 1 array chứ các phần tử ở dòng 1 của ma trận
matrix_arr[0] = 99  # Thay đổi hết các phần tử ở dòng 1
print("matrix_arr mới: \n{}".format(matrix_arr))
matrix_arr[0] = copied_values  # Gán lại từ đầu
print("matrix_arr again: \n{}".format(matrix_arr))
```
![5](https://user-images.githubusercontent.com/45547213/57612244-ada40180-759e-11e9-8f73-49b4418b5e29.PNG)

- Index và Slicing
```
matrix_arr = np.array([[3, 4, 5], [6, 7, 8], [9, 5, 1]])
print("In ra ma trận gốc: \n{}".format(matrix_arr))
print("In ra dòng 1 đến dòng 2:\n{}".format(matrix_arr[:2]))
print("In ra dòng 0 đến dòng 1 với cột 2 và cột 3 :\n{}".format(matrix_arr[:2, 1:]))
print("In ra phần tử ở dòng 2 và cột 1,2: {}".format(matrix_arr[1, :2]))
print("In ra 3 dòng ở cột 1:\n{}".format(matrix_arr[:, :1]))
```
![6](https://user-images.githubusercontent.com/45547213/57612250-af6dc500-759e-11e9-9c3d-f8eadcc73751.PNG)

- Kiểm tra phàn tử trong array
```
personals = np.array(['Manu', 'Jeevan', 'Prakash', 'Manu', 'Prakash', 'Jeevan', 'Prakash'])
print(personals == 'Manu') # nếu trùng thì nó trả về True còn không trùng trả về False
```

- Kết hợp
```
personals = np.array(['Manu', 'Jeevan', 'Prakash', 'Manu', 'Prakash', 'Jeevan', 'Prakash'])
random_no = random.randn(7, 4)  # Tạo ra ma trận có 7 dòng và 4 cột và giá trị của phần tử được random
print("In ra ma trận: \n", random_no, "\n")
print("In ra các dòng của ma tận với giá trị khi personals trả về True:\n", random_no[personals == 'Manu'])
```

![7](https://user-images.githubusercontent.com/45547213/57612253-b0065b80-759e-11e9-86e2-138d06955bc1.PNG)


## Fancy Indexing
- indexing
```
algebra = random.randn(7, 4)  # Tạo 1 matrix có 7 dòng và 4 cột
for j in range(7):
    algebra[j] = j  # Gán giá trị cho các phần tử
print("Ma trận: \n", algebra, '\n')
print('In ra ma trận: \n', algebra[[4, 5, 1]])
```
![8](https://user-images.githubusercontent.com/45547213/57612292-c6141c00-759e-11e9-9750-11ee33617fb2.PNG)
- Fancy
```
fancy = np.arange(36).reshape(9,4) #reshape is to reshape an array
print("In ra ma trận:\n", fancy)
print("Index: ", fancy[[1, 4, 3, 2], [3, 2, 1, 0]])
# Lấy các phần tử (1,3) (4,2) (3,1) (2,0)
```

![9](https://user-images.githubusercontent.com/45547213/57612294-c7454900-759e-11e9-83ee-c89c2ab58e7a.PNG)

- Hàm ix_
```
fancy = np.arange(36).reshape(9,4) #reshape is to reshape an array
print('Ma trận gốc: \n', fancy)
print('Ma trận dùng hàm ix_: \n', fancy[np.ix_([1, 4, 8, 2], [0, 3, 1, 2])])
```

![10](https://user-images.githubusercontent.com/45547213/57612296-c8767600-759e-11e9-8a0f-9e37fa9cddc6.PNG)
## universal functions
Các hàm tính toán kiểu sqrt, exp
Hình 11 Hình 12
![11](https://user-images.githubusercontent.com/45547213/57612298-c9a7a300-759e-11e9-9389-4047f16a924f.png)
![12](https://user-images.githubusercontent.com/45547213/57612303-cb716680-759e-11e9-8246-328fa1f0f422.png)
## Data processing using Arrays
- Hàm meshgrid
```
mtrices = np.arange(-5, 5, 1)
x, y = np.meshgrid(mtrices, mtrices) #mesh grid function takes two 1 d arrays and produces two 2d arrays
print("Matrix values of y: \n{}\n".format(y))
print("Matrix values of x: \n{}\n".format(x))
```

![13](https://user-images.githubusercontent.com/45547213/57612306-cca29380-759e-11e9-8ad4-d7bd5eb8652e.PNG)

- Hàm zip, Where
```
x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([6, 7, 8, 9, 10])
cond = [True, False, True, True, False]
z1 = [(x, y, z) for x, y, z in zip(x1, y1, cond)]
print(z1)
print(np.where(cond, x1, y1))  # True sẽ lấy phần tử của x1 còn False sẽ lấy phần tử của y1
```
![Hình 14](https://user-images.githubusercontent.com/45547213/57612312-cf04ed80-759e-11e9-9c84-ed250e22f226.PNG)

## Statistical methods
- mean, sum, cumsum
```
thie = np.random.randn(5,5)
print('Trung bình của ma trận: ', thie.mean())
print('Trung bình của ma trận: ', np.mean(thie))
print('Tổng của ma trận: ', thie.sum())
```
axis là 1 tham số của hàm sum và cumsum nếu axis = 0 thì là tính tổng dòng còn = 1 thì tính tổng cột

## Sorting
- Hàm sort
- Hàm unique loại các giá trị tùng lặp
