git:
	$ git add .
	$ git add -A
	$ git commit -m "V 1.0.0.5"
	$ git push origin master

local:
	$ dev_appserver.py ~/Escritorio/encuentraCasa2/

server:
	$ dev_appserver.py --host=$(SRV) ~/Escritorio/encuentraCasa2/

upload:
	$ appcfg.py update ~/Escritorio/encuentraCasa2/ --oauth2