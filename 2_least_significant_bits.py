from PIL import Image
import numpy as np
from math import floor

class least_significant:

    def __init__(self,file_name,final_file,show=False):
        msg=[]
        im = Image.open(file_name)
        im=im.convert('RGB')
            
        original=im.load()
        modified=im.load()

        sizeImagem=im.size
        print('The picture size is '+str(sizeImagem[0])+' x '+str(sizeImagem[1]))
        limite=floor((sizeImagem[0]*sizeImagem[1])*(3/float(4)))
        print('The maximum number of characters that picture supports is : '+str(limite))

        msg=self.getMessage()
        msg=self.ConvertStringToBinary(msg)
        binaryPicture=self.modifyPictureToBinary(modified,original,sizeImagem,len(msg)*4)
        modified=self.modifying(binaryPicture,original,msg,sizeImagem,im,len(msg))

        if show:
            im.show()
        im.save(final_file)


    def getMessage(self):
        msg=list(input("message to be hiden: "))
        return msg

    def ConvertStringToBinary(self,msg):
    #Add the character '#' at the end of the message and convert it to binary.
        for iterator in range(len(msg)):
            letterAscii=ord(msg[iterator])
            msg[iterator]=np.binary_repr(letterAscii,width=8)

        msg.append(np.binary_repr(35,width=8))
    
        return msg

    def modifyPictureToBinary(self,pixelMod,pixelOri,sizeImagem,qtdLoop):
    #Get all RGB numbers of the image and convert them to binary.
        binaryPixel=[]
    
        for i in range(sizeImagem[0]):
            for j in range(sizeImagem[1]):
                for z in range(0,3):
                    binaryPixel.append((str(np.binary_repr(pixelOri[i,j][z],width=8))))
        return binaryPixel

    def modifying(self,binaryMatrix,original,msg,sizeImagem,im,qtdLetter):
    # Replace the last 2 bits from each binary RGB number with the bits of the message to be hidden. 
        original=im.load()
        [count,modifiedPixels,binaryMsg,modificada,resto]=[0,[],'',[],len(msg)%3]
    
        for string in msg:
            binaryMsg+=string

        for binary in binaryMatrix:
            binary=binary[:6]
            binary+=binaryMsg[count]    
            binary+=binaryMsg[count+1]
            modifiedPixels.append(binary)
            count+=2
        
            if count/8>=(qtdLetter):
                break

        count=0
    
        try:
            for i in range(sizeImagem[0]):
                for j in range(sizeImagem[1]):
                    positionI=i
                    positionJ=j
                    original[i,j]=(int(modifiedPixels[count],2),int(modifiedPixels[count+1],2),int(modifiedPixels[count+2],2))
                    count+=3                
        except IndexError:
            if resto==1:
                original[positionI,positionJ]=(int(modifiedPixels[count],2),original[positionI,positionJ][1],original[positionI,positionJ][2])
            if resto==2:
                original[positionI,positionJ]=(int(modifiedPixels[count],2),int(modifiedPixels[count+1],2),original[positionI,positionJ][2])
        return original

#least_significant('face.png','msghiden.png',show=True)
