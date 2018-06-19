def sort_by_last_letter(strings):
    def last_letter(s): # Local function
        return s[-1]
    return sorted(strings, key=last_letter)


print(sort_by_last_letter(['hello', 'from', 'a', 'local', 'function'])) # ['a', 'local', 'from', 'function', 'hello']