#!/bin/bash
#set -x            Mode debug

#Parametres de langues
#horodatage=$(date "+%A %d %B %Y a %Hh%M")

echo

echo
POST=$(</dev/stdin)
echo $POST
echo 'content length:'$CONTENT_LENGTH

if [ "$REQUEST_METHOD" = "POST" ]; then
        read QUERY_STRING
fi


echo SERVER_SOFTWARE = $SERVER_SOFTWARE
echo SERVER_NAME = $SERVER_NAME
echo GATEWAY_INTERFACE = $GATEWAY_INTERFACE
echo SERVER_PROTOCOL = $SERVER_PROTOCOL
echo SERVER_PORT = $SERVER_PORT
echo REQUEST_METHOD = $REQUEST_METHOD
echo HTTP_ACCEPT = "$HTTP_ACCEPT"
echo PATH_INFO = "$PATH_INFO"
echo PATH_TRANSLATED = "$PATH_TRANSLATED"
echo SCRIPT_NAME = "$SCRIPT_NAME"
echo QUERY_STRING = "$QUERY_STRING"
echo REMOTE_HOST = $REMOTE_HOST
echo REMOTE_ADDR = $REMOTE_ADDR
echo REMOTE_USER = $REMOTE_USER
echo AUTH_TYPE = $AUTH_TYPE
echo CONTENT_TYPE = $CONTENT_TYPE
echo CONTENT_LENGTH = $CONTENT_LENGTH

if [ "$SCRIPT_NAME" = "/cgi-bin/polSnmpV2.py" ]; then
	echo "OuvrirPopup('','popup_win','fullscreen=no, height=500, width=500, noresize=yes, scrolling=yes, 
scrollbars=1')"
fi

POST=$(echo $POST | sed -f /stockage/mrtg/test_IHM_DG/remplacement_de_caracteres.sed)



hop=$(snmpwalk -c strt cis-mow1 -v 2c .1.3.6.1.2.1.2.2.1.2 -t 100)

hop=$(echo $hop | sed s:IF-MIB:\<br\>IF-MIB:g)


cat <<EOF
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<link rel="stylesheet" href="http://mrtg1/mrtg/test_IHM_DG/style.css" />
<title>Briva - Liste des interfaces et des indexes du routeur</title>
</head>

<body>
<div id="bloc_page">
<header>
<div id="titre_principal">
<H1>Service SERI - Briva</H1>
<H2>Administration MRTG</H2>
</div>
</header>

<section>
<p>$hop</p>

</section>

<footer>
<div id="footer">
Interface Briva version 1.0
</div>
</footer>

</div>

</body>
</html>

EOF
