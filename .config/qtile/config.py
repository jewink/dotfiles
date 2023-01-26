# jeWink QTile config
#   _     _ _ _ _     _   
#  |_|___| | | |_|___| |_ 
#  | | -_| | | | |   | '_|
# _| |___|_____|_|_|_|_,_|
#|___|                    

import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.command import lazy
from libqtile.widget import Spacer
from libqtile.widget.base import _TextBox

#from qtile_extras import widget
#from qtile_extras.widget.decorations import RectDecoration
#from qtile_extras import widget

# mod4 or mod = super key
# map to which keys on your system by running the xmodmap
mod = "mod4"
mod1 = "alt"
mod2 = "control"

home = os.path.expanduser('~')
myTerm = "xfce4-terminal"
myBrowser = "brave"


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

######################## KEYS ######################
keys = [
# Migrated from sxhkd and essentials

    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod], "b", lazy.spawn(myBrowser)),
    Key([mod], "F12", lazy.spawn("rofi -show drun -show-icons")),
    Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#3B4252' -nf '#5E81AC' -sb '#81A1C1' -sf '#EBCB8B' -p 'Run: '")),
    Key([mod], "v", lazy.spawn("pavucontrol")),
    Key([mod], "Escape", lazy.spawn("xkill")),
    Key([mod], "x", lazy.spawn("archlinux-logout")),
    Key([mod], "F6", lazy.spawn("vlc")),
    Key([mod], "F2", lazy.spawn("xfce4-appfinder --collapsed")),
    Key([mod], "F3", lazy.spawn("xfce4-appfinder")),
    
# SUPER + FUNCTION KEYS

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),

# SUPER + SHIFT/CONTROL KEYS

    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "Return", lazy.spawn("thunar")),
    Key([mod, "control"], "Return", lazy.spawn("alacritty")),
    Key([mod, "shift"], "r", lazy.reload_config()),
    Key([mod, "shift"], "m", lazy.layout.maximize()),

# CONTROL + SHIFT KEYS
   
    Key([mod2, "shift"], "r", lazy.restart()),
    Key([mod2, "shift"], "Escape", lazy.spawn("xfce4-taskmanager")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),
    
# FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating())
    ]

def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)

keys.extend([
    # MOVE WINDOW TO NEXT SCREEN
    Key([mod,"shift"], "Right", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod,"shift"], "Left", lazy.function(window_to_previous_screen, switch_screen=True)),
])

######################## GROUPS ######################
# Additional Icons       
groups = [
    Group('1', position=0, label='1:', layout='monadtall', matches=[Match(wm_class='brave-browser')]),
    Group('2', position=1, label='2:', layout='monadtall'),# matches=[Match(wm_class='smplayer')]),
    Group('3', position=2, label='3:', layout='monadtall'),
    Group('4', position=3, label='4:', layout='monadtall'),# matches=[Match(wm_class='VirtualBox Machine')]),
    Group('5', position=4, label='5:', layout='monadtall', matches=[Match(wm_class='telegram-desktop')]),
    Group('6', position=5, label='6:', layout='monadtall'),# matches=[Match(title='updates'), Match(wm_class='VirtualBox Manager')]),
    Group('7', position=6, label='7:', layout='monadtall'),# 
    Group('8', position=7, label='8:', layout='monadtall'),# 
    Group('9', position=8, label='9:', layout='monadtall'),# 
    Group('0', position=9, label='0:', layout='monadtall') # 
]

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
     #  Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen())
    ])

######################## LAYOUT ######################
def init_layout_theme():
    return {"margin":5,
            "border_width":2,
            "border_focus": "#5e81ac",
            "border_normal": "#4c566a"
            }

layout_theme = init_layout_theme()

layouts = [
    #layout.MonadTall(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    layout.MonadTall(**layout_theme),
    #layout.MonadWide(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
    layout.TreeTab(**layout_theme),
    layout.Columns(**layout_theme)
]

############ COLORS ##########
colors =[["#2F343F", "#2F343F"], # color 0 (Grau)
         ["#2F343F", "#2F343F"], # color 1 (Grau)
         ["#c0c5ce", "#c0c5ce"], # color 2 (Hellgrau)
         ["#81A1C1", "#81A1C1"], # color 3 (NORD Blau)
         ["#3384d0", "#3384d0"], # color 4 (Hellblau)
         ["D8DEE9", "#D8DEE9"], # color 5 (NORD Grau)
         ["#cd1f3f", "#cd1f3f"], # color 6 (Rot)
         ["#62FF00", "#62FF00"], # color 7 (Hellgrün)
         ["#6790eb", "#6790eb"], # color 8 (Hellblau)
         ["#a9a9a9", "#a9a9a9"]] # color 9 (Rotgrau)

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

######################## WIDGETS ######################

widget_defaults = dict(
    font="Noto Sans",
    fontsize = 12,
    padding = 2,
)

