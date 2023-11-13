<h1 align="center">Yinamakasi Exploit (Stored XSS)</h1>

<p align="center">
Created by h3iko https://medium.com/@h3iko <br>
</p>

<p align="center">
<img src="cover.jpg" alt="Yinamakasi" width="500" height="500">
</p>

## Introduction

The Yinama microscope is a portable and wireless digital microscope made in China, equipped with a 2 MP camera and 8 adjustable LED lights. It is compatible with Android and iOS devices, as well as Windows and MacOS computers. It can operate using Wi-Fi or a cable, and to use it, you need to download an application (but we don't need it for this exploit).

This script exploits a Stored XSS vulnerability that I discovered in the manufacturer's configuration panel.

DISCLAIMER : This exploit works on Yinama microscopes, but as it is a white label product, it will probably works with other models that looks like this one.

## Context

The configuration panel of the Yinama microscope is vulnerable to a Stored XSS attack, which can lead to the injection of malicious files into the configuration panel. These malicious files could then be downloaded by a victim. The affected parameter is the SSID parameter.

## Installation

`git clone https://github.com/ilostmypassword/Yinamakasi-Exploit.git` <br>
`cd Yinamakasi-Exploit` <br>
`pip3 install -r requirements.txt` <br>
`chmod +x yinamakasi.py` <br>

## Usage

- The `a.htm` file can be modified as per your convenience; currently, it is the fake download page that I created, so you just need to change the IP adress at lines 48 to 54 to fit with your own (In hex or decimal).
- If you use this page, make sure to add your malicious files (MaxSee.* according to the platform).
- Connect to the Wi-Fi access point of the microscope.
- `python3 yinamakasi.py`

## Video PoC

[![Yinamakasi Exploit PoC](https://vimeo.com/828583512)](https://vimeo.com/828583512)
