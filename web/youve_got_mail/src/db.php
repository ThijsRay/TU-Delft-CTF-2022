<?php
require_once("config.php");

class Database extends SQLite3
{
  private static $has_been_setup = false;

  function __construct($readonly = false)
  {
    if (!self::$has_been_setup) {
      $this->has_been_setup = $this->setup();
    }

    $this->__open($readonly);
  }

  private function __open($readonly)
  {
    if ($readonly) {
      $this->open(DB_LOCATION, SQLITE3_OPEN_READONLY);
    } else {
      $this->open(DB_LOCATION);
    }
  }

  function __destruct()
  {
    $this->close();
  }

  private function setup(): bool
  {
    $this->__open(false);
    $this->exec("CREATE TABLE IF NOT EXISTS members (username TEXT, password TEXT, activated BOOLEAN, last_seen DATETIME)");
    $this->exec("CREATE TABLE IF NOT EXISTS roles (username TEXT, role_name TEXT)");
    $this->exec("CREATE TABLE IF NOT EXISTS post_types (type TEXT)");
    $this->exec("CREATE TABLE IF NOT EXISTS posts (poster TEXT, post_type TEXT, post_content TEXT)");
    $this->exec("CREATE TABLE IF NOT EXISTS stamps (type TEXT, name TEXT, country TEXT, description TEXT, image TEXT, value NUMERIC, owned_by TEXT)");
    $this->exec("CREATE TABLE IF NOT EXISTS stamps_reactions (stamp_id INT, reaction_type TEXT, text TEXT, reacter TEXT)");
    $this->exec("CREATE TABLE IF NOT EXISTS vouches (voucher TEXT, vouchee TEXT)");
    $this->exec("CREATE TABLE IF NOT EXISTS messages (voucher TEXT, vouchee TEXT)");
    $this->exec("CREATE TABLE IF NOT EXISTS profile (username TEXT, biography TEXT, image TEXT)");
    $this->exec("CREATE TABLE IF NOT EXISTS settings (key TEXT, value TEXT)");
    $this->close();
    return false;
  }
}
