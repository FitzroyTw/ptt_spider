程式說明與套件:
-------------
本程式用到了requests beautifulSoup 以及re套件 需要使用者有python環境,以及上述所說的套件
用於使用程式瀏覽ptt網頁以及內文,並且得知回文者當前ip所屬是否使用了VPN(虛擬私人網路)
請注意! ip查詢是使用了 https://ipinfo.io 來進行爬蟲查詢,每日的ip查詢會有查詢上限,當到達上限時會無法查詢,請待明日再進行。
由於是使用了上述的網站進去ip爬蟲,所以當前文章回文人數眾多時,所需要的時間會更長。
程式還提供了另一個查詢 使用者只需要取消註解掉的部分 country,city = get_ip_status(ip_address), line = f"{line} [{country}] [{city}]"
就能得知當前回文者所在國家以及區域。(此部分一樣會有查詢上限)

使用教學:
------------
運行程式
[a]鍵進行上一頁
[d]鍵進行下一頁
文章根據上面的數字編號,輸入進去即可進行瀏覽。

使用結果:
-------------

![1707201632903](https://github.com/FitzroyTw/ptt_spider.py/assets/156772301/c6baba8a-ffdd-493e-89b2-e708f74f0df7)

![1707201679740](https://github.com/FitzroyTw/ptt_spider.py/assets/156772301/3df61a5c-b7af-41da-a74f-de688664cce1)




