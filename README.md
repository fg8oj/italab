# Italab interface for ITB HF SILENT ONE

Remote access to HF Silent One values on a computer

Interface TTL to USB. Connect yellow cable (RXD) and black cable from Nextion connector to USB.

Access to TTL data from Nextion RXD pin :
Reverse ingeenering (Thank you Jean-Luc F1ULQ for help):

pwr direct					j0 	/10	
pwr ref						j2
current		x0		*100		j1
voltage		x1		*100		j4
temperature	x2		*100		j3
swr		x5 		*100 	
p4.pic=39vis m3,		TX
t1.pic=51			RX
