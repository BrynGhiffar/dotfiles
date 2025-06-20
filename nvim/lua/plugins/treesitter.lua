return {
  "nvim-treesitter/nvim-treesitter",
  build = ":TSUpdate", -- This will run :TSUpdate after installation
  config = function()
    require("nvim-treesitter.configs").setup {
      highlight = {
        enable = true, -- Enable syntax highlighting
      },
      -- You can add other Tree-sitter features here if you like,
      -- such as indent, incremental_selection, etc.
      -- indent = { enable = true },
	  ensure_installed = { "nu", "java" }
    }
  end,
}
