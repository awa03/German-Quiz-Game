#!/bin/bash

if ! command -v pip &> /dev/null
then
  echo "pip could not be found"
  exit
fi

pip install dearpygui
pip install zufallsworte 
pip install deep_translator
