'''
For this exercise you will be strengthening your page-fu mastery. 
You will complete the PaginationHelper class, which is a utility 
class helpful for querying paging information related to an array.

The class is designed to take in an array of values and an integer 
indicating how many items will be allowed per each page. 
The types of values contained within the collection/array are not relevant.
'''

# TODO: complete this class

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        number_of_pages = len(self.collection) / self.items_per_page
        if number_of_pages % 1 > 0:
            number_of_pages = int(number_of_pages) + 1
        return number_of_pages
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        max_page_number = self.page_count() - 1
        if page_index > max_page_number or page_index < 0: #out of range
            return -1
        elif page_index == max_page_number: # last page
            return self.item_count() - self.items_per_page * max_page_number
        else:
            return self.items_per_page
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index >= self.item_count() or item_index < 0 or self.item_count() == 0: # out of range
            return -1
        else:
            return int(item_index / self.items_per_page)


helper = PaginationHelper([range(25)], 4)
# page_index returned incorrect value when provided a item_index argument (24) that was out of range: 2 should equal -1
print(helper.page_index(24))