<?php
	include("connection.php");
	@session_start();
	$group=$_SESSION['group'];
	$str=mysqli_query($conn,"select * from ".$group." order by id desc;");
	if(!$str)
	{
		echo mysqli_error();
	}
	else
	{
		while($row=mysqli_fetch_row($str))
		{
			echo "<font color='gray' size='2vw'>".$row[1]."</font> _ <font face='Comic Sans MS' size='4vw'>".$row[2].": ".$row[3]."</font><br>"; 
		}
	}
?>