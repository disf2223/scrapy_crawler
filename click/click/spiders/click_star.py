# -*- coding: utf-8 -*-
import scrapy,time,re,pymysql

class ClickStarSpider(scrapy.Spider):
    name = 'click_star'                                                                                                 #爬蟲名稱
    allowed_domains = ['click108.com.tw/']                                                                              #爬取的網域名稱
    start_urls = [
         # 'http://astro.click108.com.tw/'
        'http://astro.click108.com.tw/daily_0.php?iAstro=0'
        ,'http://astro.click108.com.tw/daily_1.php?iAstro=1'
        ,'http://astro.click108.com.tw/daily_2.php?iAstro=2'
        ,'http://astro.click108.com.tw/daily_3.php?iAstro=3'
        ,'http://astro.click108.com.tw/daily_4.php?iAstro=4'
        ,'http://astro.click108.com.tw/daily_5.php?iAstro=5'
        ,'http://astro.click108.com.tw/daily_6.php?iAstro=6'
        ,'http://astro.click108.com.tw/daily_7.php?iAstro=7'
        ,'http://astro.click108.com.tw/daily_8.php?iAstro=8'
        ,'http://astro.click108.com.tw/daily_9.php?iAstro=9'
        ,'http://astro.click108.com.tw/daily_10.php?iAstro=10'
        ,'http://astro.click108.com.tw/daily_11.php?iAstro=11'
    ]                                                                                                                   #啟動時爬取的網址

    def parse(self, response):
        db = pymysql.connect("localhost", "disf2223", "Qaz321654", "db_star")                                           #mysql連接
        cursor = db.cursor()
        d_date = response.xpath('.//select/option[@selected="selected"]/text()').extract_first()                        #當天日期
        star_name = response.xpath('.//div[@class="FOOTSTAR"]/ul/li/h3/text()').extract()                               #星座名稱
        all_sc_point = response.xpath('.//div[@class="TODAY_CONTENT"]/p/span[@class="txt_green"]/text()').extract()     #整體運勢
        all_sc = response.xpath('.//div[@class="TODAY_CONTENT"]/p[2]/text()').extract()                                 #評分及說明
        love_sc_point = response.xpath('.//div[@class="TODAY_CONTENT"]/p/span[@class="txt_pink"]/text()').extract()     #愛情運勢
        love_sc = response.xpath('.//div[@class="TODAY_CONTENT"]/p[4]/text()').extract()                                #評分及說明
        job_sc_point = response.xpath('.//div[@class="TODAY_CONTENT"]/p/span[@class="txt_blue"]/text()').extract()      #事業運勢
        job_sc = response.xpath('.//div[@class="TODAY_CONTENT"]/p[6]/text()').extract()                                 #評分及說明
        money_sc_point = response.xpath('.//div[@class="TODAY_CONTENT"]/p/span[@class="txt_orange"]/text()').extract()  #財運運勢
        money_sc = response.xpath('.//div[@class="TODAY_CONTENT"]/p[8]/text()').extract()                               #評分及說明

        #SQL存入條件
        sql = "INSERT INTO star_list(d_date,star_name,all_sc_point,all_sc,love_sc_point,love_sc,job_sc_point,job_sc,money_sc_point,money_sc) VALUES ('%s', '%s', " \
              "'%s', '%s', '%s' ,'%s', '%s', '%s', '%s', '%s' )"%(d_date, star_name[0],all_sc_point[0][0:8], all_sc[0],love_sc_point[0][0:8]\
                ,love_sc[0],job_sc_point[0][0:8], job_sc[0],money_sc_point[0][0:8], money_sc[0])


        # try:
        #     cursor.execute(sql)
        #     db.commit()
        # except:
        #     db.rollback()
        cursor.execute(sql)                                                                                             #存入MySQL
        db.commit()
        db.close()



        # for url in star_url:
        #     yield scrapy.Request(url,self.star_parse)                                                                 #多頁面回傳url


    # def star_parse(self, response ):                                                                                  #接收回傳的url再次爬取網頁資訊
    #     # ddate = response.xpath('.//select/option[@selected="selected"]/text()').extract_first()
    #     # print(ddate)
    #     print(response)
