class Diary:
    def __init__(self, student):
        self.student = student
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def show_diary(self):
        print(f"Diary for {self.student}:")
        for subject in self.subjects:
            print(f"Subject: {subject.name}, Grade: {subject.grade}")
