<?php
require_once('config.php');
require_once('functions/members.php');
?>
eMailers is an online community for mail and stamp enthousiast. eMailers is a fairly closed community, so you can only register when another user vouches for you.
</br>
</br>

<?php
$username = "";
$password = "";
$voucher = "";
$error = "";

function verify_registration($username, $password, $voucher, &$error): bool
{
  if (!preg_match("/[a-z]{0,17}/", $username)) {
    $error = "Error: Username must be at most 16 lowercase characters";
    return false;
  }
  if (!preg_match("/[a-z0-9A-Z]{6,256}/", $password)) {
    $error = "Error: Password can only consists of 6 to 256 alphanumeric characters.";
    return false;
  }
  if (!Member::exists($voucher)) {
    $error = "Vouching member does not exist. Only existing members can vouch for new members.";
    return false;
  }
  if (Member::exists($username)) {
    $error = "User already exists. Please choose another username.";
    return false;
  }
  return true;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $username = $_POST['username'];
  $password = $_POST['password'];
  $voucher = $_POST['voucher'];

  if (verify_registration($username, $password, $voucher, $error)) {
    $member = new Member($username, $password);
    $member->addMember();

    $db = new Database();
    $message = "Welcome to the site " . $username . '! If you have any feedback, let me know';
    $stmt = $db->prepare("INSERT INTO messages (from_user, to_user, content) VALUES ('admin', :u, :c)");
    $stmt->bindValue(':u', $username);
    $stmt->bindValue(':c', $message);
    $stmt->execute();

    echo "Thank you for signing up! Whenever the existing member activates your membership, you are allowed to log in.";
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
  <label>Security question: which country introduced a chocolate flavoured stamp in 2013?
    <input name="security" type="text" pattern="Belgium" required value="">
  </label>
  </br>
  </br>
  <label>User who vouches for you
    <input name="voucher" type="text" pattern="[a-z]{0,16}" required value="<?= $voucher ?>">
  </label>
  </br>
  </br>
  <input type="submit" value="Submit registration request">
  <input type="reset" value="Reset registration">
</form>
