import requests
import json
import time
import random
from random import choice
from random import randint
from string import ascii_uppercase
import base64
import config
import utils.crypto as crypto

# account information
def user(ver, os, token, secret, first):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user'
        auth = crypto.mac(ver, token, secret, 'GET', '/user')
        if first == False:
            code = config.gb_code
        else:
            code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/user'
        auth = crypto.mac(ver, token, secret, 'GET', '/user')
        if first == False:
            code = config.jp_code
        else:
            code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# box contents
def cards(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/cards'
        auth = crypto.mac(ver, token, secret, 'GET', '/cards')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/cards'
        auth = crypto.mac(ver, token, secret, 'GET', '/cards')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# current news
def news(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/announcements?display=home'
        auth = crypto.mac(ver, token, secret, 'GET', '/announcements?display=home')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/announcements?display=home'
        auth = crypto.mac(ver, token, secret, 'GET', '/announcements?display=home')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# current banners
def banners(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/gashas'
        auth = crypto.mac(ver, token, secret, 'GET', '/gashas')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/gashas'
        auth = crypto.mac(ver, token, secret, 'GET', '/gashas')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# current events
def events(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/events'
        auth = crypto.mac(ver, token, secret, 'GET', '/events')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/events'
        auth = crypto.mac(ver, token, secret, 'GET', '/events')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# change account name
def changeName(ver, os, token, secret, name):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/user'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    data = {'user':{'name': name}}
    r = requests.put(url, data=json.dumps(data), headers=headers)
    return r.json()

# increase box size by 5
def capacity(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user/capacity/card'
        auth = crypto.mac(ver, token, secret, 'POST', '/user/capacity/card')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/user/capacity/card'
        auth = crypto.mac(ver, token, secret, 'POST', '/user/capacity/card')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.post(url, data=None, headers=headers)
    return r.json()

# starter banner status
def dashStatus(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/start_dash_gasha_status'
        auth = crypto.mac(ver, token, secret, 'GET', '/start_dash_gasha_status')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/start_dash_gasha_status'
        auth = crypto.mac(ver, token, secret, 'GET', '/start_dash_gasha_status')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# summon on a banner
def summon(ver, os, token, secret, id, course):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/gashas/' + str(id) + '/courses/' + str(course) + '/draw'
        auth = crypto.mac(ver, token, secret, 'POST', '/gashas/' + str(id) + '/courses/' + str(course) + '/draw')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/gashas/' + str(id) + '/courses/' + str(course) + '/draw'
        auth = crypto.mac(ver, token, secret, 'POST', '/gashas/' + str(id) + '/courses/' + str(course) + '/draw')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.post(url, data=None, headers=headers)
    return r.json()

# list of gifts
def gifts(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/gifts'
        auth = crypto.mac(ver, token, secret, 'GET', '/gifts')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/gifts'
        auth = crypto.mac(ver, token, secret, 'GET', '/gifts')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# accept gifts
def acceptGifts(ver, os, token, secret, gift):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/gifts/accept'
        auth = crypto.mac(ver, token, secret, 'POST', '/gifts/accept')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/gifts/accept'
        auth = crypto.mac(ver, token, secret, 'POST', '/gifts/accept')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    data = {'gift_ids': gift}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# list of missions
def missions(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/missions'
        auth = crypto.mac(ver, token, secret, 'GET', '/missions')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/missions'
        auth = crypto.mac(ver, token, secret, 'GET', '/missions')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# accept missions
def acceptMissions(ver, os, token, secret, mission):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/missions/accept'
        auth = crypto.mac(ver, token, secret, 'POST', '/missions/accept')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/missions/accept'
        auth = crypto.mac(ver, token, secret, 'POST', '/missions/accept')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    data = {'mission_ids': mission}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# stone stamina refill
def actRefill(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user/recover_act_with_stone'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user/recover_act_with_stone')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/user/recover_act_with_stone'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user/recover_act_with_stone')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.put(url, data=None, headers=headers)
    return r.json()

# sell cards
def sell(ver, os, token, secret, card):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/cards/sell'
        auth = crypto.mac(ver, token, secret, 'POST', '/cards/sell')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/cards/sell'
        auth = crypto.mac(ver, token, secret, 'POST', '/cards/sell')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    data = {'card_ids': card}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# set wallpaper
def setWallpaper(ver, os, token, secret, wallpaper):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/user'
        auth = crypto.mac(ver, token, secret, 'PUT', '/user')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    data = {'user': {'wallpaper_item_id': wallpaper}}
    r = requests.put(url, data=json.dumps(data), headers=headers)
    return r.json()

# story stages
def quests(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/user_areas'
        auth = crypto.mac(ver, token, secret, 'GET', '/user_areas')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/user_areas'
        auth = crypto.mac(ver, token, secret, 'GET', '/user_areas')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# stage supports
def getSupports(ver, os, token, secret, stage, difficulty):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/quests/' + str(stage) + '/supporters'
        auth = crypto.mac(ver, token, secret, 'GET', '/quests/' + str(stage) + '/supporters')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/quests/' + str(stage) + '/supporters'
        auth = crypto.mac(ver, token, secret, 'GET', '/quests/' + str(stage) + '/supporters')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# get all medals
def getMedals(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/awakening_items'
        auth = crypto.mac(ver, token, secret, 'GET', '/awakening_items')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/awakening_items'
        auth = crypto.mac(ver, token, secret, 'GET', '/awakening_items')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# get all items (orbs, training, support, treasure, special)
def getItems(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/resources/login?potential_items=true&training_items=true&support_items=true&treasure_items=true&special_items=true'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?potential_items=true&training_items=true&support_items=true&treasure_items=true&special_items=true')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/resources/login?potential_items=true&training_items=true&support_items=true&treasure_items=true&special_items=true'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?potential_items=true&training_items=true&support_items=true&treasure_items=true&special_items=true')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# list of dragonball locations
def dragonballs(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/dragonball_sets'
        auth = crypto.mac(ver, token, secret, 'GET', '/dragonball_sets')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/dragonball_sets'
        auth = crypto.mac(ver, token, secret, 'GET', '/dragonball_sets')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# friend list
def friends(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/friendships'
        auth = crypto.mac(ver, token, secret, 'GET', '/friendships')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/friendships'
        auth = crypto.mac(ver, token, secret, 'GET', '/friendships')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# search friend by user ID
def findFriend(ver, os, token, secret, id):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/users/' + str(id)
        auth = crypto.mac(ver, token, secret, 'GET', '/users/' + str(id))
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/users/' + str(id)
        auth = crypto.mac(ver, token, secret, 'GET', '/users/' + str(id))
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# add friend
def addFriend(ver, os, token, secret, id):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/users/' + str(id) + '/friendships'
        auth = crypto.mac(ver, token, secret, 'POST', '/users/' + str(id) + '/friendships')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/users/' + str(id) + '/friendships'
        auth = crypto.mac(ver, token, secret, 'POST', '/users/' + str(id) + '/friendships')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.post(url, headers=headers)
    return r.json()

# accept pending friend
def acceptFriend(ver, os, token, secret, id):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/friendships/' + str(id) + '/accept'
        auth = crypto.mac(ver, token, secret, 'PUT', '/friendships/' + str(id) + '/accept')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/friendships/' + str(id) + '/accept'
        auth = crypto.mac(ver, token, secret, 'PUT', '/friendships/' + str(id) + '/accept')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.put(url, headers=headers)
    return r.json()

# list of decks on the account.
def getTeams(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/teams'
        auth = crypto.mac(ver, token, secret, 'GET', '/teams')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/teams'
        auth = crypto.mac(ver, token, secret, 'GET', '/teams')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# set deck cards by deck number on the account.
def setTeam(ver, os, token, secret, team, cards):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/teams'
        auth = crypto.mac(ver, token, secret, 'POST', '/teams')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/teams'
        auth = crypto.mac(ver, token, secret, 'POST', '/teams')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    data = {'selected_team_num': int(team), 'user_card_teams': cards}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# start a stage by ID & difficulty
def startStage(ver, os, token, secret, stage, difficulty, friend, friend_card):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/quests/' + str(stage) + '/sugoroku_maps/start'
        auth = crypto.mac(ver, token, secret, 'POST', '/quests/' + str(stage) + '/sugoroku_maps/start')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/quests/' + str(stage) + '/sugoroku_maps/start'
        auth = crypto.mac(ver, token, secret, 'POST', '/quests/' + str(stage) + '/sugoroku_maps/start')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2

    APIToken = ''.join(random.choice(list('abcdefghijklmnopqrstuvwxyzBCDEFGHIKLMNOPQRUVWXYZ123456789-_')) for i in range(63))

    decks = getTeams(ver, os, token, secret)

    if len(str(friend)) >= 4:
        sign = json.dumps({'difficulty': int(difficulty), 'friend_id': int(friend), 'is_playing_script': True, 'selected_team_num': int(decks['selected_team_num']), 'support_leader': {'card_id': int(friend_card), 'exp': 0, 'optimal_awakening_step': 0, 'released_rate': 0}})
        enc_sign = crypto.encrypt_sign(sign)
    else:
        sign = json.dumps({'difficulty': int(difficulty), 'cpu_friend_id': int(friend), 'is_playing_script': True, 'selected_team_num': int(decks['selected_team_num'])})
        enc_sign = crypto.encrypt_sign(sign)

    headers = {
        'User-Agent': dua,
        'Accept': '*/*',
        'Authorization': auth,
        'Content-Type': 'application/json',
        'X-Platform': os,
        'X-AssetVersion': '////',
        'X-DatabaseVersion': '////',
        'X-ClientVersion': code
    }
    data = {'sign': enc_sign}

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# finish stage by ID & difficulty
def finishStage(ver, os, token, secret, stage, difficulty, paces, defeated, stoken):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/quests/' + str(stage) + '/sugoroku_maps/finish'
        auth = crypto.mac(ver, token, secret, 'POST', '/quests/' + str(stage) + '/sugoroku_maps/finish')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/quests/' + str(stage) + '/sugoroku_maps/finish'
        auth = crypto.mac(ver, token, secret, 'POST', '/quests/' + str(stage) + '/sugoroku_maps/finish')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2

    finish = int(round(time.time(), 0) + 90)
    start = finish - randint(6200000, 8200000)
    damage = randint(500000, 1000000)

    # Hercule punching bag event damage
    if str(stage)[0:3] in ('711', '185'):
        damage = randint(100000000, 101000000)

    sign = {
        'actual_steps': paces,
        'difficulty': difficulty,
        'elapsed_time': finish - start,
        'energy_ball_counts_in_boss_battle': [4, 6, 0, 6, 4, 3, 0, 0, 0, 0, 0, 0, 0, ],
        'has_player_been_taken_damage': False,
        'is_cheat_user': False,
        'is_cleared': True,
        'is_defeated_boss': True,
        'is_player_special_attack_only': True,
        'max_damage_to_boss': damage,
        'min_turn_in_boss_battle': len(defeated),
        'passed_round_ids': defeated,
        'quest_finished_at_ms': finish,
        'quest_started_at_ms': start,
        'steps': paces,
        'token': stoken
    }

    enc_sign = crypto.encrypt_sign(json.dumps(sign))

    headers = {
        'User-Agent': dua,
        'Accept': '*/*',
        'Authorization': auth,
        'Content-Type': 'application/json',
        'X-Platform': os,
        'X-AssetVersion': '////',
        'X-DatabaseVersion': '////',
        'X-ClientVersion': code
    }
    data = {'sign': enc_sign}

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# eza rankings
def zRankings(ver, os, token, secret, eza):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/z_battles/' + str(eza) + '/rankings'
        auth = crypto.mac(ver, token, secret, 'GET', '/z_battles/' + str(eza) + '/rankings')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/z_battles/' + str(eza) + '/rankings'
        auth = crypto.mac(ver, token, secret, 'GET', '/z_battles/' + str(eza) + '/rankings')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# eza support units
def zSupports(ver, os, token, secret, eza):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/z_battles/' + str(eza) + '/supporters'
        auth = crypto.mac(ver, token, secret, 'GET', '/z_battles/' + str(eza) + '/supporters')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/z_battles/' + str(eza) + '/supporters'
        auth = crypto.mac(ver, token, secret, 'GET', '/z_battles/' + str(eza) + '/supporters')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# start eza by level
def zStart(ver, os, token, secret, eza, level, friend, friend_card):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/z_battles/' + str(eza) + '/start'
        auth = crypto.mac(ver, token, secret, 'POST', '/z_battles/' + str(eza) + '/start')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/z_battles/' + str(eza) + '/start'
        auth = crypto.mac(ver, token, secret, 'POST', '/z_battles/' + str(eza) + '/start')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2

    APIToken = ''.join(random.choice(list('abcdefghijklmnopqrstuvwxyzBCDEFGHIKLMNOPQRUVWXYZ123456789-_')) for i in range(63))

    decks = getTeams(ver, os, token, secret)

    sign = json.dumps({'friend_id': int(friend), 'level': int(level), 'selected_team_num': int(decks['selected_team_num']), 'support_leader': {'card_id': int(friend_card), 'exp': 0, 'optimal_awakening_step': 0, 'released_rate': 0}})
    enc_sign = crypto.encrypt_sign(sign)

    headers = {
        'User-Agent': dua,
        'Accept': '*/*',
        'Authorization': auth,
        'Content-Type': 'application/json',
        'X-Platform': os,
        'X-AssetVersion': '////',
        'X-DatabaseVersion': '////',
        'X-ClientVersion': code
    }
    data = {'sign': enc_sign}

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# finish eza by level
def zFinish(ver, os, token, secret, eza, level, stoken, em_atk, em_hp):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/z_battles/' + str(eza) + '/finish'
        auth = crypto.mac(ver, token, secret, 'POST', '/z_battles/' + str(eza) + '/finish')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/z_battles/' + str(eza) + '/finish'
        auth = crypto.mac(ver, token, secret, 'POST', '/z_battles/' + str(eza) + '/finish')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    
    finish = int(round(time.time(), 0) + 90)
    start = finish - randint(6200000, 8200000)

    summary = {
        'summary':{
            'enemy_attack': int(em_atk),
            'enemy_attack_count': 1,
            'enemy_heal_counts': [0],
            'enemy_heals': [0],
            'enemy_max_attack': int(em_atk),
            'enemy_min_attack': int(em_atk),
            'player_attack_counts': [3],
            'player_attacks': em_hp,
            'player_heal': 0,
            'player_heal_count': 0,
            'player_max_attacks': em_hp,
            'player_min_attacks': em_hp,
            'type': 'summary'
        }
    }

    headers = {
        'User-Agent': dua,
        'Accept': '*/*',
        'Authorization': auth,
        'Content-Type': 'application/json',
        'X-Platform': os,
        'X-AssetVersion': '////',
        'X-DatabaseVersion': '////',
        'X-ClientVersion': code
    }
    data = {
        'elapsed_time': finish - start,
        'is_cleared': True,
        'level': int(level),
        'reason': 'win',
        's': 'iwM9xu4mM/7fZyLfKV93JaquLtLzpP35CKBoDiB+X8k=',
        't': base64.b64encode(json.dumps(summary).encode()).decode(),
        'token': str(stoken),
        'used_items': [],
        'z_battle_finished_at_ms': finish,
        'z_battle_started_at_ms': start
    }

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# unknown
def unpublished(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/unpublished_masters'
        auth = crypto.mac(ver, token, secret, 'GET', '/unpublished_masters')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/unpublished_masters'
        auth = crypto.mac(ver, token, secret, 'GET', '/unpublished_masters')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': '////',
        'X-DatabaseVersion': '////',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# train card
def train(ver, os, token, secret, card, cards, field, items):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/cards/' + str(card) + '/train'
        auth = crypto.mac(ver, token, secret, 'PUT', '/cards/' + str(card) + '/train')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/cards/' + str(card) + '/train'
        auth = crypto.mac(ver, token, secret, 'PUT', '/cards/' + str(card) + '/train')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    data = {
        'card_ids': cards,
        'training_field_id': int(field),
        'training_items': items
        } #{"item_id":903,"quantity":1}
    r = requests.put(url, data=json.dumps(data), headers=headers)
    return r.json()

# banner treasure list?
def special(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/special_items'
        auth = crypto.mac(ver, token, secret, 'GET', '/special_items')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/special_items'
        auth = crypto.mac(ver, token, secret, 'GET', '/special_items')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# comeback login, celebration gifts, hercule gift, budokai, battlefield, & others.
def homeResources(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/resources/home?apologies=true&banners=true&bonus_schedules=true&budokai=true&gifts=true&login_bonuses=true&random_login_bonuses=true&recommends=true&rmbattles=true&sns_campaign=true'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/home?apologies=true&banners=true&bonus_schedules=true&budokai=true&gifts=true&login_bonuses=true&random_login_bonuses=true&recommends=true&rmbattles=true&sns_campaign=true')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/resources/home?apologies=true&banners=true&bonus_schedules=true&budokai=true&gifts=true&login_bonuses=true&random_login_bonuses=true&recommends=true&rmbattles=true&sns_campaign=true'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/home?apologies=true&banners=true&bonus_schedules=true&budokai=true&gifts=true&login_bonuses=true&random_login_bonuses=true&recommends=true&rmbattles=true&sns_campaign=true')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# EXP bonus rate.
def bonus(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/bonus_schedules'
        auth = crypto.mac(ver, token, secret, 'GET', '/bonus_schedules')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/bonus_schedules'
        auth = crypto.mac(ver, token, secret, 'GET', '/bonus_schedules')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# request items exchangeable.
def babaItems(ver, os, token, secret, currency):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/shops/' + currency + '/items'
        auth = crypto.mac(ver, token, secret, 'GET', '/shops/' + currency + '/items')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/shops/' + currency + '/items'
        auth = crypto.mac(ver, token, secret, 'GET', '/shops/' + currency + '/items')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# buy items from babashop.
def babaBuy(ver, os, token, secret, currency, id, amount):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/shops/' + currency + '/items/' + id + '/buy'
        auth = crypto.mac(ver, token, secret, 'POST', '/shops/' + currency + '/items/' + id + '/buy')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/shops/' + currency + '/items/' + id + '/buy'
        auth = crypto.mac(ver, token, secret, 'POST', '/shops/' + currency + '/items/' + id + '/buy')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-Language': config.lang,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'User-Agent': dua
        }
    data = {
        'bought_num': int(amount)
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# request current clash clearance information.
def clashInfo(ver, os, token, secret, clash):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/rmbattles/' + str(clash)
        auth = crypto.mac(ver, token, secret, 'GET', '/rmbattles/' + str(clash))
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/rmbattles/' + str(clash)
        auth = crypto.mac(ver, token, secret, 'GET', '/rmbattles/' + str(clash))
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'X-Language': config.lang,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# request clash level usable cards.
def clashCards(ver, os, token, secret, level):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/rmbattles/teams/' + str(level)
        auth = crypto.mac(ver, token, secret, 'GET', '/rmbattles/teams/' + str(level))
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/rmbattles/teams/' + str(level)
        auth = crypto.mac(ver, token, secret, 'GET', '/rmbattles/teams/' + str(level))
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'X-Language': config.lang,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# start clash level.
def clashStart(ver, os, token, secret, clash, id, begin, leader, sub, cards):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/rmbattles/' + str(clash) + '/stages/' + str(id) + '/start'
        auth = crypto.mac(ver, token, secret, 'POST', '/rmbattles/' + str(clash) + '/stages/' + str(id) + '/start')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/rmbattles/' + str(clash) + '/stages/' + str(id) + '/start'
        auth = crypto.mac(ver, token, secret, 'POST', '/rmbattles/' + str(clash) + '/stages/' + str(id) + '/start')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'X-Language': config.lang,
        'User-Agent': dua
        }
    data = {
        'is_beginning': bool(begin),
        'user_card_ids': {
            'leader': int(leader),
            'members': cards,
            'sub_leader': int(sub)
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# end clash level.
def clashEnd(ver, os, token, secret, clash, hp, rounds, stoken):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/rmbattles/' + str(clash) + '/stages/finish'
        auth = crypto.mac(ver, token, secret, 'POST', '/rmbattles/' + str(clash) + '/stages/finish')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/rmbattles/' + str(clash) + '/stages/finish'
        auth = crypto.mac(ver, token, secret, 'POST', '/rmbattles/' + str(clash) + '/stages/finish')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'X-Language': config.lang,
        'User-Agent': dua
        }
    finish = int(round(time.time(), 0) + 90)
    start = finish - randint(6200000, 8200000)
    data = {
        'damage': int(hp),
        'finished_at_ms': finish,
        'finished_reason': 'win',
        'is_cleared': True,
        'remaining_hp': 0,
        'round': int(rounds),
        'started_at_ms': start,
        'token': stoken
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# favorite card by unique box ID.
def favorite(ver, os, token, secret, uniqueCard):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/cards/' + uniqueCard + '/favorite'
        auth = crypto.mac(ver, token, secret, 'PUT', '/cards/' + uniqueCard + '/favorite')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/cards/' + uniqueCard + '/favorite'
        auth = crypto.mac(ver, token, secret, 'PUT', '/cards/' + uniqueCard + '/favorite')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'X-Language': config.lang,
        'User-Agent': dua
        }
    data = {
        'card': {
            'is_favorite': True
        }
    }
    r = requests.put(url, data=json.dumps(data), headers=headers)
    return r.json()

# request account summon history.
def history(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/gashas/histories'
        auth = crypto.mac(ver, token, secret, 'GET', '/gashas/histories')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/gashas/histories'
        auth = crypto.mac(ver, token, secret, 'GET', '/gashas/histories')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'X-Language': config.lang,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# not exactly sure what this does...
def missionsForward(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/missions/put_forward'
        auth = crypto.mac(ver, token, secret, 'POST', '/missions/put_forward')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/missions/put_forward'
        auth = crypto.mac(ver, token, secret, 'POST', '/missions/put_forward')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'X-Language': config.lang,
        'User-Agent': dua
        }
    r = requests.post(url, data=None, headers=headers)
    return r.json()

# some login info that seems irrelevant.
def loginResources(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/resources/login?act_items=true&announcements=true&awakening_items=true&budokai=true&card_tags=true&cards=true&dragonball_sets=true&eventkagi_items=true&friendships=true&gashas=true&gifts=true&login_movies=true&login_popups=true&missions=true&potential_items=true&recommends=true&rmbattles=true&shops/treasure/items=true&support_items=true&support_leaders=true&teams=true&training_fields=true&training_items=true&treasure_items=true&user_areas=true&wallpaper_items=true'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?act_items=true&announcements=true&awakening_items=true&budokai=true&card_tags=true&cards=true&dragonball_sets=true&eventkagi_items=true&friendships=true&gashas=true&gifts=true&login_movies=true&login_popups=true&missions=true&potential_items=true&recommends=true&rmbattles=true&shops/treasure/items=true&support_items=true&support_leaders=true&teams=true&training_fields=true&training_items=true&treasure_items=true&user_areas=true&wallpaper_items=true')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/resources/login?act_items=true&announcements=true&awakening_items=true&budokai=true&card_tags=true&cards=true&dragonball_sets=true&eventkagi_items=true&friendships=true&gashas=true&gifts=true&login_movies=true&login_popups=true&missions=true&potential_items=true&recommends=true&rmbattles=true&shops/treasure/items=true&support_items=true&support_leaders=true&teams=true&training_fields=true&training_items=true&treasure_items=true&user_areas=true&wallpaper_items=true'
        auth = crypto.mac(ver, token, secret, 'GET', '/resources/login?act_items=true&announcements=true&awakening_items=true&budokai=true&card_tags=true&cards=true&dragonball_sets=true&eventkagi_items=true&friendships=true&gashas=true&gifts=true&login_movies=true&login_popups=true&missions=true&potential_items=true&recommends=true&rmbattles=true&shops/treasure/items=true&support_items=true&support_leaders=true&teams=true&training_fields=true&training_items=true&treasure_items=true&user_areas=true&wallpaper_items=true')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'X-Language': config.lang,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# not sure what this does...
def announceNotify(ver, os, token, secret):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/announcements/notify'
        auth = crypto.mac(ver, token, secret, 'GET', '/announcements/notify')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/announcements/notify'
        auth = crypto.mac(ver, token, secret, 'GET', '/announcements/notify')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'X-Language': config.lang,
        'User-Agent': dua
        }
    r = requests.get(url, data=None, headers=headers)
    return r.json()

# claim random gifts e.g. hercule
def claimRandomLogin(ver, os, token, secret, elapsed, expire, id, gtoken):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if ver == 'gb':
        url = config.gb_url + '/random_login_bonuses/' + id + '/accept'
        auth = crypto.mac(ver, token, secret, 'POST', '/random_login_bonuses/' + id + '/accept')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/random_login_bonuses/' + id + '/accept'
        auth = crypto.mac(ver, token, secret, 'POST', '/random_login_bonuses/' + id + '/accept')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'X-Language': config.lang,
        'User-Agent': dua
        }
    data = {
        'elapsed_days': elapsed,
        'expire': expire,
        'random_login_bonus_id': id,
        'token': gtoken
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

# get wishes or make a wish.
def wish(ver, os, token, secret, set, wish):
    if os == 'android':
        dua = config.device_agent1
    else:
        dua = config.device_agent2
    if wish == None:
        method = 'GET'
    else:
        method = 'POST'
    if ver == 'gb':
        url = config.gb_url + '/dragonball_sets/' + str(set) + '/wishes'
        auth = crypto.mac(ver, token, secret, method, '/dragonball_sets/' + str(set) + '/wishes')
        code = config.gb_code
        asset = config.file_ts1
        db = config.db_ts1
    else:
        url = config.jp_url + '/dragonball_sets/' + str(set) + '/wishes'
        auth = crypto.mac(ver, token, secret, method, '/dragonball_sets/' + str(set) + '/wishes')
        code = config.jp_code
        asset = config.file_ts2
        db = config.db_ts2
    headers = {
        'X-Platform': os,
        'X-ClientVersion': code,
        'X-AssetVersion': asset,
        'X-DatabaseVersion': db,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': auth,
        'X-Language': config.lang,
        'User-Agent': dua
        }
    if wish == None:
        r = requests.get(url, data=None, headers=headers)
    else:
        data = {
            'dragonball_wish_ids': wish
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()