def init_widgets_list():
    widgets_list = [
                widget.GroupBox(font="FontAwesome",
                        fontsize = 13,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 4,
                        padding_x = 6,
                        borderwidth = 0,
                        disable_drag = True,
                        active = colors[9],
                        inactive = colors[5],
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = colors[8],
                        foreground = colors[2],
                        background = colors[1]
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[3],
                        background = colors[1]
                        ),
                widget.CurrentLayout(
                        font = "Noto Sans Bold",
                        foreground = colors[3],
                        background = colors[1]
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[3],
                        background = colors[1]
                        ),
                widget.WindowName(font="Noto Sans",
                        fontsize = 12,
                        foreground = colors[5],
                        background = colors[1],
                        ),
               # widget.Net(
               #          font="Noto Sans",
               #          fontsize=12,
               #          interface="enp0s31f6",
               #          foreground=colors[2],
               #          background=colors[1],
               #          padding = 0,
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.NetGraph(
               #          font="Noto Sans",
               #          fontsize=12,
               #          bandwidth="down",
               #          interface="auto",
               #          fill_color = colors[8],
               #          foreground=colors[2],
               #          background=colors[1],
               #          graph_color = colors[8],
               #          border_color = colors[2],
               #          padding = 0,
               #          border_width = 1,
               #          line_width = 1,
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # # do not activate in Virtualbox - will break qtile
               # widget.Image(
               #        filename = "~/.config/qtile/icons/python-white.png",
               #        scale = True,
               #        mouse_callbacks = {'Button1': lazy.spawn(myTerm)}
               #        ),
                widget.TextBox(
                         font="FontAwesome",
                         text="  ",
                         foreground=colors[3],
                         background=colors[1],
                         padding = 0,
                         fontsize=16
                         ),
                widget.ThermalSensor(
                         foreground = colors[5],
                         foreground_alert = colors[6],
                         background = colors[1],
                         metric = True,
                         tag_sensor = "Package id 0",
                         padding = 3,
                         threshold = 80
                         ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[3],
                        background = colors[1]
                        ), 
               # # battery option 1  ArcoLinux Horizontal icons do not forget to import arcobattery at the top
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # arcobattery.BatteryIcon(
               #          padding=0,
               #          scale=0.7,
               #          y_poss=2,
               #          theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
               #          update_interval = 5,
               #          background = colors[1]
               #          ),
               # # battery option 2  from Qtile
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.Battery(
               #          font="Noto Sans",
               #          update_interval = 10,
               #          fontsize = 12,
               #          foreground = colors[5],
               #          background = colors[1],
	           #          ),
                widget.TextBox(
                         font="FontAwesome",
                         text="  ",
                         foreground=colors[3],
                         background=colors[1],
                         padding = 0,
                         fontsize=16
                         ),
                widget.CPUGraph(
                         border_color = colors[2],
                         fill_color = colors[8],
                         graph_color = colors[8],
                         background=colors[1],
                         border_width = 1,
                         line_width = 1,
                         core = "all",
                         type = "box"
                         ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[3],
                        background = colors[1]
                        ), 
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.TextBox(
               #          font="FontAwesome",
               #          text="  ",
               #          foreground=colors[4],
               #          background=colors[1],
               #          padding = 0,
               #          fontsize=16
               #          ),
                widget.TextBox(
                        font="NotoEmoji Nerd Font",
                        text="",
                        foreground=colors[3],
                        background=colors[1],
                        padding = 2,
                        fontsize=16
                        ),
                widget.Memory(
                        font="Noto Sans",
                        measure_mem='G',
                        format = '{MemUsed:.2f}GB / {MemTotal:.2f}GB',
                        mouse_callbacks = {'Button1': lazy.spawn(myTerm + ' -e htop')},
                        update_interval = 1,
                        fontsize = 12,
                        foreground = colors[5],
                        background = colors[1],
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[3],
                        background = colors[1]
                        ), 
                widget.TextBox(
#                        font="FontAwesome",
#                        text="  ",
                        font="NotoEmoji Nerd Font",
                        text="",
                        foreground=colors[3],
                        background=colors[1],
                        padding = 4,
                        fontsize=16
                        ),
                widget.Net(
                       interface = "enp0s31f6",
                       format = '↓{down} ↑{up}',
                       foreground = colors[5],
                       background = colors[1],
                       use_bits = False,
                       update_interval = 2,
                       padding = 0
                       ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[3],
                        background = colors[1]
                        ),                
                widget.TextBox(
                        font="Hack Nerd Font",
                        text=" ",
                        mouse_callbacks = {'Button1': lazy.spawn('pavucontrol')},
                        foreground=colors[3],
                        background=colors[1],
                        padding = 0,
                        fontsize=16
                        ),
                widget.Volume(
                       foreground = colors[5],
                       background = colors[1],
                       fmt = '{}',
                       padding = 0
                       ),
#                extras.widget.ALSAWidget(
#                       device = 'Master',
#                       mode = 'both',
#                       step = 5,
#                       foreground = colors[5],
#                       background = colors[1],
#                       padding = 0
#                       ),                
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[3],
                        background = colors[1]
                        ),
                widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[3],
                        background=colors[1],
                        padding = 0,
                        fontsize=16
                        ),
                widget.Clock(
                        foreground = colors[5],
                        background = colors[1],
                        fontsize = 12,
                        format="%d.%m.%Y - %H:%M",
                        mouse_callbacks = {'Button1': lazy.spawn('gsimplecal')}
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[3],
                        background = colors[1]
                        ),
                widget.Systray(
                        background=colors[1],
                        icon_size=20,
                        padding = 4
                        ),
                widget.QuickExit(
                        font = "FontAwesome",
                        background = colors[1],
                        foreground = colors[3],
                        countdown_start = 9,
                        countdown_format = '{}',
                        default_text = '',
                        padding = 6
                        )
              ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

######################## SCREENS ######################
widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26, opacity=0.8)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26, opacity=0.8))]
screens = init_screens()


######################## MOUSE CONFIGURATION ########################
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []

main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

######################## DEFINE FLOATING WINDOWS ########################
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='Arcolinux-welcome-app.py'),
    Match(wm_class='Arcolinux-calamares-tool.py'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='archlinux-logout'),
    Match(wm_class='solaar'),
    Match(wm_class='copyq'),
    Match(wm_class='pavucontrol'),
    Match(wm_class='telegram-desktop'),
    Match(wm_class='xfce4-appfinder'),
    Match(wm_class='pcloud'),
    Match(wm_class='virt-viewer'),
    Match(wm_class='ksnip')
],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
