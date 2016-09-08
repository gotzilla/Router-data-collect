#!/bin/bash

echo

POST=$(</dev/stdin)

if [ "$REQUEST_METHOD" = "POST" ]; then
	read QUERY_STRING
fi

POST=$(echo $POST | sed -f /stockage/mrtg/test_IHM_DG/remplacement_de_caracteres.sed)

QUERY=`echo $POST | sed -e "s/=/='/g" -e "s/&/';/g" -e "s/+/ /g" -e "s/%0d%0a/<BR>/g" -e "s/$/'/" `
eval $QUERY



case $continent in
 afrique) continentSelectDescription="Afrique" ;;
 amerique_centrale) continentSelectDescription="Amerique centrale" ;;
 amerique_du_nord) continentSelectDescription="Amerique du nord" ;;
 amerique_du_sud) continentSelectDescription="Amerique du sud" ;;
 europe) continentSelectDescription="Europe" ;;
 moyen_orient) continentSelectDescription="Moyen orient" ;;
 *) continentSelectDescription="--- Faites un choix ---" ;;
esac

case $lien in
 dmvpn) lienSelectDescription="DMVPN" ;;
 ls) lienSelectDescription="Liaison specialisee" ;;
 bkpvpn) lienSelectDescription="Backup VPN" ;;
 *) lienSelectDescription="--- Faites un choix ---" ;;
esac
		
