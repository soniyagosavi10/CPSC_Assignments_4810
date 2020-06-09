#!/usr/bin/env bash

(echo -e "Count   Dest" && cut -d',' -f18 2007.csv | sort | uniq -c |sort -r -n | head -3)> delayflight.csv

