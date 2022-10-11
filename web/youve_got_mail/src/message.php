<?php
require_once('config.php');
require_once('functions/members.php');
?>
</br>
</br>

<?php
if (isset($_SESSION['loggedin'])) {
  $user = $_GET['user'];
  $db = new Database(true);
  $stmt = $db->prepare("SELECT from_user, to_user, content FROM messages WHERE to_user=:u ORDER BY rowid DESC");
  $stmt->bindValue(':u', $user);

  $result = $stmt->execute();
  while ($row = $result->fetchArray()) {
    echo "<h1>A message</h1>";
    echo "from " . $row['from_user'] . "</br>";
    echo "to " . $row['to_user'] . "</br>";
    echo "<h3>Message content</h3>";
    echo $row['content'];
  }
} else {
  exit("You can only see messages when you are logged in");
}
?>
