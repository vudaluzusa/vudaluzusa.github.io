#!/usr/bin/python
import sys, os, os.path
filename = sys.argv[1];
extension = os.path.splitext(filename)[1];

if extension == ".txt":
  os.system("gedit " + filename);

if extension == ".mp4":
  os.system("vlc " + filename);
  
if extension == ".html":
  os.system("opera " + filename);
  
if extension == ".py":
  os.system("python " + filename);
  
if extension == ".sh":
  os.system("bash " + filename);
  
if extension == ".exe":
  os.system("wine " + filename);
  
exit()
