#!/usr/bin/env bash

##!/bin/bash

#function run {
#  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
#  then
#    $@&
#  fi
#}

#change your keyboard if you need it
#setxkbmap -option caps:f13,shift:both_capslock
setxkbmap -layout de

keybLayout=$(setxkbmap -v | awk -F "+" '/symbols/ {print $2}')

#if [ $keybLayout = "be" ]; then
#  cp $HOME/.config/qtile/config-azerty.py $HOME/.config/qtile/config.py
#fi

#Some ways to set your wallpaper besides variety or nitrogen
#feh --bg-fill /usr/share/backgrounds/archlinux/arch-wallpaper.jpg &
feh --bg-fill  /home/jens/Bilder/wallpaper/wallhaven-e7jj6r.jpg &

#start the conky to learn the shortcuts
#(conky -c $HOME/.config/qtile/scripts/system-overview) &
conky -c /home/jens/.config/qtile/scripts/system-overview &

#start sxhkd to replace Qtile native key-bindings
#run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &

#starting utility applications at boot time
#run variety &

#session manager used to automatically start a set of applications and set up a working desktop environment
lxsession &

nm-applet &s
pamac-tray &
xfce4-power-manager &
blueman-applet &
numlockx on &

# Assign F14 to Caps_Lock
xmodmap /home/jens/.config/qtile/scripts/xmodmap-winkljaro &

#blueberry-tray &
picom --config $HOME/.config/qtile/scripts/picom.conf &

#Lightweight replacement for the notification-daemons
#dunst &

# allow unprivileged processes to speak to privileged processes
# /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &

#starting user applications at boot time
#volumeicon &

ksnip &
solaar -w hide &
#nitrogen --restore &
#run caffeine -a &
#run firefox &
#run thunar &
#run dropbox &
#run insync start &
#run spotify &
telegram-desktop &
/home/jens/Applications/Espanso-X11.AppImage &

