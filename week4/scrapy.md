                    spiders
                    
item pipelines      engin           downloaders
                     
                     
                    scheduler
## 几条主要的数据流路径
- 第一条

spiders->engin->scheduler->engin->downloader->
engine->spiders

- 第二条

多了一个从engin到item pipelines的

## 如何选择爬虫技术路线
想要自搭框架，非常小的需求：requests库
不太小的 需求：scrapy