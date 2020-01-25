from scrapy import Spider, Request
from canna.items import CannaItem

class CannaSpider(Spider):
    name = 'canna_spider'
    allowed_urls = ['https://www.leafly.com/strains']
    start_urls = ['https://www.leafly.com/strains?page=1']


    def parse(self, response):

        begin = 'https://www.leafly.com'

        end = '/strains?page='

        next_page = response.xpath('//*[@class="flex items-center pl-sm"]/@href').getall()

        strain_urls = response.xpath('//*[@class="strain-playlist-grid"]/a/@href').getall()

        #strain_json = response.xpath('//*[@id="__NEXT_DATA__"]/text()').getall()

        npages = int(response.xpath('//*[@class="mx-lg md:mx-xxl"]/text()').getall()[-1])


        next_urls = [response.url] + [begin + end +'%d'%pgn for pgn in range (2, npages +1)]
 

        strain_url_combined = [begin + strain_url for strain_url in strain_urls]

        for url in next_urls:
            yield Request(url)
            for strain_url in strain_url_combined:
                yield Request(strain_url, self.parse_canna)

            


    def parse_canna(self, response):
        print(response)
        print('#' * 75)

        #strain_json = response.meta['strain_json']

        terpenes = None
        terp_bar_pct = None
        terp_descrip = None
        effects = None
        eff_pct = None
        feel_1 = None
        feel_1_pct = None
        feel_2 = None
        feel_2_pct = None
        feel_3 = None
        feel_3_pct = None
        feel_4 = None
        feel_4_pct = None
        feel_5 = None
        feel_5_pct = None
        help_1 = None
        help_1_pct = None
        help_2 = None
        help_2_pct = None
        help_3 = None
        help_3_pct = None
        help_4 = None
        help_4_pct = None
        help_5 = None
        help_5_pct = None
        neg_1 = None
        neg_1_pct = None
        neg_2 = None
        neg_2_pct = None
        neg_3 = None
        neg_3_pct = None
        neg_4 = None
        neg_4_pct = None
        neg_5 = None
        neg_5_pct = None
        grow_all = None
        pop_loc = None

        container = response.xpath('//main[@btc-container="true"]')
        
        for info in container: 
            strain = response.xpath('//h1/text()').get()

            prim_type = response.xpath('//div[2]/header/div[1]/h2/a/text()').get()
            rating = response.xpath('//*[@class="font-bold text-green text-xs m-none"]/span/text()').get()
            n_rate_rvws = response.xpath('//*[@class="font-bold text-green text-xs m-none"]/a/text()').get()
            thc_pct = response.xpath('//*[@data-testid="cannabinoidsContainer"]//div/text()').get()
            cbd_pct = response.xpath('//button[@data-testid="cannabinoids__carrot-link-button__cbd"]/div/text()').get()
            
            terp_ctrl = response.xpath('//div[@class="border-t border-deep-green-40 flex items-center font-headers font-bold text-xs py-md"]')
            if terp_ctrl:
                terpenes = response.xpath('//*[@class="flex flex-col"]/@data-testid').getall()
                terp_bar_pct = response.xpath('//*[@class="flex flex-col"]/@style').getall()
                terp_descrip = response.xpath('//*[@class="font-normal"]/text()').getall()
            
            calm_vs_ener = response.xpath('//*[@class="calm-energize__mark bg-leafly-white absolute top-0 bottom-0"]/@style').get()
            
            n_reported_effects = response.xpath('//*[@class="flex items-center font-mono text-xs"]/text()').get()
            
            eff_ctrl = response.xpath('//section[@class="pt-xxl "]')
            if eff_ctrl:             
                #all Effects
                effects = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()

                #all pcts
                eff_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()

                #Effects - Feelings:
                feel_1 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[0]
                feel_1_pct =  response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[0]

                feel_2 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[2]
                feel_2_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[2]

                feel_3 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[4]
                feel_3_pct  = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[4]

                feel_4 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[6]
                feel_4_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[6]

                feel_5 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[8]
                feel_5_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[8]

                #Effects - Helps with:
                help_1 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[10]
                help_1_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[10]

                help_2 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[12]
                help_2_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[12]

                help_3 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[14]
                help_3_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[14]

                help_4 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[16]
                help_4_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[16]

                help_5 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[18]
                help_5_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[18]

                #Effects - Negatives:
                neg_1 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[20]
                neg_1_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[20]

                neg_2 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[22]
                neg_2_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[22]

                neg_3 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[24]
                neg_3_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[24]

                neg_4 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[26]
                neg_4_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[26]

                neg_5 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').getall()[28]
                neg_5_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').getall()[28]

            #Lineage:
            parent_1 = response.xpath('//*[@class="lineage__left-parent"]/a/div/div/text()').get()
            parent_2 = response.xpath('//*[@class="lineage__right-parent"]/a/div/div/text()').get()
            child_1 = response.xpath('//*[@class="lineage__left-child--two-parents"]/a/div/div/text()').get()
            child_2 = response.xpath('//*[@class="lineage__right-child--two-parents"]/a/div/div/text()').get()

            #Grow Info:
                #all_tags: response.xpath('//*[@class="flex flex-row w-full mb-lg"]//@class').getall()
                #all_text: #response.xpath('//*[@class="flex flex-row w-full mb-lg"]//text()').getall()
            grw_ctrl = response.xpath('//section[@class="pt-xxl w-full lg:pt-none"]')
            if grw_ctrl:
                grow_all = response.xpath('//div[contains(@class,"bg-deep-green")]/text()').getall()
            
            #Strain Popular Locations:
            pop_ctrl = response.xpath('//section[@class="pt-xxl "]')
            if pop_ctrl:
                pop_loc = response.xpath('//*[@class="mb-lg"]/a/text()').getall()



            item = CannaItem()

            #item['strain_json'] = strain_json

            item['strain'] = strain

            item['prim_type'] = prim_type
            item['rating'] = rating
            item['n_rate_rvws'] = n_rate_rvws
            item['thc_pct'] = thc_pct
            item['cbd_pct'] = cbd_pct
            item['terpenes'] = terpenes
            item['terp_bar_pct'] = terp_bar_pct
            item['terp_descrip'] = terp_descrip
            item['calm_vs_ener'] = calm_vs_ener
            item['n_reported_effects'] = n_reported_effects
            item['effects'] = effects
            item['eff_pct'] = eff_pct
            
            item['feel_1'] = feel_1
            item['feel_1_pct'] = feel_1_pct
            item['feel_2'] = feel_2
            item['feel_2_pct'] = feel_2_pct
            item['feel_3'] = feel_3
            item['feel_3_pct'] = feel_3_pct
            item['feel_4'] = feel_4
            item['feel_4_pct'] = feel_4_pct
            item['feel_5'] = feel_5
            item['feel_5_pct'] = feel_5_pct

            item['help_1'] = help_1
            item['help_1_pct'] =  help_1_pct
            item['help_2'] = help_2
            item['help_2_pct'] = help_2_pct 
            item['help_3'] = help_3 
            item['help_3_pct'] = help_3_pct
            item['help_4'] = help_4 
            item['help_4_pct'] = help_4_pct
            item['help_5'] = help_5 
            item['help_5_pct'] = help_5_pct

            item['neg_1'] = neg_1
            item['neg_1_pct'] = neg_1_pct
            item['neg_2'] = neg_2
            item['neg_2_pct'] = neg_2_pct
            item['neg_3'] = neg_3 
            item['neg_3_pct'] = neg_3_pct 
            item['neg_4'] = neg_4
            item['neg_4_pct'] = neg_4_pct
            item['neg_5'] = neg_5
            item['neg_5_pct'] = neg_5_pct

            item['parent_1'] = parent_1
            item['parent_2'] = parent_2
            item['child_1'] = child_1
            item['child_2'] = child_2

            item['grow_all'] = grow_all


            item['pop_loc'] = pop_loc

            yield item




