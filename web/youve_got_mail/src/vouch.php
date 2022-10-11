<?php
require_once('prelude.php');

$user = $_GET['user'];

if ($user) {
  $db = new Database();
  $stmt = $db->prepare("UPDATE members SET activated=true WHERE username=:u");
  $stmt->bindValue(':u', $user, SQLITE3_TEXT);
  $stmt->execute();
  exit('vouched for user ' . $user . '!');
} else {
  exit("user does not exist");
}
