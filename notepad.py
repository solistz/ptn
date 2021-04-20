class Notepad:
    max_lenght_rows = 10
    rows = []

    def add(self, row):
        self.rows.append(row)

    def remove(self, index):
        self.rows.remove(index)



