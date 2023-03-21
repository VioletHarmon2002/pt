class Publication:
    def init(self, name):
        self.name = name

    def print_information(self):
        print("Name:", self.name)


class Book(Publication):
    def init(self, name, author, page_count):
        super().init(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print("Author:", self.author)
        print("Page count:", self.page_count)


class Magazine(Publication):
    def init(self, name, chief_editor):
        super().init(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print("Chief editor:", self.chief_editor)


donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)

donald_duck.print_information()
print()
compartment_no_6.print_information()