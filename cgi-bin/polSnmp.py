#!/bin/bash
#set -x            Mode debug

#Parametres de langues
#horodatage=$(date "+%A %d %B %Y a %Hh%M")

echo
echo

POST=$(</dev/stdin)
echo $POST

if [ "$REQUEST_METHOD" = "POST" ]; then
read QUERY_STRING
fi

POST=$(echo $POST | sed -f /stockage/mrtg/test_IHM_DG/remplacement_de_caracteres.sed)

echo $POST

QUERY=`echo $POST | sed -e "s/=/='/g" -e "s/&/';/g" -e "s/+/ /g" -e "s/%0d%0a/<BR>/g" -e "s/$/'/" `
eval $QUERY


snmpwalk -c strt $nomDuRouteur -v 2c .1.3.6.1.2.1.2.2.1.2 -t 100 | grep -vi '\(Null\|Loopback\|EFXS\|POTS\|Voice\|Foreign\|Backplane\)' > /stockage/mrtg/test_IHM_DG/$societe.$continent.$pays.$ville.$nomDuRouteur.$nomInterfaceFichier.$debitDeLaLiaison.$indexIpSla.$routeurDestination.$lien.pollingSnmp.temp~

while read line;
do
 echo -e "$line" | sed s:IF-MIB:\<br\>\ IF-MIB:g | cut -f'1,5' -d' '; 
done < /stockage/mrtg/test_IHM_DG/$societe.$continent.$pays.$ville.$nomDuRouteur.$nomInterfaceFichier.$debitDeLaLiaison.$indexIpSla.$routeurDestination.$lien.pollingSnmp.temp~

echo '<select name=\"nomInterface\" id=\"nomInterface\">' >  testIntegrationHtml.code
echo -e "<option value=default>--- Interface ---</option>" >> testIntegrationHtml.code

while read line
do   
echo -e "<option value=$line>$line</option>\n"  >> testIntegrationHtml.code
done < /stockage/mrtg/test_IHM_DG/$societe.$continent.$pays.$ville.$nomDuRouteur.$nomInterfaceFichier.$debitDeLaLiaison.$indexIpSla.$routeurDestination.$lien.pollingSnmp.temp~
echo '</select>'  >> testIntegrationHtml.code
rm -f /stockage/mrtg/test_IHM_DG/$societe.$continent.$pays.$ville.$nomDuRouteur.$nomInterfaceFichier.$debitDeLaLiaison.$indexIpSla.$routeurDestination.$lien.pollingSnmp.temp~


cat <<EOF
plop
EOF