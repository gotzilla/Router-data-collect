<?php

echo "<!DOCTYPE html>";
echo "<html>";
echo "<body>";

echo '<div id="d">';
echo '</div>';
		
$host = $_GET['param1'];

$community = "";

//$a = snmpwalk("$host", "$community", "iso.org.dod.internet.mgmt.mib-2.interfaces.ifTable.ifEntry.ifDescr");
$a['iface'] = snmpwalk("$host","$community",".1.3.6.1.2.1.2.2.1.2");
$a['value'] = snmpwalk("$host","$community",".1.3.6.1.2.1.2.2.1.1");

echo 
'
	<form method="post" action="traitement.php">
		<p>
			Veuillez sélectionner l\'interface du routeur ' . $_GET['param1'] . ' :<br />
';

foreach ($a['iface'] as $key => $element)
{
	if (stristr($element, "giga") || stristr($element, "fast"))
	{
		echo '<div id="d">';
		echo explode('"', $element)[1] . '  |  Index SNMP : ' . explode(' ', $a['value'][$key])[1] . ' <br />' ;
		echo '</div>';
		//		echo $a['value'][$key] . ' <br />' ;
	}
	echo 
	'
		</p>
		</form>
	';
}



//while ($a != "")

/*
$host = "$host"; 
$community = "$community"; 

	$sysDescr = snmpget("$host","$community","system.sysDescr.0"); 
//$ifDescr = snmpwalk("$host","$community","interfaces.ifTable.ifEntry.ifDescr"); 
//	$ifAdminStatus = snmpwalk("$host","$community","interfaces.ifTable.ifEntry.ifAdminStatus"); 
//	$ifOperStatus = snmpwalk("$host","$community","interfaces.ifTable.ifEntry.ifOperStatus"); 
//	$ifLastChange = snmpwalk("$host","$community","interfaces.ifTable.ifEntry.ifLastChange"); 

echo "<table border=1 bgcolor=#ffffff><tr><td>$host</td></tr></table><br>";
echo "<table border=1 bgcolor=#ffffff><tr><td>$sysDescr</td></tr></table><br>"; 
echo "<table border=1 bgcolor=#ffffff>";
echo "<tr> 
	<td>ifIndex</td> 
	<td>ifDescr</td> 
	<td>ifAdminStatus</td> 
	<td>ifOperStatus</td> 
	<td>ifLastChange</td> 
	</tr>"; 
			 
for ($i=0; $i<count($ifIndex); $i++) { 
	echo "<tr>"; 
	echo "<td>$ifIndex[$i]</td>"; 
	echo "<td>$ifDescr[$i]</td>"; 
	echo "<td>$ifAdminStatus[$i]</td>"; 
	echo "<td>$ifOperStatus[$i]</td>"; 
	echo "<td>$ifLastChange[$i]</td>"; 
	echo "</tr>"; 
}
echo "</table>"; 
*/


echo "</body>";
echo "</html>";

?>
