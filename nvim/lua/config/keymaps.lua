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
vim.keymap.set("n", "gD", function() vim.lsp.buf.declaration() end, opts)
vim.keymap.set("n", "gd", function() vim.lsp.buf.definition() end, opts)

