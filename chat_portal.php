<?php
ob_start();
session_start();
?>
<!DOCTYPE html>
<html>
<?php
include("connection.php");
	$name=$_SESSION['name'];
	$_SESSION['name']=$name;
	$group=$_SESSION['group'];
	$_SESSION['group']=$group;
?>
<head>
	<title></title>
	<link rel="shortcut icon" href="fav.png">

	<style>
		.background-div
		{
			position:fixed; height:100%; width:100%; left:0%; top:0%;
			opacity:0.15;
			background-image:url(b1.jpg);
			-moz-background-size: cover;
			-webkit-background-size:cover;
			-o-background-size:cover;
			background-size: cover;
		}
		#upper
		{
			position:absolute; padding:8px; font-size: 40px; color:white;
			top:0%; left:0%; width:100%; background-color:#000000;
			text-align: center; letter-spacing: 15px; word-spacing:30px;
		}
		#logout
		{
			position:absolute; left:88%; top:15%; padding:5px; background-color:black; color:white;
			text-align:center; font-size: 1.3vw; letter-spacing: 1px; border:thin solid black;
			border-radius:2px;
		}
		#logout:hover
		{
			cursor:pointer;
		}
		#log_f
		{
			position:absolute; left:88%; top:21.9%; padding:7px; background-color:rgba(0,0,0,0.7); color:white;
			text-align:center; font-size: 0.9vw; letter-spacing: 1px; border:thin solid black;
			border-radius:2px; display:none;
		}
		#log_f:hover
		{
			cursor:pointer;
		}
		#gr
		{
			position:absolute; left:1%; top:15%; padding:5px; background-color:black; color:white;
			text-align:center; font-size: 1vw; letter-spacing: 1px; border-color:black;
			border-radius:4px;
		}	
		#txt
		{
			position:absolute; top:80%; left:20%;
			width:50%; height:7%; border-radius:7px;
			font-size:1.2vw; padding-left: 15px; border-color:black;
		}
		#send_btn
		{
			position:absolute; left:71.5%; top:80%; width:10%; height:7.7%; background: rgba(0,0,0, 0.8); color:white;
			text-align:center; font-size: 1vw; letter-spacing: 1px; border-color:black;
			border-radius:7px; 
		}
		#send_btn:hover
		{
			cursor:pointer;
		}
		#show_text
		{
			position:absolute; top:15%; left:20%;
			width:60%; height:60%; border-radius:2px; background-color:  rgba(102, 204, 255,0.5);
			font-size:1.5vw; padding-left: 25px; overflow:auto;  border:thin solid #008ae6;
			padding-bottom: 10px;
		}
		#copyright
		{
			position:absolute; left:0%; top:96.2%; width:100%; background: rgba(0,0,0, 0.92);
			text-align:center; color:#ffffff; padding:5px; font-size: 0.9vw; letter-spacing: 2px;
		}
	</style>

	<script src='https://code.responsivevoice.org/responsivevoice.js'></script>

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<script>
		function chat_ajax(){
				 var req = new XMLHttpRequest(); 
				 req.onreadystatechange = function() {
				 	 if(req.readyState == 4 && req.status == 200){ 
				 	 	document.getElementById('show_text').innerHTML = req.responseText; 
				 	 	}
				 	 }
				  req.open('GET', 'auto_connect.php', true);
				   req.send(); }
			 setInterval(function(){chat_ajax()}, 1000)

			</script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<script>
		$(document).ready(function(){
			$("#logout").click(function(){
				$("#log_f").slideToggle("slow");
			});
		});
	</script>
</head>

<body>
<?php 
	include("connection.php");
	if($_SESSION['secure']==session_id())
	{
?>
	
<div class="background-div"></div>
<div id="upper">Welcome to Babble</div>
<span type="text" id="gr"> Group Code: <?php echo $group;?></span>
<button id="logout"><?php echo $name; ?><font size="5vw">&#9977;</font></button>

<form action="logout.php" method="POST">

<button id="log_f">Logout</button>
<?php
	if(isset($_POST['log_f']))
	{
		header("location : logout.php");
	}
?>
</form>
<form method="POST" action="chat_portal.php">

	<input name="send_txt" type="text" id="txt" placeholder="Write Your Message Here">
	<button name="send_btn" id="send_btn">SEND</button>	
	<div id="show_text" name="show_text">
	</div>

	<?php
	if(isset($_POST['send_btn']))
	{
		if(empty($_POST['send_txt']))
		{
			alert("Text filed cannot be blank");
		}
		else
		{
			date_default_timezone_set('Asia/Kolkata');
			$dt=date("d-m-y_h:ia");
			$ins=mysqli_query($conn,"insert into ".$group." (DateTime ,username, messages) values('$dt','$name','$_POST[send_txt]');");
			if(!$ins)
			{
				echo mysqli_error();
			}
			else
			{
				header("Refresh:0");
			}	
		}
	}
	?>
</form>
<?php
	}
	else
	{
		header("location:index.php");
	}
	
?>
		


	<div id="copyright">
		Copyright&#169; 2017 SHUBH LABWORKS All Rights Reserved. est.2017
	</div>

</body>
</html>