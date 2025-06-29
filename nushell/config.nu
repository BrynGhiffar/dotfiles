# config.nu
#
# Installed by:
# version = "0.104.1"
#
# This file is used to override default Nushell settings, define
# (or import) custom commands, or run any other startup tasks.
# See https://www.nushell.sh/book/configuration.html
#
# This file is loaded after env.nu and before login.nu
#
# You can open this file in your default editor using:
# config nu
#
# See `help config nu` for more options
#
# You can remove these comments if you want or leave
# them for future reference.

# let additional_paths = ["/home/bryn/.local/scripts"]

load-env {
	CC: "/usr/bin/clang",
	CXX: "/usr/bin/clang++",
	GPG_TTY: (tty)
	PATH: ($env.PATH | append [
		"/home/bryn/.local/scripts"
	])
}

keychain --eval --quiet id_ed25519
	| lines
	| where not ($it | is-empty)
	| parse "{k}={v}; export {k2};"
	| select k v
	| transpose --header-row
	| into record
	| load-env

$env.config = {
	show_banner: false,
	buffer_editor: "nvim",
}

alias z = zellij attach
alias nv = nvim
alias vim = nvim
alias disk-check = sudo ncdu / --exclude /mnt

def ll [] {
	ls -la | sort-by name
}

def --env y [...args] {
	let tmp = (mktemp -t "yazi-cwd.XXXXXX")
	yazi ...$args --cwd-file $tmp
	let cwd = (open $tmp)
	if $cwd != "" and $cwd != $env.PWD {
		cd $cwd
	}
	rm -fp $tmp
}

def --env record-screen [screen: string] {
	use std/log
	log debug "Start recording"
	let size = match $screen {
		"1" => "1920x1080",
		"2" => "1920x1080",
		"full" => "3840x1080",
		_ => {
			log error "Screen must be '1', '2', or 'full'"
			return;
		}
	}
	let start_position = match $screen {
		"1" => "0,0",
		"2" => "1920,0",
		"full" => "0,0",
		_ => {
			log error "Screen must be '1', '2', or 'full'"
			return;
		}
	}
	let filename = $"((^date +"%H_%M_%S-%d_%m_%Y") ++ ".mp4")";
	let filepath = "/home/bryn/Downloads/";
	let output = $filepath ++ $filename
	let input = $"(":1+" ++ $start_position)"
	let res = (ffmpeg 
		-video_size $size 
		-framerate 60 
		-f x11grab 
		-i $input $output 
		-hide_banner -loglevel warning
		-y) | complete
	log info "Finished recording..."
	let exit_code = $res | get exit_code
	$res
}

mkdir ($nu.data-dir | path join "vendor/autoload")
starship init nu | save -f ($nu.data-dir | path join "vendor/autoload/starship.nu")
