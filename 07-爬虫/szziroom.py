base_url = "http://sz.ziroom.com/z/nl/z3.html"

if __name__ == '__main__':
    for i in range(1, 51):
        Get_one_page(i)


class Get_one_page:
    def __init__(self, page):
        self.page = page
        self.parmas = {"p": page}
        self.appartments = []

    def getpage(self):
        try:
            time.sleep(random.randint(1, 2))
            response = requests.get(url=base_url, params=self.parmas, headers=my_headers)
        except Exception as e:
            print("get方法失败" + self.page)
            print(e)
            return
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            ul = soup.select("ul[id='houseList']")
            li_list = ul[0].select("li")
        else:
            print("状态码不为200------" + self.page)
            return
        for li in li_list:
            address = li.select("h3")[0].text + "," + soup.select("h4")[0].text  # 获取房源地址
            descripe = li.select(".detail")[0].text.replace(" ", "").replace("\n", ",")[2:]  # 获取房源描述信息
            tags = li.select(".room_tags")[0].text.replace("\n", ",")[1:]  # 获取房源标签
            more_href = "http:" + li.select('.more a')[0].attrs["href"]  # 详情链接
            img_src = "http:" + li.select("img")[0].attrs["_src"]  # 图片链接
            price = self.get_price(more_href)
            room = {"address": address,
                    "descripe": descripe,
                    "tags": tags,
                    "more": more_href,
                    "img_src": img_src,
                    "price": price}
            self.appartments.append(room)

def get_price(self, href):
        """返回的是季付每月租金, 从更多页面中获取"""
        try:
            time.sleep(random.randint(1, 2))
            response = requests.get(url=href, headers=my_headers)

    except Exception as e:
    print("get方法失败" + href)
    print(e)
    price = "0"

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        try:
            price = soup.select("#room_price")[0].text
        except:
            print(href)
            price = "0"
    else:
        print("状态码不为200------" + href)
        price = "0"
    regex = "\d+"
    if price == None:
        print(href)
        price = "0"
    return re.findall(regex, price)[0]
