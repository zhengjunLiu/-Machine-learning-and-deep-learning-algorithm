# -*- coding: utf-8 -*-
import scrapy
from natrue_spider.items import NatrueSpiderItem

class CatchSpiderSpider(scrapy.Spider):
	name = 'catch_spider'
	allowed_domains = ['http://www.letpub.com.cn/']
	start_urls = ['http://www.letpub.com.cn/?page=grant&name=&person=&no=&company=&addcomment_s1=553&addcomment_s2=563&addcomment_s3=0&money1=&money2=&startTime=2017&endTime=2017&subcategory=&searchsubmit=true&submit.x=77&submit.y=8&submit=advSearch#fundlisttable']

	def parse(self, response):

		
		item = NatrueSpiderItem()
		# item['name'] = response.xpath('//table[@class="table_yjfx"]/tr[@style="background:#EFEFEF;"]/td[1]/text()').extract()
		# item['university']= response.xpath('//table[@class="table_yjfx"]/tr[@style="background:#EFEFEF;"]/td[2]/text()').extract()
		# item['money']= response.xpath('//table[@class="table_yjfx"]/tr[@style="background:#EFEFEF;"]/td[3]/text()').extract()
		# item['numb']= response.xpath('//table[@class="table_yjfx"]/tr[@style="background:#EFEFEF;"]/td[4]/text()').extract()
		# item['style']= response.xpath('//table[@class="table_yjfx"]/tr[@style="background:#EFEFEF;"]/td[5]/text()').extract()
		# item['school']=response.xpath('//table[@class="table_yjfx"]/tr[@style="background:#EFEFEF;"]/td[6]/text()').extract()
		item['year']= response.xpath('//table[@class="table_yjfx"]/tr[@style="background:#EFEFEF;"]/td[7]/text()').extract()
		#item['name'] = response.xpath('//table[@class="table_yjfx"]/tr[@style="background:#EFEFEF;"]/td/text()').extract()	
		yield item