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

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $username = $_POST['username'];
  $password = $_POST['password'];

  if (verify_login($username, $password, $error)) {
    echo "Login succesful!";
    $_SESSION['loggedin'] = True;
    $_SESSION['user'] = $username;
    exit();
  }
}
?>

<style>
  input:invalid {
    border-color: red;
  }
</style>

<div><b><?= $error ?></b></div>
</br>
<form method="post">
  <label>Username (maximum of 16 lowercase characters):
    <input name="username" type="text" pattern="[a-z]{0,16}" required value="<?= $username ?>">
  </label>
  </br>
  </br>
  <label>Password (between 6 to 256 alphanumeric characters):
    <input name="password" type="password" minlength="6" pattern="[a-z0-9A-Z]{6,256}" maxlength="256" required value="<?= $password ?>">
  </label>
  </br>
  </br>
  <input type="submit" value="Login">
  <input type="reset" value="Reset login">
</form>
