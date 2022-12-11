# 6TiSCH protocol data sniffer

This repository contains flowgraph created in GNURadio environment as part of my masters thesis. 

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)

## General info

Presented in this repository flowgraph is an implementation of 6TiSCH protocol data sniffer. Packets in this flowgraph are captured and saved into the SQLite database. This flowgraph consists of only two channels but can be easily expanded to multiple more channels.

![flowgraph](https://i.imgur.com/FFkTnJa.png)

Repository structure:

    .
    ├── Database            # Directory where SQLite database file is stored
	└── DataSniffer     	# This directory contains flowgraph description in form of .grc file and python scripts generated from .grc            

## Screenshots

https://youtu.be/2_eWu4YBrdA

## Technologies
* GNURadio v3.10.1.1 
* RTL2832U
* Ubuntu 22.04

## Setup
I would highly recommend to install GNURadio on Ubuntu in version 22.04. Even though this projec could be run in previous versions of Ubuntu and on Windows, GNURadio is far more easier to install on verison 22.04. Install GNURadio:

`sudo apt-get install gnuradio`

Open GNURadio Companion:

`gnuradio-companion`

Open .grc file in GNURadio Companion and execute it. 

## To-do list:
All is done :D

## Status
Project is: _finished_
