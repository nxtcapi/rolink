# what is rolink

rolink is a discord bot that allows you to ban / kick players without having to join the game, as of now there is only 2 commands but i might add more stuff in the future, this was mostly made as a POC

# setup

## 1. the roblox side
 Copy the code from `game/rolink.Lua` and paste it into a new server script called `rolink` and inside `ServerScriptService` 

also make sure you go to game settings > security and enable studio access to api services or messaging service wont work

## 2. python bot setup
open your terminal inside the `bot` folder and install the requirements
```sh
pip install -r requirements.txt
```

## 3. getting the env stuff
- **DISCORD_TOKEN**: go to the discord developer portal, make a new application, go to the bot tab, reset the token, and copy it
- **ROBLOX_UNIVERSE_ID**: go to the roblox creator dashboard, click on your experience, and look at the url. the big number in the url is your universe id (dont confuse this with your place id)
- **ROBLOX_API_KEY**: go to this [page](https://create.roblox.com/dashboard/credentials?activeTab=ApiKeysTab), creat a new api key, give it a name & give it access to "messaging-service" under the access perimissions, you can also set up a whitelisted IP address and experience restriction (both of those are up to you)

## 4. run it
once your `.env` is filled out, just run the bot:
```sh
python main.py
```
now commands should work using your bot
