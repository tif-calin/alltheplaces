from scrapy.spiders import SitemapSpider

from locations.structured_data_spider import StructuredDataSpider


class SolidcoreUSSpider(SitemapSpider, StructuredDataSpider):
    name = "solidcore_us"
    item_attributes = {"brand": "[solidcore]", "brand_wikidata": "Q124429271"}
    sitemap_urls = ["https://www.solidcore.co/studio-sitemap.xml"]
    sitemap_rules = [(r"co/\w\w/[^/]+/[^/]+/$", "parse")]
    wanted_types = ["LocalBusiness"]
