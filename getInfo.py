import requests
from bs4 import BeautifulSoup
import pandas as pd

# 目标URL
url = "https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=C&honors=F&keywords=44547&promod=F&searchType=all&term=2254"

# 请求头，伪装浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

# 发起请求
response = requests.get(url, headers=headers)
response.raise_for_status()

# 解析HTML
soup = BeautifulSoup(response.text, "lxml")

# 找到所有包含课程信息的区域
course_cards = soup.find_all("div", class_="section--content")

# 用列表收集课程信息
data = []

for card in course_cards:
    # 提取课程名称
    course_title_tag = card.find("div", class_="class-title")
    course_title = course_title_tag.text.strip() if course_title_tag else "Unknown"

    # 提取座位信息
    seats_info_tag = card.find("div", class_="enrollment")
    if seats_info_tag:
        seats_text = seats_info_tag.get_text(strip=True)
        if "Seats Avail:" in seats_text:
            seats_avail = seats_text.split("Seats Avail:")[-1].split()[0]
        else:
            seats_avail = "Unknown"
    else:
        seats_avail = "Unknown"

    data.append({
        "Course Title": course_title,
        "Seats Available": seats_avail
    })

# 保存到DataFrame并打印
df = pd.DataFrame(data)
print(df)

# 如果需要保存成Excel或CSV文件，可以取消注释下面的行：
# df.to_csv("asu_linear_algebra_seats.csv", index=False)
# df.to_excel("asu_linear_algebra_seats.xlsx", index=False)