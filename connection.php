<?php
	$host="*****";
	$user="******";
	$pass="**********";
	$databasename="*************";
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
