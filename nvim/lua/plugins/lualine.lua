return {
	'nvim-lualine/lualine.nvim',
	requires = { 'nvim-tree/nvim-web-devicons', opt = true },
	config = function()
		local theme = require("catppuccin.utils.lualine")("mocha")
		require("lualine").setup({
			options = { theme },
			extensions = { "nvim-tree" }
		})
	end
}
