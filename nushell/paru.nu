def pkgs [] {
  ^paru -Qe
    | lines
    | parse "{package} {version}"
}

#
# - Interactively search for and install a package:
#   paru package_name_or_search_term
#
# - Synchronize and update all packages:
#   paru
#
# - Upgrade AUR packages:
#   paru -Sua
#
# - List manually installed packages:
#   paru -Qqm
#
# - Remove an installed package, its configuration files, and dependencies:
#   paru -Rns package
#
# - Get information about a package:
#   paru -Si package
#
# - Download PKGBUILD and other package source files from the AUR or ABS:
#   paru --getpkgbuild package
#
# - Display the PKGBUILD file of a package:
#   paru -Gp package
