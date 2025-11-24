class dog : 
    def voice(self) : 
        print("bhow")

class cat(dog) : 
    def voicee(self) : 
        print("Meow")
class Cow(cat) : 
    def voiceee(self) : 
        print("Hamma")

c = Cow()
c.voice()        
c.voicee()        
c.voiceee()        