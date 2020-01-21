# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CannaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    strain = scrapy.Field()
    prim_type = scrapy.Field()
    rating = scrapy.Field()
    n_rate_rvws = scrapy.Field()
    thc_pct = scrapy.Field()
    terpenes = scrapy.Field()
    terp_bar_pct = scrapy.Field()
    terp_descrip = scrapy.Field()
    calm_vs_ener = scrapy.Field()
    n_reported_effects = scrapy.Field()
    effects = scrapy.Field()
    eff_pct = scrapy.Field()
    happy = scrapy.Field()
    happy_pct = scrapy.Field()
    euph = scrapy.Field()
    euph_pct = scrapy.Field()
    relax = scrapy.Field()
    relax_pct = scrapy.Field()
    uplift = scrapy.Field()
    uplift_pct = scrapy.Field()
    creative = scrapy.Field()
    creative_pct = scrapy.Field()
    stress = scrapy.Field()
    stress_pct = scrapy.Field()
    anx = scrapy.Field()
    anx_pct = scrapy.Field()
    depr = scrapy.Field()
    depr_pct = scrapy.Field()
    pain = scrapy.Field()
    pain_pct = scrapy.Field()
    insom = scrapy.Field()
    insom_pct = scrapy.Field()
    dry_mth = scrapy.Field()
    dry_mth_pct = scrapy.Field()
    dry_eye = scrapy.Field()
    dry_eye_pct = scrapy.Field()
    para = scrapy.Field()
    para_pct = scrapy.Field()
    dizzy = scrapy.Field()
    dizzy_pct = scrapy.Field()
    anx_2 = scrapy.Field()
    anx_2_pct = scrapy.Field()
    parent_1 = scrapy.Field()
    parent_2 = scrapy.Field()
    child_1 = scrapy.Field()
    child_2 = scrapy.Field()
    pop_loc = scrapy.Field()