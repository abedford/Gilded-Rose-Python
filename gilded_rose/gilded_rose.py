legendary_item = "Sulfuras, Hand of Ragnaros"
backstage_pass = "Backstage passes to a TAFKAL80ETC concert"
aged_brie = "Aged Brie"
conjured_item = "Conjured"

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        
    def update_quality(self):
        for item in self.items:
            if item.name != aged_brie and item.name != backstage_pass:
                self.decrease_quality_for_not_legendary_item(item)
            else:
                self.increase_quality_if_less_than_50(item)
                self.increase_quality_for_backstage_pass(item)
                    
            if item.name != legendary_item:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != aged_brie:
                    if item.name != backstage_pass:
                        self.decrease_quality_for_not_legendary_item(item)
                    else:
                        self.set_quality_to_nothing(item)
                else:
                    self.increase_quality(item)

    def set_quality_to_nothing(self, item):
        item.quality = item.quality - item.quality

    def decrease_quality_for_not_legendary_item(self,item):
        if item.quality > 0:
            if item.name != legendary_item:
                self.decrease_quality_by_1(item)
                self.decrease_quality_for_conjured_item(item)


    def increase_quality_if_less_than_50(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def increase_quality_for_backstage_pass(self, item):
        if item.name == backstage_pass:
            if item.sell_in < 11:
                self.increase_quality(item)
            if item.sell_in < 6:
                self.increase_quality(item)

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
    
    def decrease_quality_for_conjured_item(self,item):
        if item.name.startswith(conjured_item):
            self.decrease_quality_by_1(item)

    def decrease_quality_by_1(self, item):
        item.quality = item.quality - 1

    

