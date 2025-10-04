##url = 'https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=1&t=1s&ab_channel=CodeWithHarry'
##chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
##
##webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
##webbrowser.get('chrome').open_new_tab(url)

import webbrowser
print("1. Chat-gpt\n2. Deep-Seek\n3. Google Gemini\n4. Grok 4\n5. Perplexity Sonar")
user_choice = int(input("Enter Your choice:\t"))

while True:
    match user_choice:
        case 1:#chat
            url = 'https://chatgpt.com/?openaicom_referred=true'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 2:#deep
            url = 'https://chat.deepseek.com/'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 3:#gemini
            url = 'https://gemini.google.com/app'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 4:#grok
            url = 'https://grok.com/'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case 5:#sonar
            url = 'https://docs.perplexity.ai/getting-started/overview'
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            break
        case _:
            print('Invalid Entry')
            break