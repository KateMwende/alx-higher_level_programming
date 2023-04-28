#!/bin/bash
#script that takes in a URL and displays all HTTP methods the server will accept
curl -s "$1" | grep "Accept" | cut -d " " -f 2- 
