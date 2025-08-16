import webbrowser
import time
import random
import sys
import pyinputplus as Pyip 

print('Welcome to The Ghost Analyst Google Dorker v1\n')
print('⚠️ Use for educational purposes only.\n')

google_dorks = [
    "https://www.google.com/search?q=site:example.com+intitle:index.of",
    "https://www.google.com/search?q=filetype:pdf+confidential",
    "https://www.google.com/search?q=site:example.com+inurl:login",
    "https://www.google.com/search?q=site:example.com+intext:password",
    "https://www.google.com/search?q=filetype:sql+password",
    "https://www.google.com/search?q=site:example.com+ext:env",
    "https://www.google.com/search?q=site:example.com+intitle:admin",
    "https://www.google.com/search?q=site:example.com+inurl:config",
    "https://www.google.com/search?q=filetype:xls+credentials",
    "https://www.google.com/search?q=site:example.com+inurl:backup"
]

try:
    ask = Pyip.inputInt("""
Choose your option:
    1. Directly open a random google dork
    2. Input search query to open your own specified dork
    3. Explore default dorks and choose which to open
    4. Ethics and guidelines of google dorking
    5. Exit
>>>>>>> """)

    if ask == 1:
        dork = random.choice(google_dorks)
        print(f'Opening dork in browser:\n{dork}')
        time.sleep(1)
        webbrowser.open(dork)

    elif ask == 2:
        query = input("Enter your custom search query (eg., site:example.com intext:Ethics): ").strip()
        if query:
            dork = (f"https://www.google.com/search?q={query}")
            print(f'Opening your custom dork:\n{dork}')
            time.sleep(1)
            webbrowser.open(dork)
        else:
            print("❌ Query cannot be empty.")

    elif ask == 3:
        print('Getting list of google dorks from Database...\n')
        time.sleep(1)
        for i, dork in enumerate(google_dorks, start=1):
            print(f"{i}. {dork}")
        new = input("\nSince you have seen list of available google dorks enter your custom search query (eg., site:example.com intext:Ethics): ").strip()
        if new:
            put = (f"https://www.google.com/search?q={new}")
            print(f'Opening your custom dork:\n{put}')
            time.sleep(1)
            webbrowser.open(put)
        else:
            print("❌ Query cannot be empty.")

    elif ask == 4:
        print("""
⚖️ Ethics & Guidelines of Google Dorking:
- Use ONLY on sites you own or have explicit permission to test.
- Do not exploit sensitive data you find.
- Report vulnerabilities responsibly.
- Treat this tool as a learning/OSINT aid, not a weapon.
        """)

    elif ask == 5:
        print("👋 Leaving so soon? Thanks for trying it out.")

    else:
        print("❌ Choose option from 1-5")

except KeyboardInterrupt:
    print("\n\n✋ Keyboard interrupt detected. Exiting gracefully...")
    sys.exit()
