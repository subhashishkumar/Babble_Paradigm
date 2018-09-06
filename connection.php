<?php
	$host="localhost";
	$user="id2377547_root";
	$pass="shubhshubh1";
	$databasename="id2377547_babble";
	$conn=mysqli_connect($host,$user,$pass);
	if($conn)
	{
		$selection_db=mysqli_select_db($conn,$databasename);
		if(!$selection_db)
		{
			die ("Can't connect : ".mysqli_error());
		}
	}
	else
	{
		die ("Not connected : ".mysqli_error());
	}
?>