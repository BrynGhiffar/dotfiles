-- ~/.config/hypr/hyprland.lua
--
-- Clean migration of the old hyprlang config (arc_hyprland.conf) to the
-- Hyprland Lua configuration format (Hyprland 0.55+).
--
-- Reference: https://wiki.hypr.land/configuring/

--------------------------------------------------------------------------------
-- Programs (old $terminal / $fileManager / $menu variables)
--------------------------------------------------------------------------------

local terminal    = "ghostty"
local fileManager = "launch_kitty explorer yazi"
local menu        = "launch_kitty fzfapp fzfapp"

local mainMod = "SUPER" -- $mainMod

--------------------------------------------------------------------------------
-- Monitors
--------------------------------------------------------------------------------
-- https://wiki.hypr.land/configuring/core/monitors/

hl.monitor({
    output   = "DP-3",
    mode     = "1920x1080@180",
    position = "0x0",
    scale    = 1,
})

hl.monitor({
    output   = "HDMI-A-1",
    mode     = "1920x1080@60",
    position = "1920x0",
    scale    = 1,
})

--------------------------------------------------------------------------------
-- Autostart (replaces the old "exec-once" lines)
--------------------------------------------------------------------------------
-- https://wiki.hypr.land/configuring/core/autostart/
-- "hyprland.start" fires once at Hyprland startup, not on every config reload,
-- so these daemons will not be spawned again when the config is re-read.

hl.on("hyprland.start", function()
    -- This is for screen sharing.
    hl.exec_cmd("dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP")
    hl.exec_cmd("nohup wpdm >/dev/null 2>&1 &")
    hl.exec_cmd("barbar")
    hl.exec_cmd("/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1")
    hl.exec_cmd('eval "$(ssh-agent -s)"')
    -- NOTE: this spawns an agent on a socket of its own choosing, while
    -- SSH_AUTH_SOCK below points at $XDG_RUNTIME_DIR/ssh-agent.socket.
    -- Kept as-is from the old config.
end)

--------------------------------------------------------------------------------
-- Environment variables
--------------------------------------------------------------------------------
-- https://wiki.hypr.land/configuring/core/environment-variables/

hl.env("XCURSOR_SIZE", "24")
hl.env("SSH_AUTH_SOCK", (os.getenv("XDG_RUNTIME_DIR") or "") .. "/ssh-agent.socket")

--------------------------------------------------------------------------------
-- input {}  (old "input" category)
--------------------------------------------------------------------------------
-- https://wiki.hypr.land/configuring/core/config-options/

hl.config({
    input = {
        kb_layout  = "us",
        kb_variant = "",
        kb_model   = "",
        kb_options = "",
        kb_rules   = "",

        follow_mouse = 1,

        touchpad = {
            natural_scroll = false,
        },

        sensitivity = 0, -- -1.0 - 1.0, 0 means no modification.
    },
})

--------------------------------------------------------------------------------
-- general {}  (old "general" category)
--------------------------------------------------------------------------------

hl.config({
    general = {
        gaps_in = 5,
        -- old: "gaps_out = 0, 5, 5, 5" (top, right, bottom, left)
        gaps_out = { top = 0, right = 5, bottom = 5, left = 5 },

        border_size = 1,

        col = {
            active_border   = { colors = { "rgba(33ccffee)", "rgba(00ff99ee)" }, angle = 45 },
            inactive_border = "rgba(595959aa)",
        },

        layout = "dwindle",

        -- Please see https://wiki.hypr.land/configuring/extra/tearing/ before you turn this on
        allow_tearing = false,
    },
})

--------------------------------------------------------------------------------
-- decoration {}  (old "decoration" category)
--------------------------------------------------------------------------------

hl.config({
    decoration = {
        rounding = 10,

        blur = {
			variant = "kawase",
            enabled = true,
            size    = 5,
            passes  = 2,
        },

		shadow = {
			enabled = true,
		}

        -- The old config had drop_shadow / shadow_range / col.shadow commented
        -- out, so shadow settings stay at their defaults here too.
    },
})

--------------------------------------------------------------------------------
-- animations {}  (old "animations" category)
--------------------------------------------------------------------------------

hl.config({
    animations = {
        enabled = true,
    },
})

--------------------------------------------------------------------------------
-- dwindle {}  (old "dwindle" category)
--------------------------------------------------------------------------------
-- https://wiki.hypr.land/configuring/layouts/dwindle-layout/

