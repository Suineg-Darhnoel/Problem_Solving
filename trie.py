class trie:

    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.children = []
        # marked as End-Of-String
        self.is_EOS = False

    def create_subtree(self, word):
        cnt_down = len(word)

        def start(obj, word):
            if len(word) > 0:
                new_child = trie(word[0], obj)

                # mark EOS here
                if cnt_down == 1:
                    new_child.is_EOS = True
                obj.children.append(new_child)

                word = word[1:]
                new_child.create_subtree(word)

        start(self, word)

    def build_trie(self, word):
        if not self.has_children or word[0] not in self.children_values:
            self.create_subtree(word)
        else:
            # first method to find found_key
            # using traditional style

            found_key = None
            for key, val in enumerate(self.children_values):
                if word[0] == val:
                    found_key = key
                    break
            self.children[found_key].build_trie(word[1:])

    def contains(self, word):
        if len(word) > 0:
            if word[0] not in self.children_values:
                return False
            else:
                # second method to find found_key
                # using list comprehension

                found_key = [
                        k for k, v in enumerate(self.children_values)
                        if word[0] == v
                    ][0]

                child = self.children[found_key]

                # consider the last character
                if len(word) == 1 and child.is_EOS:
                    return True
                return child.contains(word[1:])

    def words_list(self):
        curr_word, stack, list_of_words = "", [], []

        def depth_word(self, curr_word, level=0):
            # print(level)
            if not self.has_children:
                # print(curr_word)
                list_of_words.append(curr_word)
                if len(stack) > 0:
                    curr_child, level = stack.pop()
                    curr_word = curr_word[:level] + curr_child.value
                    depth_word(curr_child, curr_word, level)

                # start backtracking
            else:
                if self.is_EOS:
                    pass
                    list_of_words.append(curr_word)
                    # print(curr_word)
                if len(self.children) > 1:
                    for child in self.children[1:]:
                        stack.append((child, level+1))

                curr_child = self.children[0]
                curr_word = curr_word + curr_child.value
                depth_word(curr_child, curr_word, level+1)
        depth_word(self, curr_word, -1)

        return list_of_words

    @property
    def is_root(self):
        return True if self.parent is None else False

    @property
    def has_children(self):
        return True if len(self.children) > 0 else False

    @property
    def parent_value(self):
        return self.parent.value if self.parent is not None else None

    @property
    def children_values(self):
        values = []
        for child in self.children:
            values.append(child.value)
        return values


words = [
        'app', 'apple', 'any',
        'what', 'angle', 'bingo',
        'badguy', 'car', 'bingor',
        'ace'
]

root = trie('', parent=None)


for word in words:
    root.build_trie(word)

test_words = [
        'binga', 'bingo', 'badguy',
        'badgay', 'apps', 'apple', 'cp', 'car'
        ]
# print('words = ', words)

for word in test_words:
    print(word, root.contains(word))

print(root.words_list())
