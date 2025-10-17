import string
from PIL import Image, ImageGrab
import pyperclip
import time

# These are settings I have found to be helpful for when I want the programe to work on different types of papers. the current set up is default papers. not office paper.
# ffffff or fefefe as close as I can get to the ingame paper background
# I prefer a 36x23 pixel image for this with [head=3]
# head 2 works for 28x18
# head 1 works for 20x13
# no head works for 42x25
# 32 head3 width for librarian books, 38 with no head
# 29 head=3 for crates, 34 no head. same with syndicate cards, 5 hight but always go higher
# 17 wide for nano tasks at head3, 20 no head
charLimit = 10000
width =42
hight =25
def main():
    im = ImageGrab.grabclipboard() # take image from clipboard into program
    # next two lines are used to automatically save the image in the clipboard for history or future use. if you want to use it you must adjust it to fit your file structure.
    #now = time.strftime('C:/Users/YOURCOMPUTERUSERNAME/Documents/SS14/AutoPics/%m-%d_%H;%M;%S.png')
    #im.save(now)
    im = im.resize([width, hight], resample=0) #resize with point sampling
    imWidth, imHight = im.size # get image dimensions
    im = im.convert('P', colors=80) #convert image to a pallette to reduce colors
    #24-32 are safest, higher can work ^
    im = im.convert('RGB') #reconvert to rgb for calculations
    pix = list(im.getdata()) #get rgb value of every pixel
    prevpix = pix[0] #this will be used to determine if color needs to be changed
    idx = 0 #index initialized
    hexi = rgb2hex(pix[idx][0], pix[idx][1], pix[idx][2]) #turn first pixel color into hexcode
    picture = '' #'[head=3]' or whatever head level you want for this.  '' for no head
    picture += '' #serperate so above listings can be used as needed
    picture += '[color='+hexi+']' #decide first pixel's color
    for i in range(hight):
        for j in range(width):
            curpix = pix[idx]
            hexi = rgb2hex(pix[idx][0], pix[idx][1], pix[idx][2])
            if curpix != prevpix: #if new color: recolor and add box character
                picture += '[color='+hexi+']'
            if hexi == '#ffffff' or hexi == '#fefefe':
                picture += '░'
            else: #else same color and add another box
             picture += '█'
            idx += 1 
            prevpix = curpix #track color of last pixel with this
        #picture+='\n'
    picture = picture[:charLimit] #limit to character limit of pages
    pyperclip.copy(picture) #copy result to clipboard
        
    
def rgb2hex(r, g, b): #function to turn 0-255,0-255,0-255 into hex code
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

main()