hl.config({
    dwindle = {
        -- old: "# pseudotile = yes" -- dwindle:pseudotile was removed in 0.55 (it did nothing)
        preserve_split = true, -- you probably want this
    },
})

-- The old config's "master {}" and "gestures {}" blocks contained only
-- commented-out options, so they are left at their defaults.

--------------------------------------------------------------------------------
-- misc {}  (old "misc" category)
--------------------------------------------------------------------------------

hl.config({
    misc = {
        force_default_wallpaper = 0, -- Set to 0 or 1 to disable the anime mascot wallpapers
        disable_hyprland_logo   = true,
        mouse_move_enables_dpms = true,
        key_press_enables_dpms  = true,
    },
})

--------------------------------------------------------------------------------
-- Curves & animations
--------------------------------------------------------------------------------
-- https://wiki.hypr.land/configuring/core/animations/

-- Old: "bezier = myBezier, 0.05, 0.9, 0.1, 1.0" (the two middle control points).
-- In the old config only a commented-out line ever referenced it; it is kept
-- here so it is available if you want it.
hl.curve("myBezier", { type = "bezier", points = { { 0.05, 0.9 }, { 0.1, 1.0 } } })

-- Old "animation = <leaf>, 1, <speed>, <curve>, <style>" lines:
hl.animation({ leaf = "windows",     enabled = true, speed = 8,  bezier = "default", style = "popin 80%" })
hl.animation({ leaf = "windowsOut", enabled = true, speed = 7,  bezier = "default", style = "popin 80%" })
hl.animation({ leaf = "border",     enabled = true, speed = 10, bezier = "default" })
hl.animation({ leaf = "borderangle", enabled = true, speed = 8,  bezier = "default" })
hl.animation({ leaf = "fade",       enabled = true, speed = 7,  bezier = "default" })
hl.animation({ leaf = "workspaces", enabled = true, speed = 8,  bezier = "default", style = "fade" })

--------------------------------------------------------------------------------
-- Window rules (old "windowrule" lines)
--------------------------------------------------------------------------------
-- https://wiki.hypr.land/configuring/core/rules/window-rules/

hl.window_rule({
    match       = { class = "fzfwallpaper" },
    pin         = true,
    stay_focused = true,
    float       = true,
    center      = true,
    size        = { 1200, 400 },
})

hl.layer_rule({
	match = { namespace = "barbar" },
	blur = true,
})

hl.window_rule({
    match       = { class = "explorer" },
    pin         = true,
    stay_focused = true,
    float       = true,
    center      = true,
    size        = { 1200, 600 },
})

hl.window_rule({
    match       = { class = "fzfapp" },
    pin         = true,
    stay_focused = true,
    float       = true,
    center      = true,
    size        = { 400, 300 },
})

hl.window_rule({
    match = { title = "wgpu_cube" },
    pin   = true,
    float = true,
    move  = { 1480, 40 },
    size  = { 400, 400 },
})

--------------------------------------------------------------------------------
-- Workspace rules (old "workspace = N, monitor:X, persistent:true" lines)
--------------------------------------------------------------------------------
-- https://wiki.hypr.land/configuring/core/rules/workspace-rules/

for i = 1, 3 do
    hl.workspace_rule({ workspace = tostring(i), monitor = "DP-3", persistent = true })
end

for i = 4, 6 do
    hl.workspace_rule({ workspace = tostring(i), monitor = "HDMI-A-1", persistent = true })
end

--------------------------------------------------------------------------------
-- Key bindings
--------------------------------------------------------------------------------
-- https://wiki.hypr.land/configuring/core/binds/
-- Old syntax: bind = MODS, KEY, dispatcher, args
-- New syntax: hl.bind("MODS + KEY", dispatcher, { flags })

-- --- Key Bindings ---
hl.bind(mainMod .. " + RETURN", hl.dsp.exec_cmd(terminal))
hl.bind(mainMod .. " + W", hl.dsp.window.close())
-- old: "# bind = $mainMod, M, exit, "
-- hl.bind(mainMod .. " + M", hl.dsp.exit())
hl.bind(mainMod .. " + M", hl.dsp.exec_cmd("launch_kitty fzfwallpaper hypr_wallpaper"))
hl.bind(mainMod .. " + E", hl.dsp.exec_cmd(fileManager))
hl.bind(mainMod .. " + T", hl.dsp.window.float({ action = "toggle" }))
hl.bind(mainMod .. " + SPACE", hl.dsp.exec_cmd(menu))

