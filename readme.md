![frgt](https://github.com/cobanov/frgt/blob/main/frgt.png?raw=true)

# frgt.dev

[frgt.dev](https://www.frgt.dev) is a terminal based cheatsheet helper for developers

## Usage
Whenever you forget something just use this.
```bash
curl frgt.dev/tmux
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

