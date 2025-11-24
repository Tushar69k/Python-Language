class dog : 
    def voice(self) : 
        print("Bhow Bhow")

class Cat(dog) : 
    def voicee(self) : 
        print("Meow Meow")
        
class Cow(Cat) : 
    def voiceee(self) : 
        print("Hammaaaaa")


d = dog()
d.voice()

ca = Cat()
ca.voice()
        
co = Cow()
co.voice()



print("Using all Function from single class :: ")

P = Cow()
P.voice()
P.voicee()
P.voiceee()