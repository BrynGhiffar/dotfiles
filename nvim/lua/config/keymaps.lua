local api = require("nvim-tree.api")
local tscope = require('telescope.builtin')

local opts = { noremap = true, silent = true }
vim.keymap.set("n", "<C-f>", function()
	if vim.fn.bufname():match 'NvimTree_' then
		api.tree.toggle()
	else
		api.tree.find_file({ open = true, focus = true })
	end
end)
vim.keymap.set("n", 'H', '<C-o>')
vim.keymap.set("n", 'L', '<C-i>')
vim.keymap.set("n", "<leader>ff", tscope.find_files, { desc = 'Telescope find files' })
vim.keymap.set("n", "<leader>fg", tscope.live_grep, { desc = 'Telescope live grep'})
vim.keymap.set("n", "<leader>fb", tscope.buffers, { desc = 'Telescope buffers'})
vim.keymap.set("n", "<leader>fh", tscope.live_grep, { desc = 'Telescope help tags'})
vim.keymap.set("n", "<leader>fd", tscope.diagnostics, { desc = 'Telescope diagnostics'})
vim.keymap.set("n", "<leader>fr", tscope.lsp_references, { desc = 'Telescope help tags'})
vim.keymap.set("n", "<leader>nt", function() vim.cmd("tab split")end)
vim.keymap.set("n", "gD", function() vim.lsp.buf.declaration() end, opts)
vim.keymap.set("n", "gd", tscope.lsp_definitions, opts)
vim.keymap.set('t', '<Esc>', '<C-\\><C-n>', { noremap = true, silent = true })
vim.keymap.set('t', '<C-[>', '<C-\\><C-n>', { noremap = true, silent = true })

-- Lua code for your init.lu
vim.keymap.set("n", "<leader>st", function()
	vim.cmd.split()
	vim.cmd.wincmd("J")
	vim.cmd("term nu")
	vim.api.nvim_win_set_height(0, 15)
	vim.api.nvim_feedkeys(
		vim.api.nvim_replace_termcodes("i", true, true, true),
		'n', -- Interpret the key from Normal mode
		true -- Do not respect mappings for 'i' (ensure it's a raw mode switch)
  )
end)
