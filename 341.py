
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.pointer = self.get_next(nestedList)
        try:
            self.next_item = next(self.pointer)
        except StopIteration:
            self.next_item = None
    def get_next(self, nestedList: [NestedInteger]):
        for item in nestedList:
            if item.isInteger():
                yield item.getInteger()
            for item2 in item.getList():
                for item3 in self.get_next_nested(item2):
                    yield item3

    def get_next_nested(self, nestedInteger: NestedInteger):
        if nestedInteger.isInteger():
            yield nestedInteger.getInteger()

        for item in nestedInteger.getList():
            for item2 in self.get_next_nested(item):
                yield item2
        
        
    
    def next(self) -> int:
        item = self.next_item
        try:
            self.next_item = next(self.pointer)
        except StopIteration:
            self.next_item = None
        return item

        
    
    def hasNext(self) -> bool:
        return self.next_item is not None
