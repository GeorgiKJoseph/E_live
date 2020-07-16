# E_live
###### E_live is a django + arduino app for home automation and monitoring
Home automation is one of the popular trends in tech right now, but it's still a luxury. A usual household only worries about their electricity consumption only after they receive the bill.
E_live helps to monitor, track, automate and analyse electricity usage and foresee upcoming bill.

## Installation
The project is still in the developing stage, so some features may won't work:(

* install django, clone this repository.
* start virtualenv, install requirements.txt (required python packages).
* Upload code to audrino: audrino/final.ino
* if linux, modify port permission when ever audrino is connected.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; in ubuntu: `sudo chmod a+rw /dev/ttyACM0`

## Implementation

* connect audrino to the pc, in ubuntu modify port permission `sudo chmod a+rw /dev/ttyACM0` (/dev/ttyACM0 may be different depends on which port audrino is connected)
* runserver: `python manage.py runserver 0.0.0.0:8000`
* take another terminal: `python digi_phy_interface.py` 
* if you are under a local network (browse : `http://pc_current_ip:8000`) web is currently designed for smartphones.

## Design & Documentation

[Documentation (Google Drive)](https://drive.google.com/open?id=1uFiIMQDyL_0s0cy2kcOE5sBEz3lxEvRRTxvR3xHAKI0)

###### working sample
<div>
  <div style="width: 25%; float:left; margin: 5%;">
    <img src="https://github.com/GeorgiKJoseph/E_live/blob/redesign/images/working%20sample%20off.jpeg" width="45%">
 </div>
 <div style="width: 25%; float:left; margin: 5%;">
   <img src="https://github.com/GeorgiKJoseph/E_live/blob/redesign/images/working%20sample%20on.jpeg" width="45%">
 </div>
 <div>
   <img src="https://github.com/GeorgiKJoseph/E_live/blob/redesign/images/mulDev.jpg" width="45%">
 </div>
