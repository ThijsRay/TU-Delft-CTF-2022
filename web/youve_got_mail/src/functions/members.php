<?php
require_once("prelude.php");

class Member
{
  private $id;
  private $username;
  private $password;
  private $is_activated;
  private $last_seen;

  private function __construct($username, $password)
  {
    $this->username = $username;
    $this->password = $password;
    $this->is_activated = false;
    $this->last_seen = time();
  }

  public function addMember($username, $password)
  {
    if (!$this->exists($username)) {
      $db = new Database();
      $query = sprintf(
        "INSERT INTO members (username, password, activated, last_seen) VALUES (%s, %s, %d, %d)",
        $username,
        $password,
        $this->is_activated,
        $this->last_seen
      );
      $db->exec($query);
    }
  }

  static function exists($username): bool
  {
    $db = new Database(true);
    $stmt = $db->prepare("SELECT COUNT(*) FROM members WHERE username == :username");
    $stmt->bindValue(':username', $username, SQLITE3_TEXT);
    $result = $stmt->execute();
    print_r($result->fetchArray());
    return false;
  }
}
