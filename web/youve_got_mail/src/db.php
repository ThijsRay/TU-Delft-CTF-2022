<?php
require_once("config.php");

class Database extends SQLite3
{
  function __construct(bool $readonly = false)
  {
    if (!file_exists(DB_LOCATION)) {
      $this->setup();
    }

    $this->_open($readonly);
  }

  private function _open(bool $readonly)
  {
    if ($readonly) {
      $this->open(DB_LOCATION, SQLITE3_OPEN_READONLY);
    } else {
      $this->open(DB_LOCATION, SQLITE3_OPEN_READWRITE | SQLITE3_OPEN_CREATE);
    }
  }

  function __destruct()
  {
    $this->close();
  }

  private function setup(): bool
  {
    $this->_open(false);
    $this->exec("CREATE TABLE IF NOT EXISTS members (username TEXT, password TEXT, activated BOOLEAN, last_seen DATETIME)");
    $this->exec("CREATE TABLE IF NOT EXISTS roles (username TEXT, role_name TEXT)");
    $this->exec("CREATE TABLE IF NOT EXISTS posts (poster TEXT, title TEXT, post_content TEXT)");
    $this->exec("CREATE TABLE IF NOT EXISTS vouches (voucher TEXT, vouchee TEXT)");
    $this->exec("CREATE TABLE IF NOT EXISTS messages (from_user TEXT, to_user TEXT, content TEXT)");
    $this->exec("CREATE TABLE IF NOT EXISTS profile (username TEXT, biography TEXT, image TEXT)");
    $this->exec("CREATE TABLE IF NOT EXISTS settings (key TEXT, value TEXT)");

    // TODO: copy database and remove this
    $this->exec("INSERT INTO members (username, password, activated, last_seen) VALUES ('admin', 'ZblKhUWvdfuSek74lbE4', true, '2022-10-15 10:00:00')");
    $this->exec("INSERT INTO members (username, password, activated, last_seen) VALUES ('bob', 'ZblKhUWvdfuSek74lbE4', true, '2022-10-15 10:00:01')");
    $this->exec("INSERT INTO members (username, password, activated, last_seen) VALUES ('charlie', 'ZblKhUWvdfuSek74lbE4', true, '2022-10-15 10:00:02')");
    $this->exec("INSERT INTO members (username, password, activated, last_seen) VALUES ('denise', 'ZblKhUWvdfuSek74lbE4', true, '2022-10-15 10:00:03')");
    $this->exec("INSERT INTO members (username, password, activated, last_seen) VALUES ('fred', 'ZblKhUWvdfuSek74lbE4', true, '2022-10-15 10:00:04')");

    $this->exec("INSERT INTO roles (username, role_name) VALUES ('admin', 'admin')");
    $this->exec("INSERT INTO roles (username, role_name) VALUES ('bob', 'member')");
    $this->exec("INSERT INTO roles (username, role_name) VALUES ('charlie', 'member')");
    $this->exec("INSERT INTO roles (username, role_name) VALUES ('denise', 'member')");
    $this->exec("INSERT INTO roles (username, role_name) VALUES ('fred', 'member')");

    $this->exec("INSERT INTO posts (poster, title, post_content) VALUES ('admin', 'Welcome to the site!', 'It is still a work in progress but the basics should be working. If anybody has any suggestions, please send me a message. No stamp necessary!')");
    $this->exec("INSERT INTO posts (poster, title, post_content) VALUES ('charlie', 'Expert required', 'I have a rare stamp in my collection and I want an expert opinion on it. Anybody knows anybody who can help me?')");
    $this->exec("INSERT INTO posts (poster, title, post_content) VALUES ('denise', 'Stamp for sale', 'Selling this stamp from the year 1337. It is in a great state. Im open for any offer over 5k')");
    $this->exec("INSERT INTO posts (poster, title, post_content) VALUES ('charlie', 'RE: charlie', 'Hey charlie! I know about an expert in the field of stamps. Ill send you their contact information via private message')");
    $this->exec("INSERT INTO posts (poster, title, post_content) VALUES ('fred', 'POOR SEO PERFORMANCE?? WE CAN HELP!', 'WE OFFER GREAT SERVICES TO BOOST YOUR WEBSITES RANKING FOR _FREE_ SIGN UP NOW AT www (dot) THIS IS NOT SPAM BUT A GREAT GREAT DEAL (dot) com FOR YOUR _FREE_ TRAIL')");
    $this->exec("INSERT INTO posts (poster, title, post_content) VALUES ('admin', 'Sorry everybody', 'I am still working on the spam prevential system, it is not working great yet. Please ignore the previous message while I sort this out.')");
    $this->exec("INSERT INTO posts (poster, title, post_content) VALUES ('bob', 'RE: admin', 'No problem, I can understand the problem. Let us know if we can help')");

    $this->exec("INSERT INTO profile (username, biography, image) VALUES ('admin', 'Administrator of the site. Contact me if you have any issue with it.', '/images/profile/admin.jpeg')");
    $this->exec("INSERT INTO profile (username, biography, image) VALUES ('bob', 'My name is bob. i like stamps', '/images/profile/bob.jpeg')");
    $this->exec("INSERT INTO profile (username, biography, image) VALUES ('charlie', 'have a great collection of stamps, not sure what to do with them', '/images/profile/charlie.jpeg')");
    $this->exec("INSERT INTO profile (username, biography, image) VALUES ('denise', 'i am selling VERY RARE and VERY OLD stamps, message me for more information', '/images/profile/denise.jpeg')");
    $this->exec("INSERT INTO profile (username, biography, image) VALUES ('fred', 'GO TO DOUBLE U DOUBLE U DOUBLE U DOT NOT A SPAM SITE DOT COM AND SEE WHAT WE CAN OFFER TO YOU', '/images/profile/fred.jpeg')");

    $this->exec("INSERT INTO messages (from_user, to_user, content) VALUES ('admin', 'admin', 'TUDCTF{RE@DIn9_07hEr_P3OPlEs_L3t73rS_IS_n07_aLl0Wed_accorDiNG_7o_tHe_DU7CH_COns717U7i0n}')");
    $this->exec("INSERT INTO messages (from_user, to_user, content) VALUES ('admin', 'bob', 'Welcome on the site bob! If you have any feedback, please let me know')");
    $this->exec("INSERT INTO messages (from_user, to_user, content) VALUES ('admin', 'charlie', 'Welome on the site charlie! If you have any feedback, please let me know')");
    $this->exec("INSERT INTO messages (from_user, to_user, content) VALUES ('admin', 'denise', 'Welome on the site denise! If you have any feedback, please let me know')");
    $this->exec("INSERT INTO messages (from_user, to_user, content) VALUES ('admin', 'fred', 'Welome on the site fred! If you have any feedback, please let me know')");
    $this->exec("INSERT INTO messages (from_user, to_user, content) VALUES ('admin', 'fred', 'Stop spamming!')");
    $this->exec("INSERT INTO messages (from_user, to_user, content) VALUES ('charlie', 'charlie', 'Hey! You can mail me for more info but only physical mail please')");
    $this->exec("INSERT INTO messages (from_user, to_user, content) VALUES ('charlie', 'charlie', 'Oh whoops I was sending this to myself')");

    // END TODO

    $this->close();
    return false;
  }
}
