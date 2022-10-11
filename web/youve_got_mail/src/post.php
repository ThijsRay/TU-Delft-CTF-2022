<?php
require_once('prelude.php');
if ($_SESSION['loggedin']) {
  exit('I have temporarily disabled posting posts because of spam issues. Private messages work in the mean time - admin');
} else {
  exit('You need to login first');
}
