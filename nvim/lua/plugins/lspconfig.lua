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

local tailwindcss = {
  -- exclude a filetype from the default_config
  filetypes_exclude = { "markdown" },
  -- add additional filetypes to the default_config
  filetypes_include = {},
  -- to fully override the default_config, change the below
  -- filetypes = {}
}

return {
	{
		'nvim-java/nvim-java',
		config = false,
		dependencies = {
			{
				"neovim/nvim-lspconfig",
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
				nushell = {},
				tailwindcss = tailwindcss,
				gopls = {
					analyses = {
						unusedparams = true,
					},
					staticcheck = true,
					gofumpt = true,
				}
			},
			setup = {
				jdtls = function()
					require("java").setup({})
				end,
				tailwindcss = function(_, opts)
				  opts.filetypes = opts.filetypes or {}

				  -- Add default filetypes
				  vim.list_extend(opts.filetypes, vim.lsp.config.tailwindcss.filetypes)

				  -- Remove excluded filetypes
				  --- @param ft string
				  opts.filetypes = vim.tbl_filter(function(ft)
					return not vim.tbl_contains(opts.filetypes_exclude or {}, ft)
				  end, opts.filetypes)

				  -- Additional settings for Phoenix projects
				  opts.settings = {
					tailwindCSS = {
					  includeLanguages = {
						elixir = "html-eex",
						eelixir = "html-eex",
						heex = "html-eex",
					  },
					},
				  }

				  -- Add additional filetypes
				  vim.list_extend(opts.filetypes, opts.filetypes_include or {})
				end,
			}
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
