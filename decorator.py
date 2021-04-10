from abc import abstractmethod,ABC
class PlayerDecorator(ABC):
    @abstractmethod
    def handleinput(self,c):
        pass
    
    
class BaseClass:
    def __init__(self):
        pass
    
    def handleinput(self,c):
        if   c=='w':
            print('moving forward')
        elif c == 'a':
            print('moving left')
        elif c == 's':
            print('moving back')
        elif c == 'd':
            print('moving right')
        elif c == 'e':
            print('attacking ')
        elif c == ' ':
            print('jumping')
        else:
            print('undefined command')
            
            
class BlazingPlayer(PlayerDecorator):
    def __init__(self,wrapper):
        self.wrapper=wrapper
        
    def handleinput(self,c):
        if c == 'e':
            print("using fire ",end ='')
            
        self.wrapper.handleinput(c)
    def extrafunction(self):
        print("extra function")    
        
class BouncingPlayer(PlayerDecorator):
    def __init__(self,wrapper):
        self.wrapper=wrapper
     
   
    def handleinput(self,c):
        if c == 'e':
            print("with arrows ",end =' ')
        self.wrapper.handleinput(c)
        

player = BaseClass()
player.handleinput('e')
player.handleinput('')


player= BlazingPlayer(player)
player.extrafunction()
player.handleinput('e')
player.handleinput(' ')


            
              

                                
        
         