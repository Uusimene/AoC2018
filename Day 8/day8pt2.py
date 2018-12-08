
def main():
    file = open("input.txt", "r", encoding="utf-8")
    for row in file:
         data = row.rstrip()
    file.close()
    data = data.split(" ")
    data = list(map(int, data))
    nodes = Node(data)
    nodes.addChild()
    print("Part 1:", getMetadataSum(nodes))
    print("Part 2:", nodes.value)


def getMetadataSum(node):
    metadatasum = sum(node.metadatas)
    for i in range(0, node.child_count):
        metadatasum += getMetadataSum(node.children[i])
    return metadatasum


class Node(object):
    def __init__(self, data):
        self.child_count = data[0]
        self.metadata_count = data[1]
        self.data_list = data[2:]
        self.children = []
        self.metadatas = []
        self.value = 0

    def addChild(self):
        for i in range(0, self.child_count):
            self.children.append(Node(self.data_list))
            self.data_list = self.children[-1].addChild()
        self.addMetadata()
        return self.data_list

    def addMetadata(self):
        self.metadatas = (self.data_list[:self.metadata_count])
        self.data_list = self.data_list[self.metadata_count:]
        if self.child_count == 0:
            self.value = sum(self.metadatas)
        else:
            for i in self.metadatas:
                try:
                    self.value += self.children[i-1].value
                except IndexError:
                    continue


main()
