class TagCloud:
    def __init__(self):
        self.tags = {}
        # create a dictionary to store value

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
        # create a tag argument for get count


cloud = TagCloud()

cloud.add("Python")
cloud.add("python")
cloud.add("Python")
cloud.add("Dart")
print(cloud.tags)
