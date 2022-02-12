class Computer():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def update(self):
        self.name="Shivam"
    def compare(self,other):
        if self.name==other.name:
            return True
        else:
            return False





a=Computer("Mohit",22)
b=Computer("Gaurav",23)

a.update()

print(a.compare(b))