-- The old config used the undefined "$mainMode" variable on the binds below
-- (hyprlang substitutes an empty string, so they were bound without SUPER).
-- They are bound to mainMod here, as clearly intended.
hl.bind(mainMod .. " + F",         hl.dsp.window.fullscreen({ mode = "maximized" }))            -- old: fullscreen, 1
hl.bind(mainMod .. " + SHIFT + F", hl.dsp.window.fullscreen_state({ internal = 2, client = 2 })) -- old: fullscreen, 2
hl.bind(mainMod .. " + Y", hl.dsp.exec_cmd('notify-send "Date: $(date)" --expire-time=2500'))

-- old "binde" (repeat while held) => { repeating = true }
hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("wpctl set-volume -l 1.4 @DEFAULT_AUDIO_SINK@ 7%+"), { repeating = true })
hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("wpctl set-volume -l 1.4 @DEFAULT_AUDIO_SINK@ 7%-"), { repeating = true })
hl.bind("XF86AudioMute", hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"))

-- old "execr" (raw exec) => plain exec_cmd: Lua strings are verbatim, and
-- exec_cmd runs the command through the shell, so $(...), | and && all work.
hl.bind(mainMod .. " + CTRL + S", hl.dsp.exec_cmd('grim -g "$(select-region)" - | wl-copy && notify-send "Screenshot" "Copied to clipboard"'))
hl.bind(mainMod .. " + SHIFT + C", hl.dsp.exec_cmd("hyprpicker -a"))
hl.bind(mainMod .. " + Q", hl.dsp.exec_cmd("/home/bryn/dotfiles/wlogout/scripts/run.sh"))
-- old: "# bind = $mainMod, P, pseudo, # dwindle"
-- hl.bind(mainMod .. " + P", hl.dsp.window.pseudo())       -- dwindle
-- old: "# bind = $mainMod, J, togglesplit, # dwindle"
-- hl.bind(mainMod .. " + J", hl.dsp.layout("togglesplit")) -- dwindle (J currently moves focus down)

-- Move focus with mainMod + hjkl (old "movefocus" dispatcher)
hl.bind(mainMod .. " + h", hl.dsp.focus({ direction = "left" }))
hl.bind(mainMod .. " + l", hl.dsp.focus({ direction = "right" }))
hl.bind(mainMod .. " + k", hl.dsp.focus({ direction = "up" }))
hl.bind(mainMod .. " + j", hl.dsp.focus({ direction = "down" }))

-- Move the current workspace to a monitor (old "movecurrentworkspacetomonitor")
-- hl.bind("ALT + 1", hl.dsp.workspace.move({ monitor = "HDMI-A-1" }))
-- hl.bind("ALT + 2", hl.dsp.workspace.move({ monitor = "DP-3" }))

-- Switch workspaces with mainMod + [1-3], [a/s/d -> 4-6], [7-9], [0 -> 10]
-- Move the active window to a workspace with mainMod + SHIFT + the same keys
local ws_keys = {
    { key = "1", ws = 1 },
    { key = "2", ws = 2 },
    { key = "3", ws = 3 },
    { key = "a", ws = 4 },
    { key = "s", ws = 5 },
    { key = "d", ws = 6 },
    { key = "7", ws = 7 },
    { key = "8", ws = 8 },
    { key = "9", ws = 9 },
    { key = "0", ws = 10 },
}

for _, entry in ipairs(ws_keys) do
    hl.bind(mainMod .. " + " .. entry.key,          hl.dsp.focus({ workspace = entry.ws }))
    hl.bind(mainMod .. " + SHIFT + " .. entry.key, hl.dsp.window.move({ workspace = entry.ws }))
end

-- Example special workspace (scratchpad), translated from the old commented
-- binds. Note mainMod + S / SHIFT + S collide with s -> workspace 5, which is
-- why they stay commented here too:
-- hl.bind(mainMod .. " + SHIFT + S", hl.dsp.window.move({ workspace = "special:magic" }))
-- hl.bind(mainMod .. " + S", hl.dsp.workspace.toggle_special("magic"))

-- Scroll through existing workspaces with mainMod + scroll
hl.bind(mainMod .. " + mouse_down", hl.dsp.focus({ workspace = "e+1" }))
hl.bind(mainMod .. " + mouse_up",   hl.dsp.focus({ workspace = "e-1" }))

-- Move/resize windows with mainMod + LMB/RMB and dragging (old "bindm")
hl.bind(mainMod .. " + mouse:272", hl.dsp.window.drag(),   { mouse = true })
hl.bind(mainMod .. " + mouse:273", hl.dsp.window.resize(), { mouse = true })
