## getting numbers of alphabets in their original order 
alpha = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class GroupedLetterGen:
    def __init__(self, string, group_by):
        self.string = string
        self.group_by = group_by
        self.groups = self._generate_groups()
    def _generate_groups(self):
        letters = [char.lower() for char in self.string if char.isalpha()]
        groups = [letters[i:i+self.group_by] for i in range(0, len(letters), self.group_by)]
        if len(groups[-1]) < group_by:
            groups[-1] += [' '] * (group_by - len(groups[-1]))
        return groups
    
class 

def changing_input_to_num(words):
    
    word_to_number = {}
    for word in words:
        word_lower = word.lower()
        index = words.index(word_lower) + 1
        word_to_number[word] = index 
    return word_to_number
words = input("Word to encrypt:")
group_by = len(words) 
changed_word = changing_input_to_num(words) 

print(changed_word)
print(group_by)

string = input("Enter Your message here:>.")
generator = GroupedLetterGen(string, group_by)
print("Groups", generator.groups)

    

