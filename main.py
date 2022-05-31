# pip install selenium
from selenium import webdriver
# pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
# pip install beautifulsoup4
from bs4 import BeautifulSoup

import datetime
import re

# Options to hide the browser
options = webdriver.ChromeOptions()
options.add_argument("headless")

def main():
    time = "Tags\t" + str(datetime.date.today())
    print(time)
    name = "Tags " + str(datetime.date.today()) + ".txt"
    data = open(name, "a", encoding="utf-8")
    data.write(time)

    for n in range(1, 17):
        b = str(n)

        # Options to hide the browser at the end
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        driver.get("https://nhentai.xxx/tags?page=" + b)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')

        titles = soup.findAll("a", class_="tag")
        num = soup.findAll("span", class_="count")

        data.write("\npage " + b)
        tit = 0

        for title in titles[0:]:
            res = str('\nTitle: {}'.format(titles[tit].text))

            print(res)
            for tot in num[tit]:
                t = str('\n{}'.format(num[tit].text))
                y = int(re.search(r'\d+', t).group(0))
                print(y)
                # Checking the minimum number of pages to write to a file
                if y < 1000:
                    continue
                # write to a file
                data.write(res)
                data.write("\nNumber of pages: " + str(y))
                print(t)
            tit += 1

    data.close()

# Start program
if __name__ == '__main__':
    main()
