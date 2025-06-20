local rust_analyzer = {
	settings = {
		['rust-analyzer'] = {
			check = { command = 'clippy' }
		}
	}
}

local lua_ls = {
	settings = {
		Lua = {
			diagnostics = {
				globals = { "vim" }
			}
		}
	}
}

local ts_ls = { }

return {
	{
		'nvim-java/nvim-java',
		config = false,
		dependencies = {
			{
				"neovim/nvim-lspconfig",
				setup = {
					jdtls = function()
						require("java").setup({})
					end
				}
			}
		}
	},
	{
		"neovim/nvim-lspconfig",
		opts = {
			servers = {
				pyright = {},
				rust_analyzer = rust_analyzer,
				clangd = {},
				ts_ls = ts_ls,
				lua_ls = lua_ls,
				jdtls = {},
				nushell = {}
			},
		},
		config = function(_, opts)
			vim.diagnostic.config({
			  signs = {
				text = {
				  [vim.diagnostic.severity.ERROR] = '✘',
				  [vim.diagnostic.severity.WARN] = '▲',
				  [vim.diagnostic.severity.HINT] = '⚑',
				  [vim.diagnostic.severity.INFO] = '»',
				},
			  },
			})
			-- DiagnosticVirtualTextError xxx cterm=italic gui=italic guifg=#f38ba9
			vim.api.nvim_set_hl(0, 'DiagnosticVirtualTextError', { bg = "#ff0000"})
			local lspconfig = require('lspconfig')
			for server, config in pairs(opts.servers) do
				config.capabilities = require('blink.cmp')
					.get_lsp_capabilities(config.capabilities)
				lspconfig[server].setup(config)
			end
		end,
	},
}
