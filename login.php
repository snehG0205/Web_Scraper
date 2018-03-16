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

$sql = "SELECT * FROM usr_tbl WHERE Username LIKE '$username' AND Password LIKE '$password';";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "Login successful";
}
else{
	echo "Login Failed";
}
?>
