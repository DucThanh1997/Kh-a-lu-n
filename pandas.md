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
