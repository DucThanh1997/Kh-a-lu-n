## Series
- Định nghĩa
Series là một mảng một chiều giống như đối tượng chứa một mảng dữ liệu
```
import pandas as pd
from pandas import Series, DataFrame

mjp = Series([5, 4, 3, 2, 1])
print("In ra  series và kiểu dữ liệu của values:\n", mjp)
print("In ra  giá trị của series: \n", mjp.values)
print("In ra cách index cho mỗi values và cách sắp đặt: ", mjp.index, '\n')

jeeva = Series([5, 4, 3, 2, 1, -7, -29], index=['a', 'b', 'c', 'd', 'e', 'f', 'h'])
print('In ra jeeva:\n', jeeva)
print('In ra giá trị của phần tử a', jeeva['a'])
print("In ra  giá trị của jeeva: ", jeeva.values)
print("In ra cách index cho mỗi values và cách sắp đặt", jeeva.index)
```


![image](https://user-images.githubusercontent.com/45547213/57614066-96671300-75a2-11e9-8958-926527d8ce50.png)

- Slicing 
```
jeeva = Series([5, 4, 3, 2, 1, -7, -29], index=['a', 'b', 'c', 'd', 'e', 'f', 'h'])
jeeva['d'] = 9  # gán giá trị số 9 cho jeeva['d']
print("In ra series: \n", jeeva)
print("jeeva từ a đến c: ", jeeva[['a', 'b', 'c']])
print("In ra những phần tử có giá trị lớn hơn 0: ", jeeva[jeeva > 0])
```

![image](https://user-images.githubusercontent.com/45547213/57614792-48eba580-75a4-11e9-9c8d-afa57710c76b.png)

- Math
```
jeeva = Series([5, 4, 3, 2, 1, -7, -29], index=['a', 'b', 'c', 'd', 'e', 'f', 'h'])
print("Jeeva nhân đôi:\n", jeeva * 2)
print("Trung bình của jeeva: ", np.mean(jeeva))
print('b' in jeeva)  # Kiểm tra b có trong jeeva ko
print('z' in jeeva)  # Kiểm tra z có trong jeeva ko
```

![image](https://user-images.githubusercontent.com/45547213/57615043-ec3cba80-75a4-11e9-878c-1bc9ea36c726.png)


- Method
```
player_salary = {'Rooney': 50000, 'Messi': 75000, 'Ronaldo': 85000, 'Fabregas': 40000, 'Van persie': 67000}

new_player = Series(player_salary)  # đổi từ dict sang series
print("In ra series:\n", new_player)

players = ['Klose', 'Messi', 'Ronaldo', 'Van persie', 'Ballack']
player_1 = Series(player_salary, index=players)  # gán những giá trị có ở player vào player_salary nếu không có giá trị thì trả về null
print("in ra player_1:\n", player_1)
print("Check xem chỗ nào null: ", pd.isnull(player_1))
print("Check xem chỗ nào not null: ", pd.notnull(player_1))

player_1.name = 'Bundesliga players' # gán tên cho cái series
player_1.index.name = 'Player names'  # gán tên cho cái index
print("In ra cái series mới:\n", player_1)
```
![image](https://user-images.githubusercontent.com/45547213/57637171-eb238180-75d4-11e9-813a-d4cdeda58e17.png)



## Data frame
- Định nghĩa
Nó biến 1 cái dict thành 1 cái bảng
```
states = {'State': ['Gujarat', 'Tamil Nadu', ' Andhra', 'Karnataka', 'Kerala'],
          'Population': [36, 44, 67, 89, 34],
          'Language': ['Gujarati', 'Tamil', 'Telugu', 'Kannada', 'Malayalam']}
india = DataFrame(states)  # creating a data frame
print(india)
```
![image](https://user-images.githubusercontent.com/45547213/57637509-cda2e780-75d5-11e9-88f1-108c4bef49fa.png)

Bạn có thể thay đổi thứ tự của các cột so với dict ban đầu 
```
print(DataFrame(states, columns=['State', 'Language', 'Population']))
```
![image](https://user-images.githubusercontent.com/45547213/57637636-1fe40880-75d6-11e9-9048-582c4ab78685.png)

Bạn cũng có thể thay đổi kiểu index và truy cập từng phần tử
```
new_farme = DataFrame(states, columns=['State', 'Language', 'Population', 'Per Capita Income'], index=['a', 'b', 'c', 'd', 'e'])
print('frame mới:\n', new_farme, '\n')

print('lấy cột state:\n', new_farme['State'], '\n')

print('còn cách này để value của 1 cột:\n', new_farme.Population, '\n')
```


![image](https://user-images.githubusercontent.com/45547213/57638132-51110880-75d7-11e9-813a-54b93a73b0da.png)


- Bạn có thể gán giá chị cho cột, lấy value theo dòng
```
print('lấy từng dòng:\n', new_farme.iloc[[2]])

new_farme['Per Capita Income'] = 99  #Gán giá trị cho cột

print('frame mới:\n', new_farme, '\n')
```
![image](https://user-images.githubusercontent.com/45547213/57638971-1dcf7900-75d9-11e9-8107-a139a06101c3.png)

- Bạn có thể thêm cột rồi xóa cột, rồi đảo cột 
```
ew_farme['Development'] = new_farme.State == 'Gujarat'  # Tạo cột mới trả về true ở dòng có state là gujarat
print(new_farme)
del(new_farme['Development']) # Xóa cột mới
print(new_farme)
print(elections.T
```




























