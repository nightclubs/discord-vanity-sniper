import requests, threading, json

f = open('config.json'); config = json.load(f)

def __headers():
    return {

      'authority'              : 'discord.com',
      # 'x-super-properties'     : 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDA3Iiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MjEiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTU0MTg2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
      'x-discord-locale'       : 'en-US',
      'x-debug-options'        : 'bugReporterEnabled',
      'accept-language'        : 'en-US',
      'authorization'          : config['token'],
      'user-agent'             : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9007 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36',
      'accept'                 : '*/*',
      'origin'                 : 'https://discord.com',
      'sec-fetch-site'         : 'same-origin',
      'sec-fetch-mode'         : 'cors',
      'sec-fetch-dest'         : 'empty'
    
    }

def __snipe__vanity():
 with requests.Session() as session:
    snipe_res    = session.patch(
        f"https://discord.com/api/v9/guilds/{config['guild_id']}/vanity-url", 
         headers = __headers(), 
         json    = {'code': config['vanity']}
    )

    if config['vanity'] in snipe_res.text:
        print(f">> [system] {config['vanity']} sniped! :: {config['guild_id']}")
    
    else:
        print(snipe_res.text)

while True: 
 threading.Thread(target=__snipe__vanity).start()