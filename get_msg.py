from PIL import Image
import numpy as np


class get_msg:

    def __init__(self,file_name,show=False):

        im = Image.open(file_name)
        im=im.convert('RGB')
        image=im.load()
        size_imagem=im.size

        print(self.getMsgBinary(image,size_imagem))

        if show:
            im.show()
    
    def getMsgBinary(self,image,size_imagem):

        [byte,letter,count]=[[],[],0]
        
        for i in range(size_imagem[0]):
            for j in range(size_imagem[1]):
                for z in range(0,3):
                    byte.append(np.binary_repr(image[i,j][z],width=8)[6])
                    byte.append(np.binary_repr(image[i,j][z],width=8)[7])
                    count+=1
                    if len(byte)>=8:
                        byte=self.gatherChar(byte)
                        if 35==int(byte,2):
                            return self.gatherChar(letter)
                        else:
                            letter.append(chr(int(byte,2)))
                            byte=[] 
                

    def gatherChar(self,letters):
    
        string=''

        for letter in letters:
            string+=letter

        return string

get_msg('msghiden.png',show=False)
