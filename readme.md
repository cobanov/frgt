![frgt](https://github.com/cobanov/frgt/blob/main/static/frgt.png?raw=true)

# frgt.dev

[frgt.dev](https://www.frgt.dev) is a terminal based cheatsheet helper for developers

## Install
```bash
/bin/bash -c "$(curl -fsSL https://gist.githubusercontent.com/cobanov/0a27716624b46461d9717b6c0509af41/raw/fce9ad243b1c3fb740c4223b6ee336bb9b1f5694/install.sh)"
```
## Usage
Whenever you forget something just use this.
```bash
curl -L frgt.dev/tmux
```
```
# Window
CTRL + B C	create window
CTRL + B 0 … 9	select window by number
CTRL + B &	kill window

# Pane
CTRL + B %	vertical split
CTRL + B “	horizontal split
CTRL + B X	kill pane

# Session
tmux new -s sessionname	new session
tmux a -t sessionname attach session
tmux kill-session -t sessionname kill session
tmux ls	list all session
```
## Cheatsheets
- tmux
- vim
- create a github repository
- docker
- scp
- ffmpeg
- awk
- conda

## Terminal Shortcut
Firstly, make your command executable by using chmod
```bash
chmod u+x frgt.sh
```
Then make an alias in your .bashrc to make it persistent:

```bash
alias frgt='/path/to/frgt.sh'
```

```bash
frgt docker

# docker pull image_namem                                       Download an image, and all its parents, from the registry.
# docker start container_name                                   Start a container
# docker stop container_name                                    Stop a container
# docker kill $(docker ps -q)
```

## Adding Cheatsheets
You can provide your custom or general cheatsheet.
- Create a gist
- Go to [frgt.dev/add](https://www.frgt.dev/add)
- Done!
### Cheatsheet Template
The best way the format of cheatsheets are seperated with pipe symbol.
```bash
docker start container_name|Start a container
docker stop container_name|Stop a container
docker build image_name .|Build an image
docker image ls|List all images
docker ps|Manage containers using ps/kill
```
frgt.dev can properly display the data if is seperated with pipes but otherwise it will worked anyway.

## To-Do's
Feel free to contribute.


## License

[MIT](https://choosealicense.com/licenses/mit/)
