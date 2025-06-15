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
				signcolumn = 'yes'
			}
		}
	end,
}
