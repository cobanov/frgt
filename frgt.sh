#!/bin/bash
# curl 
if [ -z $1 ]

then 
    echo "type something for example 'tmux' or 'vim'"
else 
    curl -L frgt.dev/$1 
fi
