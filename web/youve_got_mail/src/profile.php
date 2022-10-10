<?php
require_once('config.php');
require_once('functions/members.php');
?>
</br>
</br>

<?php
$error = "";
$username = "";
$password = "";

function verify_login($username, $password, &$error): bool
{
  $db = new Database(true);
  $stmt = $db->prepare("SELECT COUNT(*) FROM members WHERE username=:u AND password=:p AND activated=true");
  $stmt->bindValue(':u', $username);
  $stmt->bindValue(':p', $password);

  $result = $stmt->execute();
  if ($result->fetchArray()[0] === 0) {
    $error = "Cannot find an activated user with these credentials";
    return false;
  } else {
    return true;
  }
}

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
  $username = $_GET['user'];

  $db = new Database(true);
  $stmt = $db->prepare("SELECT username, biography, image FROM profile WHERE username=:u");
  $stmt->bindValue(':u', $username);
  $result = $stmt->execute();
  $result = $result->fetchArray();
  if (!$result) {
    exit("User does not exist");
  }
} else {
  exit(0);
}
?>

<h2>Profile of <?= $result['username'] ?></h2>
<p><?= $result['biography'] ?></p>

Photo of <?= $result['username'] ?>
</br>
<img width="100px" src="<?= $result['image'] ?>">
