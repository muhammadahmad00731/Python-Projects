import webbrowser
import numpy as np
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##url = 'https://www.youtube.com/watch?v=RDIWT43ZQIo&ab_channel=JunaidAkram'     |
##chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"     |
##                                                                               |-->"to open any link"
##webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path)) |
##webbrowser.get('chrome').open_new_tab(url)                                     |
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
user_input = input(print('Presss\'Q\' to Quit.\nOR\nPress\'L\' to check the list of videos:\t'))

list_of_videos = np.array(['Introduction','Data Types','f-string', 'Comments and Escape Sequence','Lists','Tuples','Tuples-Method','Dictionaries','Recursion','Sets','List-Comprehension','if/else','Match case','break and continue','pass','While-Loop','For-Loop','Lambda Function','Functions','Files I/O','read()/readlines()','Writing-Files','Try/Except','Local vs Global variables','Enumerate','Classes / Objectss','Class Methods','super keyword','__init__ , __str__','Inheritance','Getters and Setters','Static Methods','Polymorphism','Encapsulation','Time Module'])
i=1
while True:
    if (user_input == 'q' or user_input == 'Q'):
        break

    elif (user_input == 'l' or user_input == 'L'):
        while (i <= len(list_of_videos)):
            for x in list_of_videos:
                print(f'{i}-{x}')
                i+=1
##        break
    user_2nd_input = int(input(print("Enter the number of the topic form the list:\t")))
##    print(list_of_videos[user_2nd_input - 1])
    video_number = (user_2nd_input - 1)
    match video_number:
        case 0:
            url = 'https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=1&t=1s&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 1:
            url = 'https://www.youtube.com/watch?v=ORCuz7s5cCY&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=6&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 2:
            url = 'https://www.youtube.com/watch?v=ixmxgUf8yIg&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 3:
            url = 'https://www.youtube.com/watch?v=qxPMmW93eDs&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 4:
            url = 'https://www.youtube.com/watch?v=eF6nK5bSlmg&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 5:
            url = 'https://www.youtube.com/watch?v=PipsOUDKrVk&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 6:
            url = 'https://www.youtube.com/watch?v=XblLSduioJI&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 7:
            url = 'https://www.youtube.com/watch?v=j2G68uQtOwM&t=464s&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 8:
            url = 'https://www.youtube.com/watch?v=XYwJKFB8DUk&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 9:
            url = 'https://www.youtube.com/watch?v=l3kCO8cVA6o&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 10:
            url = 'https://www.youtube.com/watch?v=D2h_qI6Tx4M&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 11:
            url = 'https://www.youtube.com/watch?v=ceiuLR2ysas&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 12:
            url = 'https://www.youtube.com/watch?v=bthQCK1QAmQ&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 13:
            url = 'https://www.youtube.com/watch?v=RkwJnjdrm70&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 14:
            url = 'https://www.youtube.com/watch?v=KYclL3ugFCU&ab_channel=IBMTechTamil'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 15:
            url = 'https://www.youtube.com/watch?v=-tCFyIyKVx0&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 16:
            url = 'https://www.youtube.com/watch?v=fIYVzKp0q5w&t=273s&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 17:
            url = 'https://www.youtube.com/watch?v=UfFWf-PXUqE&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 18:
            url = 'https://www.youtube.com/watch?v=dyvxxJSGUsE&t=5s&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 19:
            url = 'https://www.youtube.com/watch?v=eDBPlcWYses&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 20:
            url = 'https://www.youtube.com/watch?v=l1FsnQxET9U&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 21:
            url = 'https://www.youtube.com/watch?v=4LKo6dlku7M&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 22:
            url = 'https://www.youtube.com/watch?v=RaG6GgcDt54&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 23:
            url = 'https://www.youtube.com/watch?v=RaG6GgcDt54&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 24:
            url = 'https://www.youtube.com/watch?v=kGnYc_h1geM&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 25:
            url = 'https://www.youtube.com/watch?v=a7baAGCBA9U&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 26:
            url = 'https://www.youtube.com/watch?v=9ynmDLc5FYo&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 27:
            url = 'https://www.youtube.com/watch?v=P648reefNh0&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 28:
            url = 'https://www.youtube.com/watch?v=12HRkYld22c&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 29:
            url = 'https://www.youtube.com/watch?v=-KsfUaQEY9Y&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 30:
            url = 'https://www.youtube.com/watch?v=2gbCT8h9uyk&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 31:
            url = 'https://www.youtube.com/watch?v=GcSVYNSsJxo&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 32:
            url = 'https://www.youtube.com/watch?v=xnb-9TI-BjQ&t=1s&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 33:
            url = 'https://www.youtube.com/watch?v=wySW_E4XsvE&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 34:
            url = 'https://www.youtube.com/watch?v=oTtIvV-Q1FY&ab_channel=CodeWithHarry'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case _:
            print('Invalid Entry')
            break