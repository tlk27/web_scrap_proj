# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CannaItem(scrapy.Item):
    
    ##can be uncommented to include json data
    #strain_json = scrapy.Field()

    strain = scrapy.Field()

    prim_type = scrapy.Field()
    rating = scrapy.Field()
    n_rate_rvws = scrapy.Field()
    thc_pct = scrapy.Field()
    cbd_pct = scrapy.Field()
    terpenes = scrapy.Field()
    terp_bar_pct = scrapy.Field()
    terp_descrip = scrapy.Field()
    calm_vs_ener = scrapy.Field()

    n_reported_effects = scrapy.Field()
    effects = scrapy.Field()
    eff_pct = scrapy.Field()

    ##comment out effects below for  more strain records
    ##effects include feel_1 through neg_5_pct
    feel_1 = scrapy.Field()
    feel_1_pct = scrapy.Field()
    feel_2 = scrapy.Field()
    feel_2_pct = scrapy.Field()
    feel_3 = scrapy.Field()
    feel_3_pct = scrapy.Field()
    feel_4 = scrapy.Field()
    feel_4_pct = scrapy.Field()
    feel_5 = scrapy.Field()
    feel_5_pct = scrapy.Field()

    help_1 = scrapy.Field()
    help_1_pct = scrapy.Field()
    help_2 = scrapy.Field()
    help_2_pct = scrapy.Field()
    help_3 = scrapy.Field()
    help_3_pct = scrapy.Field()
    help_4 = scrapy.Field()
    help_4_pct = scrapy.Field()
    help_5 = scrapy.Field()
    help_5_pct = scrapy.Field()

    neg_1 = scrapy.Field()
    neg_1_pct = scrapy.Field()
    neg_2 = scrapy.Field()
    neg_2_pct = scrapy.Field()
    neg_3 = scrapy.Field()
    neg_3_pct = scrapy.Field()
    neg_4 = scrapy.Field()
    neg_4_pct = scrapy.Field()
    neg_5 = scrapy.Field()
    neg_5_pct = scrapy.Field()

    parent_1 = scrapy.Field()
    parent_2 = scrapy.Field()
    child_1 = scrapy.Field()
    child_2 = scrapy.Field()

    grow_all = scrapy.Field()

    pop_loc = scrapy.Field()



