# Italab interface for ITB HF SILENT ONE

Remote access to HF Silent One values on a computer via USB

Needed : 
- ITB / Italab HF Silent One or other model with a Nextion display screen
- Interface TTL to USB. Connect yellow cable (RXD) and black cable from Nextion connector to USB.

Access to TTL data from Nextion RXD pin:
Reverse ingeenering (Thank you Jean-Luc F1ULQ for help):

<code>
pwr direct					j0 	/10	
pwr ref						j2
current		x0		*100		j1
voltage		x1		*100		j4
temperature	x2		*100		j3
swr		x5 		*100 	
p4.pic=39     TX
p4.pic=38			RX
</code>

Sample Code in Python
