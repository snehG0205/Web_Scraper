<?php
$servername = "localhost";
$username = "root";
$password = "";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully";

$username = $_POST["username"];
$password = $_POST["password"];

$sql = "INSERT INTO usr_tbl (Username, Password) VALUES ('$username', '$password');";

if (mysqli_query($conn,$sql)) {
    echo "Registration successful";
}
else{
	echo "Registration Failed";
}
?>
