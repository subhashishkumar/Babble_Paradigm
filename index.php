<?php ob_start(); ?>
<html>
<head>
<title>Babble | HOME
</title>
<link rel="shortcut icon" href="fav.png">
<link rel="stylesheet" href="index.css">
<script>
	function checkr1()
	{
		var a,z;
		a=document.getElementById("m").value;
		z=/^[a-zA-Z0-9_]+$/;
		if(!a.match(z) || a.charCodeAt(0)==32)
		{
			document.getElementById("n").innerHTML="*";
			return 0;
		}
		else
		{
			document.getElementById("n").innerHTML="";
			return 1;
		}
	}

	function checkr2()
	{
		var a,z;
		a=document.getElementById("p").value;
		z=/^[a-zA-Z0-9#$%^&*()_+=~<>?]{7,30}$/;
		if(!a.match(z) || a=="")
		{
			document.getElementById("q").innerHTML="*";
			alert("Invalid password. Must be more than 6 characters");
			return 0;
		}
		else
		{
			document.getElementById("q").innerHTML="";
			return 1;
		}
	}

	function checkr3()
	{
		var a,z;
		a=document.getElementById("p").value;
		z=document.getElementById("ll").value;
		if(!(a==z))
		{
			document.getElementById("mm").innerHTML="*";
			alert("Passwords must be same");
			return 0;
		}
		else
		{
			document.getElementById("mm").innerHTML="";
			return 1;
		}
	}

	function register_now()
	{
		if(checkr1()==0 || checkr2()==0 || checkr3()==0)
		{
			checkr1();
			checkr2();
			checkr3();
		}
		else
		{
			document.getElementById("lastc").style.visibility="visible";
		}
	}

	function tick1()
	{
		document.getElementById("done").style.visibility="visible";
	}
</script>
<script src='https://code.responsivevoice.org/responsivevoice.js'></script>

</head>
<body>
<span id="done" style="position:absolute;background: rgba(26,255,26, 0.7); color:white; padding:3px; font-size: 1vw; width:30%; border-radius:3px; text-align: center; top:56%; left:32%; letter-spacing: 3px; visibility:hidden; word-spacing: 5px">&#x2714; You have been registered. Just Login now.</span>
<div class="background-div"></div>
<div id="upper">Welcome to Babble</div>

<div id="copyright">
	Copyright&#169; 2017 SHUBH LABWORKS All Rights Reserved. est.2017.
</div>

<form method="POST">

	<div class="login" >
		<div class="w">Login Here.</div>
		<input type="text" name="username" class="box1" placeholder="Username"><span class="username_error"></span><br><br>
		<input type="password" name="pass" class="box2" placeholder="Password"><span class="pass_error"></span><br><br>
		<button class="log" name="log">LogIn</button></div></form><form method="POST">
	<div class="register" >
		<div class="pp">Register from Here.</div>
		<input type="text" name="reg_username" class="reg_username1" id="m" onblur="checkr1()" placeholder="Username">
		<span class="reg_username_error" id="n"></span><br><br>
		<input type="password" name="reg_pass" class="reg_password1" id="p" placeholder="Password" onblur="checkr2()">
		<span class="reg_pass_error" id="q"></span><br><br>
		<input type="password" name="reg_cpass" class="reg_cpassword1" placeholder="Confirm Password" id="ll" 
		onblur="checkr3()">
		<span class="reg_cpass_error" id="mm"></span><br><br>
	</div>
	<div id="lastc">
			<div id="xxx">Continue for Confirmation</div>
			<input type="submit" id="continue" name="continue" value="Continue">
		</div>
<?php

if(isset($_POST['log']))
{
    @session_start();
	include("connection.php");
	$counter=0;
	try
	{	       
 	$r=mysqli_query($conn,"select * from user_info where username='$_POST[username]' and pass='$_POST[pass]'");
		if(!$r)
		{
			echo mysqli_error();
		}
		else
		{
			while($row=mysqli_fetch_row($r))
			{
				
                                $counter++;
				$_SESSION['name']=$row[0];
			}
		}
		if($counter==1)
		{
			$_SESSION['secure']=session_id();
			$_SESSION['name']=$_POST['username'];header("location:group_creation.php");
ob_end_flush();
}else
		{
			echo "<div class='my_comment'>";
			echo "<script>responsiveVoice.speak('Username not found. Please Sign Up');</script>";
			echo "<font color='red'>Username not found. Please Sign Up</font>";
			echo "</div>";
		}
	}
	catch(Exception $e)
	{
		echo $e;
	}
	
}
?>

</form>
<input type="submit" class="sign" name="sign" onclick="register_now()" value="SignIn">
<?php
	if(isset($_POST['continue']))
	{
		include("connection.php");
		$x=mysqli_query($conn,"select * from user_info where username= ".$_POST['reg_username'].";");
		if(!$x)
		{
			$ins=mysqli_query($conn,"insert into user_info values('$_POST[reg_username]','$_POST[reg_pass]');");
			if(!$ins)
			{
				echo "<font color='red'>Sorry, try sometimes later</font>";
			}
			else
			{
				echo "<script> tick1(); </script>";
				echo "<script>responsiveVoice.speak('You have been register. Now your a Babbler. Go---- LogIn ');</script>";
				
			}
		}
		else
		{
			?>
			<script>
				function s()
				{
					alert("username not available.");
				}
			</script>
			<?php
		}
	}
?>	

</body>
</html>