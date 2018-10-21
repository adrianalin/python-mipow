Python control for Mipow smart LED bulbs
=========================================

A simple python API for [Mipow Smart](https://www.amazon.com/MIPOW-PLAYBULB-Bluetooth-changing-Waterproof/dp/B0188P93JC) Bluetooth LE lightbulbs
Based on the work by Matthew Garret on [python-zengge](https://github.com/mjg59/python-zengge) 

Modify this code in order to work with Playbulb Sphere BTL301W.
- 0x1b the color handle
- 0x19 the effect handle
- the correct order for setting collor is w/r/g/b

Great documentation at https://github.com/Heckie75/Mipow-Playbulb-BTL201.git

Notes
-----

Note that this has been written against a specific bulb, and may misbehave on some other bulbs that speak a similar protocol. Please get in touch if you have a bulb that partially works with this code.
