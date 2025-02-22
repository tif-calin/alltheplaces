import html

from scrapy import FormRequest, Spider

from locations.dict_parser import DictParser
from locations.spiders.vapestore_gb import clean_address


class WinemarkGBSpider(Spider):
    name = "winemark_gb"
    item_attributes = {"brand": "Winemark", "brand_wikidata": "Q122011535"}

    def start_requests(self):
        yield FormRequest(
            url="https://winemark.com/wp-admin/admin-ajax.php",
            formdata={"action": "csl_ajax_onload", "radius": "10000"},
        )

    def parse(self, response, **kwargs):
        for location in response.json()["response"]:
            location["street_address"] = html.unescape(
                clean_address([location.pop("address"), location.pop("address2")])
            )
            item = DictParser.parse(location)
            item["extras"]["branch"] = item.pop("name")
            if url := location["url"]:
                item["website"] = response.urljoin(url)

            yield item
