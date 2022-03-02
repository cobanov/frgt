from deta import Deta

deta = Deta('a047pg0i_9AWgmcVXv8x1JJBM6iQZkMj6gTsm1Q1g')
db = deta.Base('cheatsheets')

## Insert a data
db.insert({
    'key':'tmux',
    'url':'https://gist.githubusercontent.com/cobanov/65aed70d56f4fe832c6c62614ce47650/raw/fdcbd9d9af342ce6a3a07ffed2774de737de93bb/vim.txt',
})


# Fetches all data

url = db.get('tmux')['url']
print(url)
