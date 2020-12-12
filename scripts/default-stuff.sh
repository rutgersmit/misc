#! /bin/bash
set -e
echo -n "❓  Run apt update && apt upgrade && reboot? (y/n) "
read updateupgrade

echo $updateupgrade

if [ "$updateupgrade" != "${updateupgrade#[Yy]}" ] ;then
  echo "🚀  Updating and upgrading."
  sudo apt update
  sudo apt upgrade -y
  
  echo -n "❓  Reboot now? (y/n) "
  read doreboot
  if [ "$doreboot" != "${doreboot#[Yy]}" ] ;then
    echo "➡  Rebooting now"
    sudo reboot
  fi
  
fi

echo -n "❓  Install ssh (y/n) "
read installssh
if [ "$installssh" != "${installssh#[Yy]}" ] ;then
  echo "🚀  Installing ssh"
  sudo apt install openssh-server -y
  echo "✔  Installed ssh"
fi

echo -n "❓  Install zsh and oh-my-zsh (y/n) "
read installzsh
if [ "$installzsh" != "${installzsh#[Yy]}" ] ;then
  echo "🚀  Installing zsh"
  sudo apt install zsh -y
  echo "✔  Installed zsh"
  
  echo "🚀  Installing oh-my-zsh"
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
  echo "✔  Installed oh-my-zsh"
fi


echo -n "❓  Set new hostname? (y/n) "
read setnewhostname

if [ "$setnewhostname" != "${setnewhostname#[Yy]}" ] ;then
  echo -n "❓  Enter new hostname: "
  read newhostname
  sudo hostnamectl set-hostname $newhostname
  sudo sed -i 's/preserve_hostname: false/preserve_hostname: true/g' config.cfg
  echo "✔  Hostname set"
fi


echo -n "❓  Add user rutger? (y/n) "
read addmyself

if [ "$addmyself" != "${addmyself#[Yy]}" ] ;then
  sudo adduser rutger
  sudo usermod -a -G sudo rutger
  echo "✔  User added"
fi

