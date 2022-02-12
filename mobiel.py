class Computer():
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def  config(self):
        print("This Pc is "+ self.cpu +" version an it has ",self.ram ,"gb ram")


dell=Computer("i5",8);
lenovo=Computer("i3",16)
dell.config()
lenovo.config()

