import requests
from bs4 import BeautifulSoup

# 目标URL
url = 'https://www.udemy.com/courses/search/?q=data+analytics&src=sac&kw=data+ana'

# 发送HTTP GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 假设课程名称和价格位于具有特定class的元素中，这里使用假设的class名
    # 你需要根据实际网页结构来调整这些选择器
    courses = soup.find_all('div', class_='course-name-class')  # 课程名称的容器
    prices = soup.find_all('div', class_='price-class')  # 价格的容器

    # 遍历课程和价格，打印出来
    for course, price in zip(courses, prices):
        print(f"Course Name: {course.get_text().strip()}")
        print(f"Price: {price.get_text().strip()}")
else:
    print(f"Failed to retrieve content, status code: {response.status_code}")
