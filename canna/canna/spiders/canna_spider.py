from scrapy import Spider, Request
from marijuana.items import CannaItem

class CannaSpider(Spider):
    name = 'canna_spider'
    allowed_urls = ['https://www.leafly.com/strains']
    start_urls = ['https://www.leafly.com/strains?page=1']


    def parse(self, response):

        begin = 'https://www.leafly.com'

        next_page = response.xpath('//*[@class="flex items-center pl-sm"]/@href').extract()

        strain_urls = response.xpath('//*[@class="strain-playlist-grid"]/a/@href').extract()

        #strain_data = response.xpath('//*[@id="__NEXT_DATA__"]/text()').extract()

        npages = int(response.xpath('//*[@class="mx-lg md:mx-xxl"]/text()').extract()[-1])

        next_urls = [begin + url for url in next_page]

        strain_url_combined = [begin + strain_url for strain_url in strain_urls]

        try: 
            for url in next_urls[:2]:
                for strain_url in strain_url_combined:
                #for strain_url in strain_url_combined[:3]:
                    yield Request(strain_url, self.parse_canna)
        except Exception as e:
            print ('*' * 75)
            print(e)
            


    def parse_canna(self, response):
        print(response)
        print('#' * 75)

        # begin_2 = 'https://www.leafly.com'
        
        # div_eles = response.xpath('//*[@class="strain-tile justify-start relative"]/@href').extract()

        # element = [begin_2 + div_ele for div_ele in div_eles]

        container = response.xpath('//*[@class="container"]')
        
        for strain in container:
            strain = response.xpath('//h1/text()').extract()
            prim_type = response.xpath('//div[2]/header/div[1]/h2/a/text()').extract()
            rating = response.xpath('//*[@class="font-bold text-green text-xs m-none"]/span/text()').extract_first()
            n_rate_rvws = response.xpath('//*[@class="font-bold text-green text-xs m-none"]/a/text()').extract_first()
            thc_pct = response.xpath('//*[@data-testid="cannabinoidsContainer"]//div/text()').extract_first()
            terpenes = response.xpath('//*[@class="flex flex-col"]/@data-testid').extract()
            terp_bar_pct = response.xpath('//*[@class="flex flex-col"]/@style').extract()
            terp_descrip = response.xpath('//*[@class="font-normal"]/text()').extract()
            calm_vs_ener = response.xpath('//*[@class="calm-energize__mark bg-leafly-white absolute top-0 bottom-0"]/@style').extract()
            #strain_descrip = response.xpath('//*[@itemprop="description"]/p/text()').extract()
            n_reported_effects = response.xpath('//*[@class="flex items-center font-mono text-xs"]/text()').extract_first()

            
            #all Effects
            effects = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()

            #all pcts
            eff_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()

            #Effects - Feelings:
            happy = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[0]
            happy_pct =  response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[0]

            euph = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[2]
            euph_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[2]

            relax = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[4]
            relax_pct  = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[4]

            uplift = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[6]
            uplift_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[6]

            creative = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[8]
            creative_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[8]

            #Effects - Helps with:
            stress = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[10]
            stress_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[10]

            anx = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[12]
            anx_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[12]

            depr = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[14]
            depr_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[14]

            pain = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[16]
            pain_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[16]

            insom = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[18]
            insom_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[18]

            #Effects - Negatives:
            dry_mth = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[20]
            dry_mth_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[20]

            dry_eye = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[22]
            dry_eye_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[22]

            para = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[24]
            para_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[24]

            dizzy = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[26]
            dizzy_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[26]

            anx_2 = response.xpath('//*[@class="mb-xl relative w-full"]/div/text()').extract()[28]
            anx_2_pct = response.xpath('//*[@class="mb-xl relative w-full"]/div/span/text()').extract()[28]

            #Lineage:
            try:
                parent_1 = response.xpath('//*[@class="lineage__left-parent"]/a/div/div/text()').extract_first()
                parent_2 = response.xpath('//*[@class="lineage__right-parent"]/a/div/div/text()').extract_first()
                child_1 = response.xpath('//*[@class="lineage__left-child--two-parents"]/a/div/div/text()').extract_first()
                child_2 = response.xpath('//*[@class="lineage__right-child--two-parents"]/a/div/div/text()').extract_first()
            except Exception as e:
                print ('=' * 75)
                print(e)

            #Grow Info:
            ##Check later on this for reg expressions

            #Strain Popular Locations:
            pop_loc = response.xpath('//*[@class="mb-lg"]/a/text()').extract()

            item = CannaItem()

            item['strain'] = strain
            item['prim_type'] = prim_type
            item['rating'] = rating
            item['n_rate_rvws'] = n_rate_rvws
            item['thc_pct'] = thc_pct
            item['terpenes'] = terpenes
            item['terp_bar_pct'] = terp_bar_pct
            item['terp_descrip'] = terp_descrip
            item['calm_vs_ener'] = calm_vs_ener
            item['n_reported_effects'] = n_reported_effects
            item['effects'] = effects
            item['eff_pct'] = eff_pct
            
            item['happy'] = happy
            item['happy_pct'] = happy_pct

            item['euph'] = euph
            item['euph_pct'] = euph

            item['relax'] = relax
            item['relax_pct'] = relax_pct

            item['uplift'] = uplift
            item['uplift_pct'] = uplift_pct

            item['creative'] = creative 
            item['creative_pct'] = creative_pct

            item['stress'] = stress
            item['stress_pct'] =  stress_pct

            item['anx'] = anx
            item['anx_pct'] = anx_pct 

            item['depr'] = depr 
            item['depr_pct'] = depr_pct
            
            item['pain'] = pain 
            item['pain_pct'] = pain_pct
            
            item['insom'] = insom 
            item['insom_pct'] = insom_pct

            item['dry_mth'] = dry_mth
            item['dry_mth_pct'] = dry_mth_pct

            item['dry_eye'] = dry_eye
            item['dry_eye_pct'] = dry_eye_pct

            item['para'] = para 
            item['para_pct'] = para_pct 

            item['dizzy'] = dizzy
            item['dizzy_pct'] = dizzy_pct

            item['anx_2'] = anx_2 
            item['anx_2_pct'] = anx_2_pct

            item['parent_1'] = parent_1
            item['parent_2'] = parent_2
            item['child_1'] = child_1
            item['child_2'] = child_2

            item['pop_loc'] = pop_loc

            yield item

