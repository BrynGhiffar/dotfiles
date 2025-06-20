return {
	"nvim-tree/nvim-tree.lua",
	version = "*",
	lazy = false,
	dependencies = {
		"nvim-tree/nvim-web-devicons",
	},
	config = function()
		require("nvim-tree").setup {
			git = { ignore = false },
			filters = { dotfiles = false, },
			live_filter = {
				always_show_folders = false,
			},
			diagnostics = {
				enable = true,
				icons = {
					hint = "",
					info = "",
					warning = "",
					error = "",
				},
				show_on_dirs = true,
			},
			view = {
				centralize_selection = true,
				signcolumn = 'yes',
				width = 30,
			}
		}
	end,
}
