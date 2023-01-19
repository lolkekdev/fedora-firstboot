#! /usr/bin/bash

sudo dnf install inxi htop neofetch vim ranger flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
sudo curl http://sandrospadaro.altervista.org/sandrospadaro.repo --output /etc/yum.repos.d/sandrospadaro.repo
sudo dnf install rmtrash