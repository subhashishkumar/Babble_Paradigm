<?php ob_start();
@session_start(); ?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<link rel="shortcut icon" href="fav.png">

<style>
	.background-div
	{
		position:fixed; height:100%; width:100%; left:0%; top:0%;
		opacity:0.4;
		background-image:url(g1.jpg);
		-moz-background-size: cover;
		-webkit-background-size:cover;
		-o-background-size:cover;
		background-size: cover;
	}
	#create
	{
		position:absolute; top:15%; left:30%; 
		width:40%; height:25%; background-color:#0099ff; border: thin solid #004d99; border-radius:15px; text-align:center;
	 background: rgba(0, 0, 0, 0.85); color:white;
	}
	#p
	{
		position:absolute; top:2%; left:15%;
		padding:5px; font-size: 1.3vw; letter-spacing: 3px; word-spacing: 6px;	}
	#create_room
	{
		position:absolute; top:35%; left:17%;
		width:60%; height:20%; border-radius:10px;
		font-size:1.5vw; padding-left: 40px;border: thin solid #004d99;
	}
	#create_btn
	{
		position:absolute; top:68%; left:40%;
		padding:4px; width:20%;
		font-size:1.4vw; background: rgba(0, 0, 0, 0.9); border: thin solid #33ccff;
		color:#33ccff; transition: 0.7s;
	}
	#create_btn:hover
	{
		background-color:#33ccff; cursor:pointer; color: #ffffff; box-shadow:0px 0px 30px #000000; 
	}
	#comment1
	{
		position:absolute; top:103%;left:20%; width:65%; 
		height:15%; color:red;
		font-size: 1.5vw;

	}
	#open
	{
		position:absolute; top:55%; left:30%;
		width:40%; height:25%; background-color:#0099ff; border: thin solid #004d99; border-radius:15px; text-align:center;
			 background: rgba(0, 0, 0, 0.85); color:white;
	}
	#w
	{
		position:absolute; top:2%; left:11%;
		padding:5px; font-size: 1.3vw; letter-spacing: 3px; word-spacing: 6px;
		font-size: 1.2vw;
	}
	#open_room
	{
		position:absolute; top:35%; left:17%;
		width:60%; height:20%; border-radius:10px;
		font-size:1.5vw; padding-left: 45px;border: thin solid #004d99;
	}
	#open_btn
	{
		position:absolute; top:68%; left:40%;
		padding:4px; width:20%;
		font-size:1.4vw;background: rgba(0, 0, 0, 0.9); border: thin solid #33ccff;
		color:#33ccff; transition: 0.7s;
	}
	#open_btn:hover
	{
		background-color:#33ccff; cursor:pointer; color: #ffffff; box-shadow:0px 0px 30px #000000; 
	}
	#comment2
	{
		position:absolute; top:103%;left:25%; width:65%; 
		height:15%;
		color:red; font-size: 1.5vw;
	}
	#logout
	{
		position:absolute; left:88%; top:5%; padding:3px; background-color:black; color:white;
		text-align:center; font-size: 1.3vw; letter-spacing: 1px; border:thin solid black;
		border-radius:2px;
	}
	#logout
	{
		cursor:pointer;
	}
	#copyright
	{
		position:absolute; left:0%; top:96.2%; width:100%; background: rgba(0,0,0, 1);
		text-align:center; color:#ffffff; padding:5px; font-size: 0.9vw; letter-spacing: 2px;
	}
</style>

<script>
	function codecode(n)
	{
		var n;
		document.getElementById("comment1").innerHTML=n;
	}
	function codec(n)
	{
		var n;
		document.getElementById("comment2").innerHTML=n;
	}
</script>
<script src='https://code.responsivevoice.org/responsivevoice.js'></script>
		
</head>

<?php
	include("connection.php");
	$name=$_SESSION['name'];
	if($_SESSION['secure']==session_id())
	{
		
?>
<body>


<div id="copyright">
	Copyright&#169; 2017 SHUBH LABWORKS All Rights Reserved. est.2017.
</div>
<div class="background-div"></div>
<form method="POST">
	<div id="create">
		<div id="p">Build your Unique Chat_Room Code</div><br>
		<input type="text" placeholder="Build Chat_room Code" id="create_room" name="create_room"><br><br>
		<button id="create_btn" name="create_btn">Build</button>
		<span id="comment1"></span>
	</div>
	

	<?php
		include("connection.php");
		if(isset($_POST['create_btn']))
		{
			if(empty($_POST['create_room']))
			{				
				echo "<script>codecode('Group Code cannot be blank');</script>";
			}
			else
			{
				$ins=mysqli_query($conn,"select * from ".$_POST['create_room'].";");
				if(!$ins)
				{
					echo "<script>codecode('Group Building in Process.');</script>";
					$k=mysqli_query($conn,"create table ".$_POST['create_room']." (id int(11) not null auto_increment primary key, DateTime varchar(35), username varchar(20), messages varchar(200))");
					if(!$k)
					{
						echo "<script>codecode('Sorry, try sometimes later.');</script>";
					}
					else
					{	

						echo "<script>responsiveVoice.speak('Hurray ! Your group has been created. Open your portal from below given space.');</script>";
						echo "<style>#comment1{color:green; left:10%;width:80%;}</style>";
						echo "<script>codecode('Your group has been created. Open your portal.');</script>";
					}
				}
				else
				{
					echo "<script>responsiveVoice.speak('sorry ------------its Unavailable . please Try another');</script>";
					echo "<script>codecode('Group code is unavailable. Try another.');</script>";
				}
			}
		}
	?>
</form>
<form method="POST" action="logout.php">
<button id="logout" name="logout"><?php echo $name; ?><font size="6vw">&#9977;</font><br><font size="2px">Logout</font></button>
<?php
	if(isset($_POST['logout']))
	{
		header("location: logout.php");
	}
?>
</form>
<form method="POST">
<?php
               
		include("connection.php");
		if(isset($_POST['open_btn']))
		{
			if(empty($_POST['open_room']))
			{
				
				echo "<script>codec('Group code cannot be blank.');</script>";
			}
			else
			{
				$open_t=mysqli_query($conn,"select * from ".$_POST['open_room'].";");
				if(!$open_t)
				{
					echo "<script>codec('Group Name does not Exist.');</script>";
				}
				else
				{
					$_SESSION['group']=$_POST['open_room'];
					$_SESSION['name']=$name;
					header("Location: chat_portal.php");
				}
			}
		}
	?>
<?php
	}
	else
	{header("Location:index.php");}
?>
	<div id="open">
		<div id="w">Open Chat_Room by Entering CR_Code.</div><br>
		<input type="text" placeholder="Enter Your Group Code" id="open_room" name="open_room"><br><br>
		<button id="open_btn" name="open_btn">Open</button>
		<span id="comment2"></span>
	</div>
	
</form>

</body>
</html>