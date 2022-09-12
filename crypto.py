import arabic_reshaper
from bidi.algorithm import get_display
from colorama import Fore, Back, Style
import fontstyle
encrypted = input("Enter the string: ")

arabic = ['ذ','ض','ص','ث','ق','ف','غ','ع','ه','خ','ح','ج','د','ش','س','ي','ب','ل','ا','ت','ن','م'
          ,'ك','ط','ئ','ء','ؤ','ر','لا','ى','ة','و','ز','ظ',' ']

english = ['`','q','w','e','r','t','y','u','i','o','p','[',']','a','s','d','f','g','h','j','k','l'
          ,';','\'','z','x','c','v','b','n','m',',','.','/',' ']

translator = dict(zip(english,arabic))

decrypted = ""

for x in encrypted:
    decrypted+=translator[x]

arabicReshape = arabic_reshaper.reshape(decrypted)

disp = get_display(arabicReshape)

Styled = fontstyle.apply(disp,'bold/red')

finalAppearence= """
===========================================================================
=                                                                         
=                             {}                                          
=                                                                         
===========================================================================
""".format(Styled)
print(finalAppearence)
