class Stacks:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        if len(self.stack) == 0: return True
        return False
    
    def __len__(self):
        return len(self.stack)
    
    def peek(self):
        return self.stack[-1]
    
    def __str__(self):
        string = ""
        for item in self.stack:
            string = string + item + " "
        return string
    
if __name__ == "__main__":
    folder = Stacks()
    library = ["Maths", "Physics", "Comp Sci"]
    for books in library:
        folder.push(books)
    print("="*30)
    print(f"Added {len(folder)} to folder")
    print(f"Last added book is {folder.peek()}")
    folder.pop()
    folder.pop()
    folder.push("Music")
    print(f"Removed two books and added {folder.peek()}")
    print(f"Books in folder: {folder}")