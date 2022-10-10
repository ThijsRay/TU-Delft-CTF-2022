<?php
require('prelude.php');

$db = new Database(true);
$result = $db->query("SELECT poster, title, post_content FROM posts ORDER BY rowid DESC");

?>

<a href="/register">Click here to register</a></br>

<?php
if (isset($_SESSION['loggedin'])) {
  echo "Logged in as " . $_SESSION['user'];
  echo "</br><a href='/message?user=" . $_SESSION['user'] . "'>View messages</a>";
  echo "</br><a href='/post'>Publish a post</a>";
  echo "</br><a href='/logout'>Logout</a>";
} else { ?>
  <a href="/login">Click here to login</a>
<?php } ?>
<h1>Latest posts</h1>
<?php
while ($row = $result->fetchArray()) { ?>
  <h2><?= $row['title']; ?></h2>
  posted by <a href='/profile?user=<?= $row['poster'] ?>'><?= $row['poster'] ?></a>
  </br>
  <?= $row['post_content'] ?>
<?php
}
?>
