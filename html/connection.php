<?php
/* Database connection start */
$servername = "db";
$username = "root";
$password = "password";
$dbname = "Alva_Server";

$conn = mysqli_connect($servername, $username, $password, $dbname) or die("Connection failed: " . mysqli_connect_error());

/* check connection */
if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}

?>