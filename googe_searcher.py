import webbrowser
import os

# Define the path to Chrome (adjust if your Chrome is installed elsewhere)
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# Check if Chrome exists at the specified path
if not os.path.exists(chrome_path):
    print("Google Chrome not found at the specified path.")
else:
    # Register Chrome as a browser
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

    # Get user input
    query = input("Enter your search query: ")

    # Format the Google search URL
    search_url = f"https://www.google.com/search?q={query}"

    # Open the search in Chrome
    webbrowser.get('chrome').open(search_url)

##"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"