from tinydb import TinyDB

db = TinyDB('gist_db.json')

tmux = {'name':'tmux', 'url':'https://gist.githubusercontent.com/cobanov/e0a8f27f492149fd949cb82cbd05bf33/raw/0b8ec61e182d0a184cb2c841197952df6abce494/tmux.txt'}
vim = {'name':'vim', 'url':'https://gist.githubusercontent.com/cobanov/65aed70d56f4fe832c6c62614ce47650/raw/fdcbd9d9af342ce6a3a07ffed2774de737de93bb/vim.txt'}
repo = {'name':'repo', 'url':'https://gist.githubusercontent.com/cobanov/73f5b8dfd07d302004ce7f43c85ccdd3/raw/d084e3f67fd6cb075e81cd3fd9216da582d00b01/repo.txt'}

db.insert(repo)