cat <<EOF
<!DOCTYPE html>
<html>
	<head>
		<script language=javascript>

			function OuvrirPopup(page,nom,option) 
			{
				window.open(page,nom,option);
			}
			
			function Soumettre()
			{
				document.Form1.target ='_parent';
				document.Form1.action ='/cgi-bin/index.py';
			}

			function SnmpPopup()
			{
				if((document.getElementById('nomDuRouteur').value) != '')
				{ 
					document.Form1.action ='/cgi-bin/polSnmp.py';
					pop_up=window.open ('','pop_up','fullscreen=no, height=500, width=500, resizable=no, scrollbars=1, scrolling=yes');
					document.Form1.target ='pop_up';
				}

				else
				{
					alert('Nom du routeur non defini');
				}
			}

			function ChoixLien()
			{
				if ((document.getElementById('lien').value) == 'ls')
				{
					document.getElementById("div_interface").style.display="block";
					document.getElementById("div_sla").style.display="block";
					document.getElementById("div_concentrateur").style.display="block";
					document.getElementById("div_debit_ls").style.display="block";
					document.getElementById("div_debit_vpn").style.display="none";
					document.Form1.debitVpn.selectedIndex = 0;
					document.Form1.debitVpn.options[0].selected="true";
					document.Form1.debitLs.options[0].selected="true";
					document.getElementById("div_debit_ls_perso").style.display="none";
					document.getElementById("div_infolien_ls_perso").style.display="none";
					document.getElementById("div_debit_vpn_perso").style.display="none";
					document.getElementById("div_infolien_vpn_perso").style.display="none";
					document.getElementById("debitVpn").value='';
				}

				else 
				{
					document.getElementById("div_interface").style.display="none";
					document.getElementById("div_sla").style.display="none";
					document.getElementById("div_concentrateur").style.display="none";
					document.getElementById("div_debit_ls").style.display="none";
					document.getElementById("div_debit_vpn").style.display="block";
					document.getElementById("routeurDestination").value='';
					document.Form1.debitVpn.selectedIndex = 0;
					document.Form1.debitVpn.options[0].selected="true";
					document.Form1.debitLs.options[0].selected="true";
					document.getElementById("div_debit_ls_perso").style.display="none";
					document.getElementById("div_infolien_ls_perso").style.display="none";
					document.getElementById("div_debit_vpn_perso").style.display="none";
					document.getElementById("div_infolien_vpn_perso").style.display="none";
				}
			}

			function ChoixDebitLs()
			{
				if ((document.getElementById("debitLs").value) == 'perso')
				{
					document.getElementById("div_debit_ls_perso").style.display="block";
					document.getElementById("div_infolien_ls_perso").style.display="block";
					document.getElementById("debitVpn").value='';
				}
				else
				{
					document.getElementById("div_debit_ls_perso").style.display="none";
					document.getElementById("div_infolien_ls_perso").style.display="none";
				}
			}

			function ChoixDebitVpn()
			{
				if ((document.getElementById("debitVpn").value) == 'perso')
				{
					document.getElementById("div_debit_vpn_perso").style.display="block";
					document.getElementById("div_infolien_vpn_perso").style.display="block";
					document.getElementById("debitLs").value='';
				}
				else
				{
					document.getElementById("div_debit_vpn_perso").style.display="none";
					document.getElementById("div_infolien_vpn_perso").style.display="none";					
				}
			}

		</SCRIPT>

		<meta charset="utf-8" />
		<link rel="stylesheet" href="/mrtg/test_IHM_DG/reset.css" />
		<link rel="stylesheet" href="/mrtg/test_IHM_DG/style.css" />
		<title>Briva - Administration MRTG</title>		

	</head>

	<body>
		<div id="bloc_page">

			<header>
				<div id="titre_principal">
					<H1>Service SERI - Briva</H1>
					<H2>Administration MRTG</H2>
				</div>
			</header>
			
			<div id="banniere_image">
				<div id="banniere_description">
					Outil de creation de configuration MRTG - Service SERI
				</div>
			</div>
			<section>
			<form name="Form1" id="Form1" method="POST" >
								
				<div id="section">
					<div id="type_de_liaison">
						<div id="a">
							<label for="type_de_liaison">Type de liaison</label>
						</div>
						<div id="b">
							<select name="lien" id="lien" onChange="ChoixLien();">
								<option selected value="$lien">$lienSelectDescription</option>
								<option value="bkpvpn">Backup VPN</option>
								<option value="dmvpn">DMVPN</option>
								<option value="ls">Liaison specialisee</option>
							</select>
						</div>
					</div>

					<div id="div_societe">
						<div id="a">Agence (AFP, SID...)</div>
						<div id="b">
							<input type="text" name="societe" value="$societe" />
						</div>
					</div>

					<div id="div_continent">

						<div id="a">
							<label for="Continent">Continent</label>
						</div>
						<div id="b">
							<select name="continent" id="continent">
								<option selected value="$continent">$continentSelectDescription</option>
								<option value="afrique">Afrique</option>
								<option value="amerique_centrale">Amerique centrale</option>
								<option value="amerique_du_sud">Amerique du sud</option>
								<option value="amerique_du_nord">Amerique du nord</option>
								<option value="asie">Asie</option>
								<option value="australie">Australie</option>
								<option value="europe">Europe</option>
								<option value="moyen_orient">Moyen orient</option>								
							<optgroup label="-- Personnalisation --">
								<option value="autre">Personnaliser --></option>
							</select>
						</div>
					</div>

					<div id="div_pays">
						<div id="a">Pays</div>
						<div id="b">
							<input type="text" name="pays" value="$pays"/>
						</div>
					</div>

					<div id="div_ville">
						<div id="a">Ville</div>
						<div id="b">
							<input type="text" name="ville" value="$ville" />
						</div>
					</div>

					<div id="div_routeur">
						<div id="a">Routeur</div>
						<div id="b">
							<input type="text" name="nomDuRouteur" id="nomDuRouteur" value="$nomDuRouteur" />
						</div>
					</div>

					<div id="div_interface" name="div_interface">
						<div id="a">Nom de l'interface</div>
						<div id="divNomInterface">
							<select name="nomInterface" id="nomInterface">
								<option value="" disabled>Cliquez sur le bouton</option>
							</select>
						</div>
						<div id="c">
							<INPUT type="submit" class="bouton_submit" name="previsualiser" id="previsualiser" value="Afficher interfaces" onClick="SnmpPopup()" />
						</div>
					</div>	

					<div id="div_debit_ls" >
						<div id="a">
							<label for="debit">Debit</label>
						</div>
						<div id="b">
							<select name="debitLs" id="debitLs" value="" onChange="ChoixDebitLs();">
								<option value="defaut">--- Faites un choix ---</option>
								<optgroup label="-- Liaison specialisee --">
									<option value="32000&bandePassante=Liaison Specialisee 256 Kbps">1) 256 Kbps</option>
									<option value="64000&bandePassante=Liaison Specialisee 512 Kbps">2) 512 Kbps</option>
									<option value="96000&bandePassante=Liaison Specialisee 768 Kbps">3) 768 Kbps</option>
									<option value="128000&bandePassante=Liaison Specialisee T1">4) T1</option>
									<option value="256000&bandePassante=Liaison Specialisee E1">5) E1</option>
									<option value="128000&bandePassante=Liaison Specialisee 1 Mbps">6) 1 Mbps</option>
									<option value="128000&bandePassante=Liaison Specialisee 2 Mbps">7) 2 Mbps</option>
									<option value="512000&bandePassante=Liaison Specialisee 4 Mbps">8) 4 Mbps</option>
									<option value="750000&bandePassante=Liaison Specialisee 6 Mbps">9) 6 Mbps</option>
									<option value="1250000&bandePassante=Liaison Specialisee 10 Mbps">10) 10 Mbps</option>
									<option value="2560000&bandePassante=Liaison Specialisee 20 Mbps">11) 20 Mbps</option>
									<option value="5625000&bandePassante=Liaison Specialisee 45 Mbps">12) 45 Mbps</option>
									<option value="6250000&bandePassante=Liaison Specialisee 50 Mbps">13) 50 Mbps</option>
									<option value="12500000&bandePassante=Liaison Specialisee 100 Mbps">14) 100 Mbps</option>
									<option value="19375000&bandePassante=Liaison Specialisee 155 Mbps">15) 155 Mbps</option>
									<option value="125000000&bandePassante=Liaison Specialisee 1 Gbps">16) 1 Gbps</option>
								<optgroup label="-- Personnalisation --">
									<option value="perso">20) Personnaliser --></option>
							</select>
						</div>
					</div>

					<div id="div_debit_vpn" style="display: none;">
						<div id="a">
							<label for="debit">Debit</label>
						</div>
						<div id="b">
							<select name="debitVpn" id="debitVpn" value="" onChange="ChoixDebitVpn();">
								<option value="defaut">--- Faites un choix ---</option>
								<optgroup label="------- DSL -------">
									<option value="64000&bandePassante=ADSL 512Kbps">1) ADSL 512 Kbps</option>
									<option value="125000&bandePassante=ADSL 1 Mbps">2) ADSL 1 Mbps</option>
									<option value="250000&bandePassante=ADSL 2 Mbps">3) ADSL 2 Mbps</option>
									<option value="500000&bandePassante=ADSL 4 Mbps">4) ADSL 4 Mbps</option>
									<option value="1000000&bandePassante=ADSL 8 Mbps">5) ADSL 8 Mbps</option>
									<option value="1250000&bandePassante=ADSL 10 Mbps">6) ADSL 10 Mbps</option>
									<option value="1875000&bandePassante=ADSL 15 Mbps">7) ADSL 15 Mbps</option>
									<option value="2500000&bandePassante=ADSL 20 Mbps">8) ADSL 20 Mbps</option>
								<optgroup label="-- Personnalisation --">
								<option value="perso">10) Personnaliser --></option>
							</select>
						</div>
					</div>

					<div id="div_debit_ls_perso" style="display: none;">
						<div id="a">Debit (En octets par seconde)</div>
						<div id="b">
							<input type="text" name="debitDeLaLiaison" id="debit" value="$debitDeLaLiaison" />
						</div>
					</div>

					<div id="div_infolien_ls_perso" style="display: none;">
						<div id="a">Infos (Ex : LS 10Mbps...)</div>
						<div id="b">
							<input type="text" name="debitDeLaLiaison" id="debit" value="$debitDeLaLiaison" />
						</div>
					</div>

					<div id="div_debit_vpn_perso" style="display: none;">
						<div id="a">Debit</div>
						<div id="b">
							<input type="text" name="debitDeLaLiaison" id="debit" value="$debitDeLaLiaison" />
						</div>
					</div>
					
					<div id="div_infolien_vpn_perso" style="display: none;">
						<div id="a">Infos (Ex : ADSL 10Mbps...)</div>
						<div id="b">
							<input type="text" name="debitDeLaLiaison" id="debit" value="$debitDeLaLiaison" />
						</div>
					</div>
					
					<div id="div_sla">
						<div id="a">Index SLA</div>
						<div id="b">
							<input type="text" name="indexIpSla" value="$indexIpSla" />
						</div>
					</div>					

					<div id="div_concentrateur">
						<div id="a">Routeur de concentration</div>
						<div id="b">
							<input type="text" name="routeurDestination" value="$routeurDestination" />
						</div>
					</div>

					<div id="bouton_submit">
						<div id="a"></div>
						<div id="b">
							<input type="submit" value="Generer la page MRTG" class="bouton_submit" onClick="Soumettre() ; window.pop_up.close();" />
						</div>
					</div>

				</div>
			</form>


			</section>

			<footer>
				<div id="footer">
				Interface Briva version 1.2
				</div>
			</footer>

		</div>

	</body>
</html>


EOF