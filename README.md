此為一個爬取當日各星座運勢的簡單爬蟲  
爬取後會自動存入MySQL  
更改click/click/spiders/click_star.py裡面的連接位置  
在spider的上一層輸入scrapy crawl click_star即可開始爬取  

  

##簡單指令  
scrapy startproject tutorial        #創建項目  
cd tutorial  
scrapy genspider <name> <網域>      #建立spider  
scrapy crawl <spider's name>        #啟動spider  

