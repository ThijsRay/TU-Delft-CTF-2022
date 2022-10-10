<?php
require_once("prelude.php");

class Member
{
  private $id;
  private $username;
  private $password;
  private $is_activated;
  private $last_seen;

  public function __construct($username, $password)
  {
    $this->username = $username;
    $this->password = $password;
    $this->is_activated = false;
    $this->last_seen = time();
  }

  public function addMember()
  {
    if (!$this->exists($this->username)) {
      $db = new Database();
      $stmt = $db->prepare(
        "INSERT INTO members (username, password, activated, last_seen) VALUES (:u, :p, :a, :ls)"
      );
      $stmt->bindValue(':u', $this->username, SQLITE3_TEXT);
      $stmt->bindValue(':p', $this->password, SQLITE3_TEXT);
      $stmt->bindValue(':a', $this->is_activated, SQLITE3_INTEGER);
      $stmt->bindValue(':ls', $this->last_seen, SQLITE3_TEXT);
      $stmt->execute();
    }
  }

  static function exists($username): bool
  {
    $db = new Database(true);
    $stmt = $db->prepare("SELECT COUNT(*) FROM members WHERE username == :username");
    $stmt->bindValue(':username', $username, SQLITE3_TEXT);
    $result = $stmt->execute();
    if ($result->fetchArray()[0] === 0) {
      return false;
    } else {
      return true;
    }
  }
}
