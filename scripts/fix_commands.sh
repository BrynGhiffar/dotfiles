#!/bin/sh

# How to fix broken archlinux setup due to unable to mount /boot. You can check the error in journalctl -xb

# Credits to post by Shashank Shekhar: https://medium.com/@correspond.shashank/broke-my-arch-linux-again-heres-how-i-fixed-it-5db2db040b14

# 1. Mount root partition
mount /dev/sdc3 /mnt

# 2. Chroot into /mnt
arch-chroot /mnt

# 3. Delete /boot 
rm -rf /boot/*

# 4. install linux
pacman -S linux

# 5. Mount boot partition
mount /dev/sdc1 /boot

# 6. Reinstall bootloader
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB

# 7. Create the grub configuration
grub-mkconfig -o /boot/grub/grub.cfg

# 8. Create the linux image
mkinitcpio -p linux

# 9. Regenerate fstab (not necessary)
genfstab -U -p /

# 10. Exit from chroot
exit

# 11. Unmount everything (Important!)
umount -a

# 12. Reboot system
reboot

# Possible solution to try from gemini
# 1. Create new initramfs 
mkinitcpio -P

# 2. create boot configuration
grub-mkconfig -o /boot/grub/grub.cfg

# 3. Exit from chroot
exit

# 4. Unmount everything (Important!)
umount -a

# 5. Reboot system
reboot
