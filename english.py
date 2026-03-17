from bs4 import BeautifulSoup
import requests
import random

def get_quote(pagenum=1):
  if pagenum == 1:
     url = "https://quotes.toscrape.com/"
  else:
     url = f"https://quotes.toscrape.com/page/{pagenum}/"
  print(f"正在获取第 {pagenum} 页的每日一句...")

  try:
    response = requests.get(url, timeout=10, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
      
    all_quotes = soup.find_all('div', class_='quote')
    if not all_quotes:
        return "\n 每日一句获取失败：未找到任何引用"
    else:
      target_quote = random.choice(all_quotes)  

    quote = target_quote.find('span', class_='text').text
    author = target_quote.find('small', class_='author').text
    return f"\n 每日随机一句：{quote} —— {author}"
  except Exception as e:
      return f"\n 每日随机一句获取失败：{e}"

if __name__ == "__main__":
    print(get_quote())
    random_page = random.randint(1, 10)
    result = get_quote(random_page)
    print(result) 
