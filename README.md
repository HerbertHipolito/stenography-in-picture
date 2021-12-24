# stenography-in-picture
Algorithm to hide a message in a picture by applying 2 least significant bits using Python. This code transforms the message to be hidden in binary and replaces only the 2
least significant bits from each RGB number of the picture per 2 bits from the converted message. The change in the colour pixels is not significant to be notable.

To run the code you need the follwing dependencies:

PIL, numpy:

python3 -m pip install --upgrade Pillow
pip install numpy

How to use:

the class least_significant of '2_least_significant_bits.py' receives the path of the image you want to hide the message and the name of the resulting image. You can set the parameter show=True if you want to see the image after applying the algorithm. Don't use the character '#' because it is used to recognizer where the last letter of your message is. 

To reveal the message, run 'get_msg.py' and get_msg class with the path of the modified imagem. 

