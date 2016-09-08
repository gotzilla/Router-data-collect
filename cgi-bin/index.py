#!/bin/bash
#set -x            Mode debug

#horodatage=$(date "+%A %d %B %Y a %Hh%M")
#echo "$horodatage"

echo
POST=$(</dev/stdin)

if [ "$REQUEST_METHOD" = "POST" ]; then 
	read QUERY_STRING 
fi 

POST=$(echo $POST | sed -f ./remplacement_de_caracteres.sed)

echo $POST

QUERY=`echo $POST | sed -e "s/=/='/g" -e "s/&/';/g" -e "s/+/ /g" -e "s/%0d%0a/<BR>/g" -e "s/$/'/" `
eval $QUERY

echo
echo "#Fichier de configuration cree le $horodatage"
echo 'lien :'$lien
echo 'societe :'$societe
echo 'continent :'$continent
echo 'pays :'$pays
echo 'ville :'$ville
echo 'nomDuRouteur :'$nomDuRouteur
echo 'nomInterface :'$nomInterface
echo 'debitDeLaLiaison :'$debitDeLaLiaison
echo 'indexIpSla :'$indexIpSla
echo 'routeurDestination :'$routeurDestination
echo 'InfoLien (bandePassante) :'$bandePassante

echo 'indexInterface :'$indexInterface

nomInterfaceFichier=$(echo $nomInterface | sed s:/:-:g)

echo
echo "./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterfaceFichier~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info"
echo

echo "#Fichier de configuration cree le $horodatage"                  >  ./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterfaceFichier~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info
echo "lien=\"$lien\""                                                 >> ./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterfaceFichier~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info
echo "societe=\"$societe\""                                           >> ./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterfaceFichier~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info
echo "continent=\"$continent\""                                       >> ./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterfaceFichier~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info
echo "pays=\"$pays\""                                                 >> ./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterfaceFichier~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info
echo "ville=\"$ville\""                                               >> ./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterfaceFichier~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info
echo "nomDuRouteur=\"$nomDuRouteur\""                                 >> ./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterfaceFichier~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info
echo "nomInterface=\"$nomInterface\""                                 >> ./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterfaceFichier~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info
echo "debitDeLaLiaison=\"$debitDeLaLiaison\""                         >> ./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterfaceFichier~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info
echo "indexIpSla=\"$indexIpSla\""                                     >> ./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterfaceFichier~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info
echo "routeurDestination=\"$routeurDestination\""                     >> ./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterfaceFichier~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info
echo "bandePassante=\"$bandePassante\""                               >> ./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterfaceFichier~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info
echo "index=\"$index\""                                               >> ./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterfaceFichier~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info

echo

cat ./$societe~$continent~$pays~$ville~$nomDuRouteur~$nomInterface~$debitDeLaLiaison~$indexIpSla~$routeurDestination~$lien.info

