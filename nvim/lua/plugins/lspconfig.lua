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

return {
	{
		"neovim/nvim-lspconfig",
		opts = {
			servers = {
				pyright = {},
				rust_analyzer = rust_analyzer,
				clangd = {},
				lua_ls = lua_ls
			}
		},
		config = function(_, opts)
			local lspconfig = require('lspconfig')
			for server, config in pairs(opts.servers) do
				config.capabilities = require('blink.cmp')
					.get_lsp_capabilities(config.capabilities)
				lspconfig[server].setup(config)
			end
		end,
	},
}
