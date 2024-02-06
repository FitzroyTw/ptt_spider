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
運行程式即可

使用結果:
-------------
![ptt-pitcure](https://github.com/FitzroyTw/ptt.py/assets/156772301/c057a12c-2f9f-460a-a8d6-b56460f2ee7f)


![ptt-img](https://github.com/FitzroyTw/ptt.py/assets/156772301/c51a7542-1ce8-4fe7-9934-cef47cf26d7a)
