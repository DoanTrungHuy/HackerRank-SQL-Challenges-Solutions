import pandas as pd
import matplotlib.pyplot as plt

# Dữ liệu mô phỏng
data = {
    'Name': ['Abigail', 'Samantha', 'Julia', 'Ashley', 'Maria', 'Jane', 'Christeen', 'Kristeen', 'Scarlet', 'Amelia', 'Priya', 'Meera', 'Priyanka', 'Priyanka', 'Jennifer', 'Priya', 'Julia', 'Kristeen', 'Samantha', 'Ashley'],
    'Occupation': ['Doctor']*10 + ['Professor']*3 + ['Singer']*7,
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Sử dụng GROUP BY trong pandas để nhóm theo nghề nghiệp và đếm số lượng trong mỗi nhóm
grouped = df.groupby('Occupation').size()

# Vẽ biểu đồ cột
grouped.plot(kind='bar', color='skyblue')
plt.title('Số lượng người trong mỗi nghề nghiệp')
plt.xlabel('Nghề nghiệp')
plt.ylabel('Số lượng')
plt.xticks(rotation=45)
plt.show()
