<?
	/*php module for faster connection to mysql*/
    $host = "localhost";
    $user = "";
    $password = "";
    $database = "";

    $db = new mysqli($host, $user, $password, $database);
    
    if ($db->connect_error) {
                die("Connection failed: " . $db->connect_error);
    }


?>